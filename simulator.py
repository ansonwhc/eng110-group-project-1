class Simulator:
    def __init__(self):
        self.current_data = data = {
            # type of centers: [#1, #2]
            # type of centers: [{num_of_trainees_in_a_course: int}, ...]
            "training_hub": [
                { # 1_training_hub
                    "num_java_trainees": 0,
                    "num_C#": 0,
                },
                { # 2_training_hub
                    "num_java_trainees": 0,
                    "num_C#": 0,
                }
            ],
            "bootcamp": [
                {  # 1_bootcamp
                    "num_java_trainees": 0,
                    "num_C#": 0,
                },
                {  # 2_bootcamp
                    "num_java_trainees": 0,
                    "num_C#": 0,
                }
            ],
            "tech_centre": [
                {  # java_tech_centre
                    "num_java_trainees": 0,
                },
                {  # DevOps_tech_centre
                    "num_devops_trainees": 0,
                }
            ]
        }

    def calculate_open_centres(self, inp = None) -> int:
        if inp is None:
            inp = self.current_data

        result = 0
        for centre_type in inp.values():
            result += len(centre_type)

        return result
