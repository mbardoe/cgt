from cgt.pushpin import PushPinGame
from cgt.game import GameTree


def test_empty_case():
    empty_case = PushPinGame()
    number = GameTree(empty_case).value()
    assert number == 0


def test_one_case():
    case = PushPinGame(["L"])
    print(case.moves())
    number = GameTree(case).value()
    assert number == 1


def test_q1_case():
    case = PushPinGame(["L", "", "R"])
    assert -2 == GameTree(case).value()


def test_q1_sub1_case():
    case = PushPinGame(["L", "R"])
    assert -1.5 == GameTree(case).value()


def test_q2_case():
    case = PushPinGame(["", "L", "R"])
    assert -1.75 == GameTree(case).value()


def test_q3_case():
    case = PushPinGame(["L", "L", "R"])
    assert -1.625 == GameTree(case).value()


def test_q4_case():
    case = PushPinGame(["L", "R", "L"])
    assert float(15 / 8) == GameTree(case).value()
