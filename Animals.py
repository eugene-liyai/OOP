class Animals:

	def feathers(self):
		return self.strings['feathers']
	def fur(self):
		return self.strings['fur']
	def hair(self):
		return self.strings['hair']
	def scales(self):
		return self.strings['scales']

class Chicken(Animals):
	strings = dict(
		feathers="The chicken has feathers",
		fur = "The chicken has no fur",
		hair = "The chicken has no hair",
		scales = "The chicken has scales on its feet"
		)

class Dog(Animals):
	strings = dict(
		feathers="The dog has no feathers",
		fur = "The dog has soft fur",
		hair = "The dog has no hair",
		scales = "The dog has no scales"
		)

def on_the_farm(chicken):
	print(chicken.feathers())
	print(chicken.scales())
	print(chicken.fur())
	print(chicken.hair())

def in_the_kenel(dog):
	print(dog.feathers())
	print(dog.scales())
	print(dog.fur())
	print(dog.hair())

def main():
	dingo = Dog()
	hen = Chicken()

	print("**** in the kenel ****")
	for obj in (dingo, hen):
		in_the_kenel(obj)

	print("**** on the farm *****")
	for obj in (dingo, hen):
		on_the_farm(obj)

if __name__ == "__main__":
	main()