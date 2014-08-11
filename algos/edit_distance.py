def edit_distance(s1,s2) :
	
	def memoize(func) : 
		cache = {}
		def memoized_func(*args):
			if tuple(args) not in cache : 
				cache[tuple(args)] = func(*args)
			else : 
				print("Used cache")
			return cache[tuple(args)]
		return memoized_func

	@memoize
	def edit_sub(i,j):
		if i < 0  or j < 0 : 
			return max(i+1,j+1) 
		else :
			subst = edit_sub(i-1,j-1) + int(s1[i]!=s2[j])
			add = edit_sub(i,j-1) + 1
			delete = edit_sub(i-1,j) + 1
			return min(subst, min(delete, add))
	
	return edit_sub(len(s1)-1, len(s2)-1)


if __name__ == '__main__' : 
	print edit_distance("ab", "dcb")
