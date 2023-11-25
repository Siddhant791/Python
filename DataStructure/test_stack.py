from Stack import Stack
import pytest

def test_push():
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(5)
    expected_list = [3, 5]
    actual_list = test_stack.stack

    for element in actual_list:
        assert element in expected_list


def test_pop():
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(5)
    actual_popped_value = 5
    expected_popped_value = test_stack.pop()
    assert actual_popped_value == expected_popped_value


def test_is_empty():
    test_stack = Stack()
    test_stack.push(3)
    assert not test_stack.isEmpty()
    test_stack.pop()
    assert test_stack.isEmpty()


def test_peek():
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(5)
    assert 5 == test_stack.peek()
    assert 5 == test_stack.peek()
    assert 5 == test_stack.pop()
    assert 3 == test_stack.peek()

def test_exception():
    test_stack = Stack()
    with pytest.raises(ValueError):
        test_stack.pop()
    with pytest.raises(ValueError):
        test_stack.peek()

