from enum import Enum


class ListType(Enum):
    Stack = 1
    Queue = 2


class Deck:
    def __init__(self, list_type=ListType.Stack):
        print('initialing a stack object')
        self.deck = []
        self.listType = list_type

    def __iter__(self):
        return self

    def __next__(self):
        result = self.pop()
        if result is None:
            raise StopIteration

        return result

    def push(self, item):
        if self.listType == ListType.Stack:
            self.deck[len(self.deck):] = [item]
        else:
            self.deck[:-len(self.deck)] = [item]

    def pop(self):
        if len(self.deck) == 0:
            return None

        val = self.deck[-1]
        self.deck = self.deck[:-1]

        return val
