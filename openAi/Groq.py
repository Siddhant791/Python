from typing import Annotated, TypedDict
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END

# 1. Define calculation tools
@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide two numbers. Returns error if dividing by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# 2. Initialize Groq client with current model
groq_api_key = "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"
model = ChatGroq(
    temperature=0,
    # model_name="llama3-70b-8192",
    model_name="gemma2-9b-it",
    groq_api_key=groq_api_key
).bind_tools([add, multiply, divide])

# 3. Define State with proper message handling
class AgentState(TypedDict):
    messages: Annotated[list, lambda x, y: x + y]

# 4. Updated Nodes with proper termination
def model_node(state: AgentState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

def tool_node(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]

    tool_calls = last_message.tool_calls
    if not tool_calls:
        return {"messages": [AIMessage(content="No tools called")]}

    tool_call = tool_calls[0]
    tool_name = tool_call["name"]
    args = tool_call["args"]

    # Execute tool
    result = globals()[tool_name].run(args)

    # Create tool message with proper format
    tool_message = ToolMessage(
        content=str(result),
        name=tool_name,
        tool_call_id=tool_call["id"]
    )

    return {"messages": [tool_message]}

# 5. Configure workflow with termination
workflow = StateGraph(AgentState)
workflow.add_node("model", model_node)
workflow.add_node("tool", tool_node)
workflow.set_entry_point("model")

def decide_next_step(state):
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "tool"
    return END

workflow.add_conditional_edges(
    "model",
    decide_next_step,
    {"tool": "tool", END: END}
)
workflow.add_edge("tool", "model")
app = workflow.compile()

# 6. Run with recursion limit config
result = app.invoke(
    {"messages": [HumanMessage(content="What is 3 plus 5 multiplied by 2?")]},
    {"recursion_limit": 100}  # Increased limit for complex calculations
)

# Print conversation history
for msg in result["messages"]:
    print(f"{msg.type}: {msg.content}")