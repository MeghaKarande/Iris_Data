
import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config


class IrisData():
    def __init__(self, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_models(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.log_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

        with open(config.BEST_MODEL_PATH, "rb") as f:
            self.dt_clf = pickle.load(f)

    def get_predicted_species(self) :

        self.load_models()

        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLengthCm
        test_array[3] = self.PetalWidthCm

        print("Test Array -->\n",test_array)

        species = self.dt_clf.predict([test_array])[0]

        return species
    

if __name__ == "__main__":
    SepalLengthCm = 5.10
    SepalWidthCm  = 3.05
    PetalLengthCm = 1.40
    PetalWidthCm  = 0.20

    iris = IrisData(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    species = iris.get_predicted_species()
    print("Predicted Species :", species)



