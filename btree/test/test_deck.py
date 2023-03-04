from btree.deck import Deck, ListType


def test_stack():
    stype = ListType.Stack
    deck = Deck(stype)

    values = [1, 2, 3, 4, 5, 6, 7, 8]
    gold = list(reversed(values[:]))

    result = []

    for i in values:
        deck.push(i)

    for item in deck:
        result[len(result):] = [item]

    assert gold == result


def test_queue():
    deck = Deck(ListType.Queue)

    values = [1, 2, 3, 4, 5, 6, 7, 8]
    gold = values[:]
    result = []

    for i in values:
        deck.push(i)

    for item in deck:
        result[len(result):] = [item]

    assert gold == result
