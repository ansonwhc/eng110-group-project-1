from Simulator import Simulator
import csv
import re


class Record(Simulator):
    """
    REQUIREMENTS:
    simulate() output has to be (dict, dict)
    simulate() runs when Simulator is initialised
    """
    def __init__(self, duration):
        super().__init__(duration)
        self.record_dict = {"headers": [],
                            "data": []}

    def reset(self, duration):
        # helper method, ugly but MVP for now
        super().__init__(duration)

    def monthly(self, duration):
        pass

    def record(self, duration: str = None):
        # self.reset(duration)
        if self.input is not TypeError:
            if not self.record_dict["headers"]:   # ugly but MVP for now
                self.record_dict["headers"] = [*self.result.keys(),
                                               *self.simulation_info.keys()]

            self.record_dict["data"].append([*self.result.values(),
                                             *self.simulation_info.values()])

    def export(self, file_name="simulation record", extension="csv"):
        if extension == "csv":
            file_name = re.sub("[^a-zA-Z0-9 /:]", "", file_name)   # can we not use re?
            with open(f"{file_name}.{extension}", "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(self.record_dict["headers"])

                for data in self.record_dict["data"]:
                    writer.writerow(data)
        else:
            return NotImplementedError


if __name__ == "__main__":
    inp = "14"
    record_obj = Record(inp)
    record_obj.record(inp)
    inp = "32"
    record_obj.record(inp)
    inp = "24"
    record_obj.record(inp)
    record_obj.export()
