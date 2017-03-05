from vec import Vec

def zero_vec(D):
    return Vec(D, {})

def list2vec(L):
    return Vec(set(range(len(L))), {k:x for k,x in enumerate(L)})


list = ['A', 'B', 'C', 'D']
v = list2vec(list)
print(v)

# v = Vec({'A','B','C'}, {'A':1})
# for d in v.D:
#     if d in v.f:
#         print(v.f[d])