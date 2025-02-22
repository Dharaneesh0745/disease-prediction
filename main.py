from src.kidneyDiseaseClassifier import logger
from src.kidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.kidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


# STAGE_NAME = "01 - Stage => Data Ingestion"
# try:
#     logger.info(f">>>>>> {STAGE_NAME} started. <<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> {STAGE_NAME} completed. <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "02 - Stage => Prepare Base Model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> {STAGE_NAME} started. <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> {STAGE_NAME} completed. <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e