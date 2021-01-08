from pydantic import BaseModel
from typing import Tuple, List
from typing import TypeVar, Generic

"""
Example implementation of a general nimber game.
Note: Could use type vars for proper type-checking.
"""

"""
Abstract state can be a class, set, or other pythonic representation of the
game's current state. It should fully encapsulate the game's state and not
include the history of the game.
"""

AbstractState = TypeVar("T")


class AbstractGame:
    """
    Example of required methods and functions that must be implemented
    """

    def __init__(self, state: AbstractState = AbstractState()):
        self.state = state
        self.possible_moves = self.moves()

    def moves(self) -> List[List[AbstractState]]:
        """
        Returns the possible moves left. If there are no moves left, return empty lists.
        """
        raise NotImplementedError

    def apply(self, state: AbstractState):
        """
        Apply a move or "state" return by moves.
        """
        self.state = state

    @staticmethod
    def prune_states(self, state: PushPinState) -> PushPinState:
        """
        Normalizes the state
        """
        raise NotImplementedError
