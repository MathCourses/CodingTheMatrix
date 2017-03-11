from vec import Vec

def zero_vec(D):
    return Vec(D, {})

def list2vec(L):
    return Vec(set(range(len(L))), {k:x for k,x in enumerate(L)})

def triangular_solve(rowlist, b):
    """
    Solve Ax = b for vector x and rowlist = A
    :param rowlist: a representation of matrix A
    :param b: representation for solution vector b
    :return: representation of vector x
    """
    x = zero_vec(rowlist[0].D)
    for i in reversed(range(len(rowlist))):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x

def triangular_solve2(rowlist,label_list, b):
    """
    Solve Ax = b for vector x and rowlist = A
    For arbitrary domains, need to specify an order for which the system is "triangular"
    :param rowlist: a representation of matrix A
    :param b: representation for solution vector b
    :return: representation of vector x
    """
    x = zero_vec(set(label_list))
    for r in reversed(range(len(rowlist))):
        c = label_list[r]
        x[c] = (b[r] - rowlist[r] * x)/rowlist[r][c]
    return x
#
# list = ['A', 'B', 'C', 'D']
# v = list2vec(list)
# print(v)
#
# # v = Vec({'A','B','C'}, {'A':1})
# # for d in v.D:
# #     if d in v.f:
# #         print(v.f[d])