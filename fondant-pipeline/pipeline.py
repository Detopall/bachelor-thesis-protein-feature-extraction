import json
import pyarrow as pa
import pandas as pd

from fondant.pipeline import Pipeline
from fondant.pipeline.runner import DockerRunner

DATA_PATH_FONDANT = "/data/mock_data.parquet"
DATA_PATH = "./data/mock_data.parquet"

# create a new pipeline
pipeline = Pipeline(
    name="feature_extraction_pipeline",
    base_path=".fondant",
    description="A pipeline to extract features from protein sequences."
)


class FondantPipelineRun():
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def read_data(self):
        dataset = self.pipeline.read(
            "load_from_parquet",
            arguments={
                "dataset_uri": DATA_PATH_FONDANT,
            },
            produces={
                "sequence": pa.string()
            }
        )
        return dataset

    def create_pipeline(self, dataset):
        _ = dataset.apply(
            "./components/biopython_component"
        ).apply(
            "./components/generate_protein_sequence_checksum_component"
        ).apply(
            "./components/iFeatureOmega_component",
            input_partition_rows=5,
            arguments={
                "descriptors": ["AAC", "CTDC", "CTDT"]
            }
        )
        return dataset

    

    def run_pipeline(self, input_dir):
        runner = DockerRunner()
        runner.run(
            input=self.pipeline,
            extra_volumes=[f"{input_dir}:/data"]
        )


if __name__ == "__main__":
    # Create and run the FondantPipelineRun class
    fondant_pipeline_run = FondantPipelineRun(pipeline)
    # fondant_pipeline_run.create_protein_smiles()
    dataset = fondant_pipeline_run.read_data()
    fondant_pipeline_run.create_pipeline(dataset)
    fondant_pipeline_run.run_pipeline(DATA_PATH_FONDANT)

    # Create and run the DataSaving class
    # TODO
