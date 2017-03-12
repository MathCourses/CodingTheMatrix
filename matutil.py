from mat import Mat
from vec import Vec

def identity(D):
    """ Given a set D and the field's one, returns the DxD identity matrix
    e.g.:

    >>> identity({0,1,2} 1)
    Mat(({0,1,2}, {0,1,2}), {(0,0):1, (1,1):1, (2,2):1})
    """
    return Mat((D,D), {(d,d):1 for d in D})

# I = identity({1,2,3})
# print(I)

def mat2coldict(A):
    """Given a matrix, return a dictionary mapping column labels of A to columns of A
           e.g.:
           >>> M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
           >>> mat2coldict(M)
           {0: Vec({0, 1, 2},{0: 3, 1: 4, 2: 8}), 1: Vec({0, 1, 2},{0: 1, 1: 0, 2: -2})}
           >>> mat2coldict(Mat(({0,1},{0,1}),{}))
           {0: Vec({0, 1},{0: 0, 1: 0}), 1: Vec({0, 1},{0: 0, 1: 0})}
    """
    return {c:Vec(A.D[0], {r:A[(r,c)] for r in A.D[0]}) for c in A.D[1]}
#
# M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
# d = mat2coldict(M)
# print(d)

# Comprehension quizzes
# R = [[0 for j in range(4)] for i in range(3)]
# print(R)
#
# C = [[i-j for i in range(3)] for j in range(4)]
# print(C)

M = Mat(({'a','b'}, {0}), {('a',0):10, ('b',0):20})
Mt = M.transpose()
print(Mt)