from reptile import Reptile

class Snake(Reptile):
	def __init__(self):
		super().__init__()
		self.limbs = False
		self.venom = True
		self.forked_tongue = True

	def shed_skin(self):
		return "growing out"

	def smell_with_tongue(self):
		return "I use my tongue to smell food"

if __name__=='__main__':
	snake_object = Snake()

	print(snake_object.eat()) # inherited from Animal()
	print(snake_object.move()) # inherited from Animal()
	print(snake_object.hunt()) # inherited from Reptile()
	print(snake_object.smell_with_tongue()) # from current class