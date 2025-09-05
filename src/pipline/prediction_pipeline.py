import sys
from src.entity.config_entity import VehiclePredictorConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception import MyException
from src.logger import logging
from pandas import DataFrame

'''
Patient ID, Timestamp, Age, Gender, Weight, Height, BMI, Heart Rate, BP Systolic, BP Diastolic, 
SpO2, Respiration Rate, Body Temperature, Blood Glucose, Activity Level, Sleep Pattern
'''

class VehicleData:
    def __init__(self,
                Patient_ID,
                Timestamp,
                Age,
                Gender,
                Weight,
                Height,
                BMI,
                Heart_Rate,
                BP_Systolic,
                BP_Diastolic,
                SpO2,
                Respiration_Rate,
                Body_Temperature,
                Blood_Glucose,
                Activity_Level,
                Sleep_Pattern
                
                ):
        """
        Vehicle Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.Patient_ID=Patient_ID
            self.Timestamp=Timestamp
            self.Age=Age
            self.Gender=Gender
            self.Weight=Weight
            self.Height=Height
            self.BMI=BMI
            self.Heart_Rate=Heart_Rate
            self.BP_Systolic=BP_Systolic
            self.BP_Diastolic=BP_Diastolic
            self.SpO2=SpO2
            self.Respiration_Rate=Respiration_Rate
            self.Body_Temperature=Body_Temperature
            self.Blood_Glucose=Blood_Glucose
            self.Activity_Level=Activity_Level
            self.Sleep_Pattern=Sleep_Pattern

        except Exception as e:
            raise MyException(e, sys) from e

    def get_vehicle_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            vehicle_input_dict = self.get_vehicle_data_as_dict()
            return DataFrame(vehicle_input_dict)
        
        except Exception as e:
            raise MyException(e, sys) from e


    def get_vehicle_data_as_dict(self):
        """
        This function returns a dictionary from VehicleData class input
        """
        logging.info("Entered get_usvisa_data_as_dict method as VehicleData class")

        try:
            input_data = {
                "Patient_ID": [self.Patient_ID],
                "Timestamp": [self.Timestamp],
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Weight": [self.Weight],
                "Height": [self.Height],
                "BMI": [self.BMI],
                "Heart_Rate": [self.VinHeart_Ratetage],
                "BP_Systolic": [self.BP_Systolic],
                "BP_Diastolic": [self.BP_Diastolic],
                "SpO2": [self.SpO2],
                "Respiration_Rate": [self.Respiration_Rate],
                "Body_Temperature": [self.Body_Temperature],
                "Blood_Glucose": [self.Blood_Glucose],
                "Activity_Level": [self.Activity_Level],
                "Sleep_Pattern":[self.Sleep_Pattern]
            }

            logging.info("Created vehicle data dict")
            logging.info("Exited get_vehicle_data_as_dict method as VehicleData class")
            return input_data

        except Exception as e:
            raise MyException(e, sys) from e

class VehicleDataClassifier:
    def __init__(self,prediction_pipeline_config: VehiclePredictorConfig = VehiclePredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise MyException(e, sys)

    def predict(self, dataframe) -> str:
        """
        This is the method of VehicleDataClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of VehicleDataClassifier class")
            model = Proj1Estimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise MyException(e, sys)