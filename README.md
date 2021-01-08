## Combinatorial game theory
![Tests](https://github.com/InnovativeInventor/cgt/workflows/Tests/badge.svg)

Generalized deterministic recursive/dynamic combinatorial game theory calculator for evaluating the state of any two-person game that has a corresponding number.
Only uses vanilla python and pydantic (for type-checking).

Rationale:
> The best way to understand a process is to write a program automating it.

## Example game (Push)
```python
from cgt.game import GameTree
from cgt.pushpin import PushPinGame

case = PushPinGame(["", "L", "R"])
print(GameTree(case).value())
```

Output:
``` python
>>> -1.75
```

## Implementing your own game

```python
class AbstractGame():
    """
    Example of required methods and functions that must be implemented
    """
    def __init__(self, state: AbstractState = AbstractState()): # some state to pass to the game
        raise NotImplementedError

    def moves(self) -> List[List[AbstractState]]: # return a list of moves for each player
        """
        Returns the possible moves left. If there are no moves left, return empty lists.
        """
        raise NotImplementedError

    def apply(self, state: AbstractState): # takes a state and applies it to the game
        """
        Apply a move or "state" return by moves.
        """
        raise NotImplementedError
```

For a real-live working example, see [`cgt/pushpin.py`](/cgt/pushpin.py)
