#!/usr/bin/env python3
from stack import Stack

def doMath(operand1, operand2, operand):
    if operand == "*":
        return operand1 * operand2
    elif operand == "/":
        return operand1 / operand2
    elif operand == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2

def postfixEval(postfix):
    operandStack = Stack()
    tokenList = postfix.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            oprand2 = operandStack.pop()
            oprand1 = operandStack.pop()
            result = doMath(oprand1, oprand2, token)
            operandStack.push(result)
    return operandStack.pop()


print(postfixEval('7 8 + 3 2 + /'))
