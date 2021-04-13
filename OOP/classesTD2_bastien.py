class Insect:
	def __init__(self,size,is_social):
		self.number_of_legs = 6
		self.size = size
		self.is_social = is_social # boolean

class Hymenoptera(Insect):
	# Bees and wasps
	def __init__(self,size,is_social,colony_size,is_deadly):
		self.colony_size = colony_size 
		self.is_deadly = is_deadly
		self.is_social = True
		super().__init__(size, is_social)

	def feedTheQueen(self):
		print("Take my food, queen")

	def sting(self):
		if is_deadly:
			print("One sting and you're dead")
		else:
			print("Just don't mess with me")

class Coleoptera(Insect):
	# All types of beetles
	def __init__(self,size,is_social,horn_size,weight):
		self.horn_size = horn_size
		self.weight = weight
		self.is_social = False
		super().__init__(size, is_social)

	def fightForFemale(self):
		print("With my"+str(self.horn_size)"mm horn, I will defeat all my opponents to get to the female")

	def flyClumsily(self):
		print("I'm too heavy to fly correctly")