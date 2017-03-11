class Mat:
    def __init__(self, labels, function):
        assert isinstance(labels, tuple)
        assert isinstance(labels[0], set) and isinstance(labels[1], set)
        assert isinstance(function, dict)
        self.D = labels
        self.f = function

    def __repr__(self):
        "evaluatable representation"
        return "Mat("+set(self.D) + ", " + str(self.f) + ")"

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None: rows = sorted(M.D[0], key=repr)
        if cols == None: cols = sorted(M.D[1], key=repr)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(str(c),colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(str(r), pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4