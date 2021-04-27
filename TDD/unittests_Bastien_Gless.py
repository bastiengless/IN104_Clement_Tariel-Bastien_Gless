import unittest

import sys
sys.path.insert(1,'../OOP/')

from classesTD2 import Mammifere, Rongeur, Cetace

class TestMammifere(unittest.TestCase):
	def testAgePositif(self):
		chien = Mammifere(-2, 0.55, 12)
		self.assertTrue(chien.age >= 0)

class TestRongeur(unittest.TestCase):
	def testPertePoids(self):
		souris = Rongeur(0.5, 0.1, 0.5, 0.01, 6)
		previous_weight = souris.poids
		souris.courir()
		self.assertTrue(souris.poids <= previous_weight)

	def testPoidsPositif(self):
		souris = Rongeur(0.5, 0.1, 0.5, 0.01, 6)
		souris.courir()
		self.assertTrue(souris.poids >=0)


class TestCetace(unittest.TestCase):
	def testProfondeurConstancy(self):
		baleine = Cetace(16, 6, 11, 72, 122)
		previous_profondeur = baleine.profondeurMaxToleree
		baleine.plonger()
		self.assertEqual(baleine.profondeurMaxToleree,previous_profondeur)


if __name__ == "__main__":
	unittest.main()