from cgt.game import GameTree
from cgt.pushpin import PushPinGame
import itertools
from typing import List


def calculate_value(state=List[str]) -> int:
    """
    Uses alternate method to calculate values
    """
    l_bin_be = []
    r_bin_be = []

    for val in state:
        if val == "L":
            l_bin_be.append("1")
            r_bin_be.append("0")
        elif val == "R":
            r_bin_be.append("1")
            l_bin_be.append("0")
        else:
            r_bin_be.append("0")
            l_bin_be.append("0")

    l_bin = "".join(reversed(l_bin_be))
    r_bin = "".join(reversed(r_bin_be))

    if l_bin:
        l = int(l_bin, 2)
    else:
        l = 0

    if r_bin:
        r = int(r_bin, 2)
    else:
        r = 0

    return l - r


known_mapping = {}
assertion_mapping = {}

# generate mapping
for state in itertools.product(["R", "", "L"], repeat=2):
    pruned_state = PushPinGame.prune_states(state)

    case = PushPinGame(pruned_state)
    value = GameTree(case).value()
    known_mapping[tuple(pruned_state)] = GameTree(case).value()

    assertion_mapping[tuple(pruned_state)] = calculate_value(pruned_state)

# debug
print("Known", known_mapping)
print("Assertion", assertion_mapping)

# assertion/hypothesis testing
for seq_1, seq_2 in itertools.combinations(known_mapping.keys(), 2):
    print(seq_1, seq_2)
    if known_mapping[seq_1] > known_mapping[seq_2]:
        assert assertion_mapping[seq_1] > assertion_mapping[seq_2]
    elif known_mapping[seq_1] == known_mapping[seq_2]:
        assert assertion_mapping[seq_1] == assertion_mapping[seq_2]
    elif known_mapping[seq_1] < known_mapping[seq_2]:
        assert assertion_mapping[seq_1] < assertion_mapping[seq_2]
