import unittest
from center import Center

class center_tests(unittest.TestCase):

    def setUp(self) -> None:
        self.center_object = Center()
    
    def test_instance(self):
        self.assertIsInstance(self.center_object, Center, "Failed to create an object of the class Center.")
    
    def test_training_hub_trainees_below_or_equal_to_100(self):
        for training_hub in self.center_object.center_dictionary["training_hubs"]:
            self.assertLessEqual(training_hub["num_trainees"], 100, "There were more than 100 trainees found in a training hub")

    def test_bootcamps_trainees_below_or_equal_to_500(self):
        for bootcamp in self.center_object.center_dictionary["bootcamps"]:
            self.assertLessEqual(bootcamp["num_trainees"], 500, "There were more than 500 trainees found in a bootcamp")

    def test_tech_center_trainees_below_or_equal_to_200(self):
        for tech_center in self.center_object.center_dictionary["tech_center"]:
            self.assertLessEqual(tech_center["num_trainees"], 200, "There were more than 200 trainees found in a tech center")

    def test_training_hub_below_25(self):
        for training_hub in self.center_object.center_dictionary["training_hubs"]:
            if training_hub["open"] == "yes":
                self.assertGreaterEqual(training_hub["num_trainees"], 25, "Fewer than 25 trainees found in a training hub.")

    def tech_center_below_25(self):
        for tech_center in self.center_object.center_dictionary["tech_center"]:
            if tech_center["open"] == "yes":
                self.assertGreaterEqual(tech_center["num_trainees"], 25, "Fewer than 25 trainees found in a tech hub.")

    def test_max_training_hubs(self):
        count = 0
        training_hub = self.center_object.center_dictionary["training_hubs"]
        for dictionary in training_hub:
            if dictionary["open"] == "yes":
                count += 1
        self.assertLessEqual(count, 3, "There are more than three training hubs that are open.")

    def test_max_bootcamps(self):
        count = 0
        bootcamp = self.center_object.center_dictionary["bootcamps"]
        for dictionary in bootcamp:
            if dictionary["open"] == "yes":
                count += 1
        self.assertLessEqual(count, 2, "There are more than two bootcamps that are open.")

    def test_tech_center_course(self):
        tech_center = self.center_object.center_dictionary["tech_center"]
        for course in tech_center["course"]:
            if course != "devops" or course != "C#" or course != "java" or course != "data" or course != "business":
                self.assertEqual(1, 2, "Invalid course name found found in tech center")
    
    def test_type_output(self):
        self.assertIsInstance(self.center_object.num_of_open_centers, int, "Output for open centers is not an integer")
        self.assertIsInstance(self.center_object.num_of_closed_centers, int, "Output for closed centers is not an integer")
        self.assertIsInstance(self.center_object.num_of_full_centers, int, "Output for full centers is not an integer")

    

    


    
