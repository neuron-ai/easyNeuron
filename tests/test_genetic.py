import unittest

from easyneuron._testutils import log_errors
from easyneuron.exceptions import DimensionsError
from easyneuron.genetic.genomes import Genome, child_of
from numpy.random import randint


class TestGenome(unittest.TestCase):
	@log_errors
	def test_mutate(self):
		TESTS = 10

		noChanges = 0
		for i in [
			[randint(-10, 10) for _ in range(10)]
			for _ in range(TESTS)
		]:
			test = Genome(i)

			old_genome = test.genome.copy()

			new_genome = test.mutate(0.1, magnitude=5)

			self.assertTrue(old_genome.shape == new_genome.shape)
			self.assertFalse(old_genome is new_genome, msg="there is an issue with the tests.")

			if (old_genome == new_genome).all(): noChanges += 1

		self.assertLessEqual(noChanges, TESTS * 0.6)

	@log_errors
	def test_child(self):
		test = child_of(
			Genome([1, 2, 3]),
			Genome([1.1, 4, 2.8])
		)

		self.assertIsInstance(test, Genome)
		self.assertRaises(DimensionsError, child_of, Genome([1, 2, 3]), Genome([1, 2]))
