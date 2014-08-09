

def bfs(invalid, m, n, s, e) : 
	visited, paths = {}, {}
	q = []
	q.append(s) ; paths[s] = "" ; visited[s] = True

	def legal(curr) : 
			i,j = curr
			for action, cand in zip("LRUD",[(i,j-1),(i,j+1),(i+1,j),(i-1,j)]):
				ii,jj = cand
				if 0 <= ii <= m and 0 <= jj <= n and not visited.get(cand, False) and not invalid.get(cand,False) :
 					yield (action, cand)


	while q : 
		curr = q.pop(0)
		print curr, q
 
		if curr == e : 
			return paths[curr]
		for action, nbr in legal(curr) : 
			visited[nbr] = True
			q.append(nbr)
			paths[nbr] = paths[curr] + action	

	return "Not Found"	

if __name__ == '__main__' :
	invalid = {}
	invalid[(2,1)] = True
	invalid[(1,2)] = True
	invalid[(0,3)] = True
	print bfs(invalid, 4, 4, (0,0), (3, 3))
