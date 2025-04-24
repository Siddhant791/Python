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

import os
from pathlib import Path

@tool
def read_folder_files(folder_path: str = "./documents") -> str:
    """Reads all files in specified folder and returns their content as context."""
    all_content = []
    try:
        for file_path in Path(folder_path).glob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        all_content.append(f"Content of {file_path.name}:\n{content}\n")
                except Exception as e:
                    all_content.append(f"Error reading {file_path.name}: {str(e)}")
        return "\n".join(all_content)
    except Exception as e:
        return f"Error accessing folder: {str(e)}"

@tool
def homily() -> str:
    """This function gives description of homily company"""
    return ("Homily is a france based starytup which provides the home services through there platform like massag, makeeup, couifer etc."
            "It's CEO is abhinav , harshit and siddhant"
            "Very effieint company"
            "50k users"
            "widely used by france people"
            "unicorn"
            "referral 5 euro"
            "harshita designer foundoing memb")

@tool
def siddhant():
    """About Siddhant"""
    return "Founder of homily and best friend of harish"

@tool
def harish():
    """Harish description"""
    return "Senior software engineer manhaten associate, Best friend Siddhant, Best person, Gym boy, 6 packs, 34 inch chest, Single 2kids"


# 2. Initialize Groq client with current model
groq_api_key = "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"
model = ChatGroq(
    temperature=0,
    # model_name="llama3-70b-8192",
    model_name="gemma2-9b-it",
    groq_api_key=groq_api_key
).bind_tools([add, multiply, divide, homily, harish, siddhant, read_folder_files])

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
    {"messages": [HumanMessage(content="First read our documents folder at './documents', then tell me the variable name of map")]},
    {"recursion_limit": 100}  # Increased limit for complex calculations
)

# Print conversation history
for msg in result["messages"]:
    if msg.type is not "tool":
        print(f"{msg.type}: {msg.content}")