""" 
Run the dfs algo
"""
V = range(5)

E = {}
for i in range(5) : 
	E[i] = range(i)
	E[i].extend(range(i+1,5))
visited = [False]*len(V)


def dfs(V,E,s) :
	""" runs dfs """
	if visited[s] : 
		print("visited")
	else : 
		visited[s] = True
		print(s)
		for v2 in E[s] :
			dfs(V,E,v2)

if __name__ == '__main__' : 
	dfs(V,E,1)

