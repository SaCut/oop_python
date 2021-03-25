from snake import Snake

class Python(Snake):
	def __init__(self):
		super().__init__()
		self.large = True
		self.two_lungs = True

	def climb(self):
		return "up we go!"

	def swallow(self):
		return "can't be bothered to chew"

if __name__=='__main__':
	python_object = Python()

	print(python_object.climb()) # from this class
	print(python_object.smell_with_tongue()) # from Snake()
	print(python_object.seek_heat()) # from Reptile()
	print(python_object.breathe()) # from Animal()