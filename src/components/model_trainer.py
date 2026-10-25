import sys
import numpy as np
from typing import Tuple

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import load_numpy_array_data, load_object, save_object, read_yaml_file
from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifact_entity import DataTransformationArtifact, ClassificationMetricArtifact, ModelTrainerArtifact
from src.entity.estimator import MyModel
from src.constants import MODEL_SCHEMA_FILE_PATH

class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        """
        :param data_transformation_artifact: Output reference of data transformation artifact stage
        :param model_trainer_config: Configuration for model training
        """
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config
        self._model_schema=read_yaml_file(file_path=MODEL_SCHEMA_FILE_PATH)

    def get_model_object_and_report(self, train:np.array, test:np.array)-> Tuple[object,object]:
        """
        Method Name :   get_model_object_and_report
        Description :   This function trains a RandomForestClassifier with specified parameters
        
        Output      :   Returns metric artifact object and trained model object
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            logging.info("Training Random forest Classifier with specified parameters")

            ## Splitting the train and and test data into fetaures and target variables
            x_train,y_train,x_test,y_test=train[:,:-1], train[:,-1], test[:,:-1], test[:,-1]
            logging.info("Feature and Target Variables separated")

            ## Intialized Randomforest Classifier with specified parameters
            model=RandomForestClassifier(
                n_estimators=self._model_schema["parameters"]["MODEL_TRAINER_N_ESTIMATORS"],
                min_samples_split=self._model_schema["parameters"]["MODEL_TRAINER_MIN_SAMPLES_SPLIT"],
                min_samples_leaf=self._model_schema["parameters"]["MODEL_TRAINER_MIN_SAMPLES_LEAF"],
                max_depth=self._model_schema["parameters"]["MIN_SAMPLES_SPLIT_MAX_DEPTH"],
                criterion=self._model_schema["parameters"]["MIN_SAMPLES_SPLIT_CRITERION"],
                random_state=self._model_schema["parameters"]["MIN_SAMPLES_SPLIT_RANDOM_STATE"]
            )

            ## Fit the model
            logging.info("Model Training going on...")
            model.fit(x_train,y_train)
            logging.info("Model training done.")

            ## Predictions and Evaluation metrics
            y_pred=model.predict(x_test)

            ## Type casting both the values to int
            y_test = y_test.astype(int)
            y_pred = y_pred.astype(int)

            accuracy=accuracy_score(y_test,y_pred)
            precision=precision_score(y_test,y_pred)
            recall=recall_score(y_test,y_pred)
            f1=f1_score(y_test,y_pred)

            ## Creating metric Artifact
            metric_artifact=ClassificationMetricArtifact(f1_score=f1, 
                                                         precision_score=precision, 
                                                         recall_score=recall, 
                                                         accuracy_score=accuracy)
            return model, metric_artifact
        except Exception as e:
            raise MyException(e,sys) from e

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        """
        Method Name :   initiate_model_trainer
        Description :   This function initiates the model training steps
        
        Output      :   Returns model trainer artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            print("----------------------------------------------------------------------------------------------")
            print("Start ModelTrainer component")
            ## Load transformed train and test data
            train_arr=load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_arr=load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)
            logging.info("Train and test data loaded")

            ## Train model and get metrics
            trained_model, metric_artifact=self.get_model_object_and_report(train=train_arr,test=test_arr)
            logging.info("Model Object and Artifact Loaded")

            ## Load preprocessing object
            preprocessing_obj=load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            logging.info("Preprocessing Obj loaded")

            ## Check if the model's accuracy meets the expected threshold
            if accuracy_score(train_arr[:, -1], trained_model.predict(train_arr[:, :-1]))<self.model_trainer_config.expected_accuracy:
                logging.info("No model found with score above the base score")
                raise Exception("No model found with score above the base score")

            ## Save the final model object that includes both preprocessing and the trained model
            logging.info("Saving the new model as performance is better than previous one.")
            mymodel=MyModel(preprocessing_object=preprocessing_obj, trained_model_object=trained_model)
            save_object(self.model_trainer_config.trained_model_file_path,mymodel)
            logging.info("Saved final model object that includes both preprocessing and the trained model")

            ## Create and return the ModelTrainerArtifact
            model_trainer_artifact=ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                metric_artifact=metric_artifact
            )
            logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise MyException(e,sys) from e