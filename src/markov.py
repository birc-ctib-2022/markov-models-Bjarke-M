"""Markov models."""


from mimetypes import init



class MarkovModel:
    """Representation of a Markov model."""

    init_probs: list[float]
    trans: list[list[float]]

    def __init__(self,
                init_probs: list[float],
                trans: list[list[float]]):
        """Create model from initial and transition probabilities."""
        # Sanity check...
        k = len(init_probs)
        assert k == len(trans)
        for row in trans:
            assert k == len(row)
        self.init_probs = init_probs
        self.trans = trans



def likelihood(x: list[int], mm: MarkovModel) -> float:
    """
    Compute the likelihood of mm given x.

    This is the same as the probability of x given mm,
    i.e., P(x ; mm).
    """
    ...  
    i=0
    acc= mm.init_probs[x[0]]
    while i < len(x):
        acc *= mm.trans[x[i]][x[i]]
        i += 1
    return acc

#def par_estimator():



    #trans = If you see n[i] outcomes of state i, in n experiments, 
    #then the maximum likelihood parameter for the probability of 
    #seeing result i in a single experiment is n[i]/n.

    # starts:
    # For the starting probabilities in a Markov model, 𝜋, you have a multinomial distribution. 
    # If you see n runs of the Markov model, 
    # and n[i] of the start in state i, then the maximum likelihood parameter for 𝜋 has 𝜋[i]=n[i]/n.

    # The transition parameter, T, is not a multinomial distribution. That is because it 
    # is a set of conditional probabilities, row k is the conditional probability P(X[i]|X[i-1]=k). 
    # Each of the rows are multinomial distributions, and you can estimate the paramers as such.
    #  Take one row at a time, say T[k,-], then look at all the transitions out of k—those are the states
    #  you are conditioning on—and count how many times you move to each state. If you move from k to h n[k,h] 
    #  times, and you move out of a k state n[k] times, then T[k,h]=n[k,h]/n[k].