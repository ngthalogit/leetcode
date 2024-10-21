from xmlrpc.client import FastParser


def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == '{':
            stack.append('}')
        elif not stack or stack.pop() != char:
            return False
    return not stack
