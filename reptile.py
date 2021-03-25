from animals import Animal

class Reptile(Animal):
	def __init__(self):
		super().__init__() # super is used to call the parent class methods and attributes
		self.cold_blooded = True
		self.tetrapods = None
		self.heart_chambers = [3, 4]

	def hunt(self):
		return "workin' hard to catch the next meal"

	def use_venom(self):
		return "I use it if I have to"

	def seek_heat(self):
		return "Looking for sunshine"

# let's see the amazing benefits of inheritance

if __name__=='__main__':
	reptile_object = Reptile()

	print(reptile_object.hunt())
	print(reptile_object.breathe())