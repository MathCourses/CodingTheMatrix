def getitem(v, k):
    """
    Return the value of entry k in v.
    Be sure getitem(v,k) returns 0 if k is not represented in v.f
    >>> v = Vec({'a','b','c','d'}, {'a':2,'c':1,'d':3})
    >>> v['d']
    3
    >>> v['b']
    0
    """
    assert k in v.D
    return v.f[k] if k in v.f else 0


def setitem(v, k, val):
    """
    Set the element of v with label k to be val.
    setitem(v,k,val) should set the vlue for key k even if k
    is not previously represented in v.f, and even if val is 0.
    >>> v = Vec({'a','b','c'},{'b':0})
    >>> v['b'] = 5
    >>> v['b']
    5
    >>> v['a'] = 1
    >>> v['a']
    1
    >>> v['a'] = 0
    >>> v['a']
    0
    """
    assert k in v.D
    v.f[k] = val

def equal(u,v):
    """
    return true iff u is equal to v.
    Because of sparse representation, it is not enough to compare dictionaries

    >>> Vec({'a','b','c'}, {'a':0}) == Vec({'a','b','c'}, {'b':0})
    True
    >>> Vec({'a','b','c'}, {'a':0}) == Vec({'a','b','c'}, {})
    True
    >>> Vec({'a','b','c'}, {}) == Vec({'a','b','c'}, {'a':0})
    True

    Be sure that equal(u,v) checks equalities for all keys from u.f and v.f even if
    some keys in u.f do not exist in v.f (or vice versa)

    >>> Vec({'x','y','z'}, {'y':1, 'x':2}) == Vec({'x','y','z'}, {'y':1, 'x':0})
    False
    >>> Vec({'a','b','c'}, {'a':0, 'c':1}) == Vec({'a','b','c'}, {'a':0, 'c':1,'b':4})
    False
    >>> Vec({'a','b','c'}, {'a':0, 'c':1,'b':4}) == Vec({'a','b','c'}, {'a':0, 'c':1})
    False

    The keys matter:
    >>> Vec({'a','b'}, {'a':1}) == Vec({'a','b'}, {'b':1})
    False

    The values matter:
    >>> Vec({'a','b'}, {'a':1}) == Vec({'a','b'}, {'a':2})
    False
    """
    assert u.D == v.D
    for k in u.D:
        if u[k] != v[k]:
            return False
    return True

def add(u,v):
    """
    Returns the sum of the two vector.

    Do not seek to create more sparsity than exists in the two input vectors.
    Doing so will unnecessarily complicate your code and will hurt performance.

    Make sure to add together values for all keys from u.f and v.f even if some keys in u.f do not
    exist in v.f (or vice versa)

    >>> a = Vec({'a','e','i', 'o', 'u'}, {'a':0, 'e':1,'i':2})
    >>> b = Vec({'a','e','i', 'o', 'u'}, {'o':4, 'u':17})
    >>> c = Vec({'a','e','i', 'o', 'u'}, {'a':0, 'e':1,'i':2, 'o':4, 'u':17})
    >>> a + b == c
    True
    >>> a == Vec({'a','e','i', 'o', 'u'}, {'a':0, 'e':1,'i':2})
    True
    >>> b == Vec({'a','e','i', 'o', 'u'}, {'o':4, 'u':17})
    True
    >>> d = Vec({'x','y','z'}, {'x':2, 'y':1})
    >>> e = Vec({'x','y','z'}, {'z':4, 'y':-1})
    >>> f = Vec({'x','y','z'}, {'x':2, 'y':0, 'z':4})
    >>> d + e == f
    True
    >>> d == Vec({'x','y','z'}, {'x':2, 'y':1})
    True
    >>> e == Vec({'x','y','z'}, {'z':4, 'y':-1})
    True
    >>> b + Vec({'x','y','z'}, {}) == b
    True
    """
    assert u.D == v.D
    a = Vec(u.D, {})
    for k in u.D:
        if k in u.f or k in v.f:
            a[k] = u[k] + v[k]
    return a

def dot(u,v):
    """
    Returns the dot product of the two vectors.

    >>> u1 = Vec({'a','b','c'}, {'a':1, 'b':2})
    >>> u2 = Vec({'a','b','c'}, {'a':2, 'b':1})
    >>> u1*u2
    4
    >>> u1 == Vec({'a','b','c'}, {'a':1, 'b':2})
    True
    >>> u2 == Vec({'a','b','c'}, {'a':2, 'b':1})
    True
    >>> v1 = Vec({'p','q','r', 's'}, {'p':2, 's':3, 'q':-1,'r':0})
    >>> v2 = Vec({'p','q','r', 's'}, {'p':-2, 'r':5})
    >>> v1*v2
    -4
    >>> w1 = Vec({'a','b','c'}, {'a':2, 'b':3, 'c':4})
    >>> w2 = Vec({'a','b','c'}, {'a':12, 'b':8,'c':6})
    >>> w1*w2
    72
    """
    assert u.D == v.D
    return sum(v[k]*u[k] for k in u.D)

def scalar_mul(v, alpha):
    """
    Returns the scalar-vector product alpha times v.

    >>>zero = Vec({'x','y','z','w'}, {})
    >>>u = Vec({'x','y','z','w'}, {'x':1,'y':2,'z':3,'w':4})
    >>> 0*u == zero
    True
    >>>1*u == u
    True
    >>> 0.5*u == Vec({'x','y','z','w'}, {'x':0.5,'y':1,'z':1.5,'w':2})
    True
    >>> u == Vec({'x','y','z','w'}, {'x':1,'y':2,'z':3,'w':4})
    True
    """
    return Vec(v.D, {k:v[k]*alpha for k in v.f})

def neg(v):
    """
    Returns the negation of a nector.
    >>> u = Vec({1,3,5,7},{1:1, 3:2, 5:3, 7:4})
    >>> -u
    >>> Vec({1,3,5,7},{1:-1, 3:-2, 5:-3, 7:-4})
    >>> u == Vec({1,3,5,7},{1:1, 3:2, 5:3, 7:4})
    True
    >>> -Vec({'a','b','c'},{'a':1}) == Vec({'a','b','c'},{'a':-1})
    True
    """
    a = Vec(v.D, {})
    for k in v.f:
        a[k] = -v.f[k]
    return a


class Vec:
    def __init__(self, labels, function):
        assert isinstance(labels, set)
        assert isinstance(function, dict)
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __add__ = add
    __eq__ = equal
    __neg__ = neg
    __rmul__ = scalar_mul

    def __mul__(self, other):
        #if other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self, other)
        else:
            return NotImplemented # will cause other.__rmul__(self) to be invoked

    def __truediv__(self, alpha): #scalar division
        return (1/alpha)*self

    def __radd__(self, other):
        "Hack to allow sum() to work with vectors"
        if other == 0:
            return self

    def __sub__(self,other):
        "Returns a vector which is the difference of self and other"
        return self+(-other)

    def is_almost_zero(self):
        s = 0
        for x in self.f.values():
            if isinstance(x,int) or isinstance(x,float):
                s += x*x
            elif isinstance(x,complex):
                y = abs(x)
                s+= y*y
            else: return False
        return s < 1e-20

    def __str__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def __hash__(self):
        "Here we pretend Vecs are immutable so we can form sets of them"
        h = hash(frozenset(self.D))
        for k,v in sorted(self.f.items(), key = lambda x:repr(x[0])):
            if v != 0:
                h = hash(h, hash(v))
        return h

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.D, self.f.copy())

    def __iter__(self):
        raise TypeError('%r object is not iterable' % self.__class__.__name__)