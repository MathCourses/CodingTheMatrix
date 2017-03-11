from mat import Mat

def identity(D):
    """ Given a set D and the field's one, returns the DxD identity matrix
    e.g.:

    >>> identity({0,1,2} 1)
    Mat(({0,1,2}, {0,1,2}), {(0,0):1, (1,1):1, (2,2):1})
    """
    return Mat((D,D), {(d,d):1 for d in D})

I = identity({1,2,3})
print(I)

# Comprehension quizzes
# R = [[0 for j in range(4)] for i in range(3)]
# print(R)
#
# C = [[i-j for i in range(3)] for j in range(4)]
# print(C)