""" This program demonstrates the use keyword dict for params """

class Shape(object) : 
	def __init__(self,shapename,**kwds) : 
		self.shapename = shapename
		print kwds
		super(Shape,self).__init__(**kwds)

class ColoredShape(Shape) : 
	def __init__(self,color,**kwds) :
		self.color = color
		print kwds
		super(ColoredShape,self).__init__(**kwds)

cs = ColoredShape(color='red',shapename='square')

