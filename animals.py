# Let's create our first class

# `class` is the keyowrd

class Animal(): # create Animal() class
	def __init__(self): # self refers to the current class
		self.alive = True
		self.spine = True
		self.lungs = True

	def move(self):
		return "move left, right and centre"

	def eat(self):
		return "keep eating to stay alive"

	def breathe(self):
		return "keep breathing to stay alive"


if __name__=='__main__':
	# creating an object from our Animal class

	cat = Animal() # this will store all the data from Animal class into the variable cat

	print(cat.eat()) # eat() is now ABSTRACTED
