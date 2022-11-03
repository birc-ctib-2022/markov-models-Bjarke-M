"""Testing Markov models."""
from markov import likelihood
from markov import MarkovModel

def test_me() -> None:
    """Test your code."""
    ...
    assert likelihood([0,1],MarkovModel([0.5,0.5],[[0.5,0.5],[0.5,0.5]])) == 0.125