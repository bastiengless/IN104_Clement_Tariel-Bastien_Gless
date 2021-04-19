import unittest

class TestInsect(unittest.TestCase):
	def testNbOfLegs(self):
		insect = Insect(3,True)
		self.assertEqual(insect.number_of_legs, 6)
		#insects have 6 legs

class TestHymenoptera(unittest.TestCase):
	def testSociabilityConstancy(self):
		hymenoptera = Hymenoptera(3,True,110,False)
		was_social = hymenoptera.is_social
		hymenoptera.feedTheQueen()
		self.assertEqual(hymenoptera.is_social,was_social)

class TestColeoptera(unittest.TestCase):
	def testLoseOfWheigtAfterFlying(self):
		#coleoptera burn calories 
		weight =30
		coleoptera = Coleoptera(4,False,1,weight)
		coleoptera.flyClumily()
		self.assertTrue(coleoptera.weight<=weight)

	def testSociabilityConstancy(self):
                coleoptera = Coleoptera(4,False,1,30)
                was_social = coleoptera.is_social
                coleoptera.fightForFemale()
                self.assertEqual(coleoptera.is_social,was_social)
                

if __name__ == '__main__':
    unittest.main()
