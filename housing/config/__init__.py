from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
import sys, os
from housing.util.util import read_yaml_file
from housing.constants import *
from housing.exception import CodeException


class Configuration:

    def __init__(self, 
    config_file_path:str = CONFIG_FILE_PATH,
    current_time_stamp:str =CURRENT_TIME_STAMP ) -> None:
        self.config_info = read_yaml_file(file_path = config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) -> DataIngestionConfig(dataset_download_url, tgz_download_dir, raw_data_dir, ingested_train_dir, ingested_test_dir):
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )

            data_ingestion_info = self.config_info.config_info[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )

            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingested_train_dir = os.path.join(
                 data_ingestion_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )

            ingested_test_dir = os.path.join(
                data_ingestion_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]                
            )


            data_ingestion_config = DataIngestionConfig(
                dataset_download_url =  dataset_download_url,
                tgz_download_dir =  tgz_download_dir,
                raw_data_dir = raw_data_dir,
                ingested_train_dir =  ingested_train_dir, 
                ingested_test_dir = ingested_test_dir)

            logging.info(f"Data Ingestion Config : {data_ingestion_config}")
            return data_ingestion_config

        except Exception as e:
            raise CodeException(e, sys) from e

    def get_data_validation_config(self) -> DataValidationConfig(schema_file_path):
         pass

    def get_data_transformation_config(self) -> DataTransformationConfig(add_bedroom_per_room, transformed_train_dir, transformed_test_dir, preprocessed_object_file_path):
        pass

    def get_model_trainer_config(self) -> ModelTrainerConfig(trained_model_file_path, base_accuracy):
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig(model_evaluation_file_path, time_stamp):
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig(export_dir_path):
        pass

    def get_training_pipeline_config(self) -> TrainingPipelineConfig(artifact_dir):
        try:
            pass
        except Exception as e:
            raise CodeException(e, sys) from e
