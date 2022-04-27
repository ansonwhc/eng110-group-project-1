import unittest
import random
from trainee import Trainee


class TestCentre(unittest.TestCase):

    def setUp(self) -> None:
        self.trainee = Trainee()
        self.new_trainees = self.trainee.generate_new_trainees()

    # test to make sure number generated is between 50 and 100
    def test_random_between_50_100(self):
        self.assertGreaterEqual(sum(self.new_trainees.values()), 50, "This number is less than 50 trainees generated.")
        self.assertLessEqual(sum(self.new_trainees.values()), 100, "This number is more than 100 trainees generated.")

    # test to make sure there are 5 courses (5 separate key value pairs)
    def test_5_key_value_pairs(self):
        self.assertEqual(len(self.new_trainees), 5, "There's an incorrect number of courses")







