def getitem(M, k):
    """
    Returns the value of entry k in M, where k is a 2-tuple
    >>> M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
    >>> M[1,'a']
    4
    >>> M[3,'a']
    0
    """
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f[k] if k in M.f else 0

def transpose(M):
    """
    Returns the matrix that is the transpose of M.

    >>> M = Mat(({0,1}, {0,1}), {(0,1):3, (1,0):2, (1,1):4})
    >>> M.transpose() == Mat(({0,1}, {0,1}), {(0,1):2, (1,0):3, (1,1):4})
    True
    >>> M = Mat(({'x','y','z'}, {2,4}), {('x',4):3, ('x',2):2, ('y',4):4, ('z',4):5})
    >>> Mt = Mat(({2,4}, {'x','y','z'}), {(4,'x'):3, (2,'x'):2, (4,'y'):4, (4,'z'):5})
    >>> M.transpose() == Mt
    True
    """
    return Mat((M.D[1], M.D[0]), {(c,r):M[r,c] for (r,c) in M.f})

class Mat:

    def __init__(self, labels, function):
        assert isinstance(labels, tuple)
        assert isinstance(labels[0], set) and isinstance(labels[1], set)
        assert isinstance(function, dict)
        self.D = labels
        self.f = function

    __getitem__ = getitem
    transpose = transpose

    def __repr__(self):
        "evaluatable representation"
        return "Mat("+ str(self.D) + ", " + str(self.f) + ")"

    def __str__(self):
        return "Mat("+ str(self.D) + ", " + str(self.f) + ")"
