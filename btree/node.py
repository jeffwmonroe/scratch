from btree.stack import Stack, ListType
from enum import Enum
#todo need to implement a test suite

class SearchDirection(Enum):
    LeftToRight = 1,
    RightToLeft = 2


class SearchOrder(Enum):
    DepthFirst = 1,
    BreadthFirst = 2


class Node:
    def __init__(self, label: object = None, left: object = None, right: object = None) -> object:
        # print("initializing node")
        self.left = left
        self.right = right
        self.label = label

    def topdown(self):
        """This is the recursive definition of the depth first search"""
        print(f'label = {self.label}')
        if self.left is not None:
            self.left.topdown()
        if self.right is not None:
            self.right.topdown()

    def traverse(self, order=SearchOrder.DepthFirst, direction=SearchDirection.LeftToRight):
        """THis is the non-resursive variant of the search function."""
        if order == SearchOrder.DepthFirst:
            stack = Stack(ListType.Stack)
        else:
            stack = Stack(ListType.Queue)

        stack.push(self)
        while True:
            val = stack.pop()
            if val is None:
                break
            print(f'label = {val.label}')
            search = (order, direction)
            right_first = True
            match search:
                case (SearchOrder.DepthFirst, SearchDirection.LeftToRight):
                    right_first = True
                case (SearchOrder.DepthFirst, SearchDirection.RightToLeft):
                    right_first = False
                case (SearchOrder.BreadthFirst, SearchDirection.LeftToRight):
                    right_first = False
                case (SearchOrder.BreadthFirst, SearchDirection.RightToLeft):
                    right_first = True

            if right_first:
                if val.right is not None:
                    stack.push(val.right)
                if val.left is not None:
                    stack.push(val.left)
            else:
                if val.left is not None:
                    stack.push(val.left)
                if val.right is not None:
                    stack.push(val.right)

#todo this needs to go into the test suite
    def populate(self):
        r31 = Node("r31")
        r32 = Node("r32")
        r33 = Node("r33")
        r34 = Node("r34")

        r21 = Node("r21", r31, r32)
        r22: Node = Node("r22", r33, r34)

        self.label = 'r11'
        self.left = r21
        self.right = r22
