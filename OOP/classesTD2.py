

class Mammifere:
	def __init__(self,age,taille,poids):
		self.age = age # en annees
		self.taille = taille # en m
		self.poids = poids # en kg

class Rongeur(Mammifere):
	def __init__(self,age,taille,poids,longueurDents,vitesse):
		self.longueurDents = longueurDents # en m 
		self.vitesse = vitesse # en m/s
		super().__init__(age,taille,poids)

	def hiberner(self):
		print("C'est parti pour un gros dodo ... Zzzz ...")

	def courir(self):
		print("une vitesse de "+str(self.vitesse)+" ca décoiffe !")

class Cetace(Mammifere):
	def __init__(self,age,taille,poids,tempsApnee,profondeurMaxToleree):
		self.tempsApnee = tempsApnee # en minutes
		self.profondeurMaxToleree = profondeurMaxToleree # en m
		super().__init__(age,taille,poids)

	def plonger(self):
		print("Je peux plonger jusqu'à "+str(self.profondeurMaxToleree)+" metres.")

	def trempette(self):
		print("Trempette! Mais rien ne se passe ...")