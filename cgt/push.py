from typing import List, Tuple
from copy import deepcopy

# PushState = List[str]
PushState = Tuple[str]


class PushGame:
    """
    Push game implementation
    state is a list of "L", "R", or ""
    """

    def __init__(self, state: PushState = ()):
        self.state = state
        self.possible_moves = self.moves()

    def moves(self) -> List[List[PushState]]:
        """
        Return the possible moves left. If there are no moves left, return empty lists.
        """
        # seen_moves = set()
        possible_moves = [[], []]

        if state := self.prune_states(self.state):  # Could return None
            size = len(self.prune_states(state))
        else:
            return possible_moves

        for count, each_slot in enumerate(state):
            # for count, each_slot in reversed(list(enumerate(state))):
            if each_slot == "L" and not possible_moves[0]:
                next_state = deepcopy(state)
                next_state = tuple(self.push(list(next_state), count))
                next_state = self.prune_states(next_state)

                # if next_state not in seen_moves:
                #     seen_moves.add(next_state)
                possible_moves[0].append(next_state)

            elif each_slot == "R" and not possible_moves[1]:
                next_state = deepcopy(state)
                next_state = tuple(self.push(list(next_state), count))
                next_state = self.prune_states(next_state)

                # if next_state not in seen_moves:
                #     seen_moves.add(next_state)
                possible_moves[1].append(next_state)

            if possible_moves[0] and possible_moves[1]:
                break

        return possible_moves

    def push(self, state: List[str], index: int) -> List[str]:
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

    def apply(self, state: PushState):
        """
        Apply a move or "state" return by moves.
        """
        self.state = state

    @staticmethod
    def prune_states(state: PushState) -> PushState:
        """
        Gets rid of empty hanging squares and normalizes the state.
        """
        if state and not state[-1]:
            return PushGame.prune_states(state[:-1])
        else:
            return state
