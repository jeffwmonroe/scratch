import btree.node as node

# from btree.node import Node, SearchOrder, SearchDirection

# print("---------------------")
# print("Welcome to Python")
# print("")


# todo Set up test suite
# todo reconfigure to the __main__ style


def main():
    # print('inside of the main function')
    y = node.Node()
    y.populate()
    y.topdown()
    y.traverse(node.SearchOrder.BreadthFirst, node.SearchDirection.RightToLeft)


if __name__ == '__main__':
    # print('main being run')
    main()
