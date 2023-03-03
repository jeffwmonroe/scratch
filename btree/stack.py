from enum import Enum


class ListType(Enum):
    Stack = 1
    Queue = 2


class Stack():
    def __init__(self, list_type=ListType.Stack):
        print('initialing a stack object')
        self.stack = []
        self.listType = list_type

    def push(self, item):
        if self.listType == ListType.Stack:
            self.stack[len(self.stack):] = [item]
        else:
            self.stack[:-len(self.stack)] = [item]

    def pop(self):
        if len(self.stack) == 0:
            return None

        val = self.stack[-1]
        self.stack = self.stack[:-1]

        return val
