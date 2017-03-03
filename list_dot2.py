def list_dot2(u, v):
	s = [a*b for a, b in zip(u,v)]
	return sum(s)