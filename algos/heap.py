""" Implement the heap  """

class heap(object)  :
	""" A heap object """
	def __init__(self)  :
		self.length = 0;
		self.heap = []
	def extract_min(self)  :
		""" Extract the min element """
		pass


	def insert(self,e) : 
		""" Insert an element """
		self.heap.append(e)
		self.length +=1 
		self.heapify(self.length-1)

	def delete(self,e) :
		""" Delete a particular element """	
		pass
	def heapify(self,i) : 
		""" Takes an element and makes sure it maintains heap property"""
		e  = self.heap[i]
		par = i//2
		if self.heap[par] > e : 
			self.swap(par,i)
			self.heapify(par)

	def make_heap(self,l) : 
		""" Accepts an iterable and creates a heap """
		self.heap.append(l)
		self.heap.length =  len(l)
		for i in range(self.length//2-1) : 
			he

