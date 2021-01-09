from typing import TypeVar, Generic, List
import math
from copy import deepcopy

CACHE = {}  # for performance


class GameTree:
    """
    Game state calculated using a recursive tree.
    For an example game implementation, see `example.py`
    """

    def __init__(self, starting_state=None):
        self.starting_state = starting_state

        self.move_tree: List[list] = [[], []]

    def __lt__(self, other):
        if self.value() - other.value() < 0:
            return True
        else:
            return False

    def value(self) -> float:
        """
        Recursively calculate game value
        """
        left_moves, right_moves = self._construct_tree(self.starting_state)

        left = None  # the value of left's best move
        right = None  # the value of right's best moves

        if left_moves:
            starting_state = False
            left = max(left_moves).number

        if right_moves:
            starting_state = False
            right = min(right_moves).number

        try:
            self.number = self.smallest_power_between(left, right)

        except (TypeError, ZeroDivisionError):  # Zen
            if isinstance(right, float) and not isinstance(left, float):
                # self.number = (-1)*right - 1
                self.number = right - 1
            elif isinstance(left, float) and not isinstance(right, float):
                # self.number = left + 1
                self.number = left + 1
            elif (not isinstance(left, float)) and (not isinstance(right, float)):
                self.number = 0.0
            else:
                if left == right:
                    self.number = 0.0
                else:
                    raise ValueError

        return self.number

    def smallest_power_between(self, left: float, right: float) -> float:
        """
        Calculate the smallest power of two between left and right that is
        closest to zero.
        """
        positive_difference = right - left

        if 0 > left and 0 < right:
            return 0.0

        power = 0
        while pow(2, power) <= 1 / (positive_difference):
            power += 1

        if abs(right) > abs(left):
            number = math.floor(left)
            while number <= left:
                number += 1 / pow(2, power)

        elif abs(right) < abs(left):
            number = math.ceil(right)
            while number >= right:
                number -= 1 / pow(2, power)

        else:
            raise ValueError

        return float(number)

    def _construct_tree(self, starting_state):
        """
        Recursively construct move tree
        """
        if starting_state:
            for index, player in enumerate(starting_state.moves()):
                for each_move in player:
                    each_move = starting_state.prune_states(each_move)  # normalize

                    # child_game = deepcopy(starting_state)
                    child_game = starting_state.__class__(each_move)

                    # the apply function is delegated to the game class
                    # because it's out of scope for this class
                    # child_game.apply(each_move)
                    child_tree = GameTree(child_game)

                    if each_move in CACHE:  # check cache
                        child_tree.number = CACHE[each_move]
                    else:
                        CACHE[each_move] = child_tree.value()

                    self.move_tree[index].append(child_tree)

        return self.move_tree
