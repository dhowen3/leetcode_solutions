class StackNode:
    def __init__(self, value, next_node):
        self.next = next_node
        self.value = value

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = StackNode(value, None)
        else:
            self.head = StackNode(value, self.head)

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value
    def peek(self):
        print(self.head.value)

class Solution:
    def perform_operation(self, value1, value2, operator):
        if operator == '+':
            return value1 + value2
        if operator == '-':
            return value1 - value2
        if operator == '*':
            return value1 * value2
        if operator == '/':
            return int(value1 / value2)
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.push(self.perform_operation(val2, val1, token)) 
            else:
                stack.push(int(token))


            stack.peek()

        return stack.pop()
