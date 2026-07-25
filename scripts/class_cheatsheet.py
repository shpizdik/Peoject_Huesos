#class cheat-sheet for me
class Dog:
	def __init__(self, name, age): #constructor
		self.name = name
		self.age = age

	def woof(self): #method
		return f"{self.name} says woof"

#object creation and usage
dog1 = Dog("sharikov", 3)
print(dog1.name, "\t", dog1.woof())
