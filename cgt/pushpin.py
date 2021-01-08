from typing import List
from copy import deepcopy

PushPinState = List[str]

class PushPinGame:
    """
    Pushpin game implementation
    state is a list of "L", "R", or ""
    """

    def __init__(self, state: PushPinState = []):
        self.state = state
        self.possible_moves = self.moves()

    def moves(self) -> List[List[PushPinState]]:
        """
        Return the possible moves left. If there are no moves left, return empty lists.
        """
        possible_moves = [[], []]

        if state := self.prune_states(self.state):  # Could return None
            size = len(self.prune_states(state))
        else:
            return possible_moves

        for count, each_slot in enumerate(state):
            if each_slot == "L":
                next_state = deepcopy(state)
                next_state = self.push(next_state, count)
                next_state = self.prune_states(next_state)

                possible_moves[0].append(next_state)

            elif each_slot == "R":
                next_state = deepcopy(state)
                next_state = self.push(next_state, count)
                next_state = self.prune_states(next_state)

                possible_moves[1].append(next_state)

        return possible_moves

    def push(self, state: PushPinState, index: int) -> PushPinState:
        """
        Push a square, specified by its index
        """
        pusher = state[index]
        state[index] = ""

        for i in range(index, 0, -1):
            new_pusher = state[i - 1]
            state[i - 1] = pusher

            if pusher := new_pusher:
                pass
            else:
                break

        return state

    def apply(self, state: PushPinState):
        """
        Apply a move or "state" return by moves.
        """
        self.state = state

    def prune_states(self, state: PushPinState) -> PushPinState:
        """
        Gets rid of empty hanging squares.
        """
        if state and not state[-1]:
            return self.prune_states(state[:-1])
        else:
            return state
