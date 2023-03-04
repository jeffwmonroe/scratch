from btree.node import Node, SearchOrder, SearchDirection


def populate_btree():
    """ This function populates the btree with known value in a known structure.
    The node label is r + depth + breadth order
    Therefore r11 is the root
    r23 is depth two and third from the right at depth 2
    The idea is that the naming should make it easier to debug errors"""
    r31 = Node("r31")
    r32 = Node("r32")
    r33 = Node("r33")
    r34 = Node("r34")

    r21 = Node("r21", r31, r32)
    r22: Node = Node("r22", r33, r34)

    root = Node("r11")

    root.left = r21
    root.right = r22
    return root


gold_depth_left_to_right = ['r11', 'r21', 'r31', 'r32', 'r22', 'r33', 'r34']
gold_depth_right_to_left = ['r11', 'r22', 'r34', 'r33', 'r21', 'r32', 'r31']
gold_breadth_left_to_right = ['r11', 'r21', 'r22', 'r31', 'r32', 'r33', 'r34']
gold_breadth_right_to_left = ['r11', 'r22', 'r21', 'r34', 'r33', 'r32', 'r31']

node_for_testing = populate_btree()


def test_depth_left_to_right():
    result = node_for_testing.traverse(SearchOrder.DepthFirst, SearchDirection.LeftToRight)
    assert result == gold_depth_left_to_right


def test_depth_right_to_left():
    result = node_for_testing.traverse(SearchOrder.DepthFirst, SearchDirection.RightToLeft)
    assert result == gold_depth_right_to_left


def test_breadth_left_to_right():
    result = node_for_testing.traverse(SearchOrder.BreadthFirst, SearchDirection.LeftToRight)
    assert result == gold_breadth_left_to_right


def test_breadth_right_to_left():
    result = node_for_testing.traverse(SearchOrder.BreadthFirst, SearchDirection.RightToLeft)
    assert result == gold_breadth_right_to_left
