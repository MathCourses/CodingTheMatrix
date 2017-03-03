def list_dot(u, v):
	s = [u[k]*v[k] for k in range(len(u))]
	return sum(s)