from src.kidneyDiseaseClassifier import logger
from src.kidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "01 - Stage => Data Ingestion"
try:
    logger.info(f">>>>>> 01 - Stage {STAGE_NAME} started. <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> 01 - Stage {STAGE_NAME} completed. <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e