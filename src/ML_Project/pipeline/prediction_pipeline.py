import joblib
from pathlib import Path




class PredictionPipeline:
    def __init__(self) -> None:
        self.model = joblib.load(filename= Path('artifacts\model_trainer\model.joblib'))

    def predict(self,data):
        prediction = self.model.predict(data)

        return prediction