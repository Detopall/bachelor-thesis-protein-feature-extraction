# Fondant Protein Features Pipeline

## Table of Contents

- [Data](#data)
- [Fondant](#fondant)
- [Components](#components)
- [Installation](#installation)
- [Requirements](#requirements)
  - [Env variables](#env-variables)
    - [unikp_component](#unikp_component)
    - [Data files](#data-files)
- [Executing the Pipeline](#executing-the-pipeline)
- [Partition issue with Fondant](#partition-issue-with-fondant)

## Data

The data is downloaded from [this link](https://www.uniprot.org/uniprotkb?query=cyp). You can choose how much data you want to download. This project has used around 2650 protein sequences. This data is then used in the pipeline to generate features for each protein sequence. The only thing needed in this pipeline is the protein sequence.

## Fondant

This project uses [Fondant](https://fondant.ai/en/latest/) to run the pipeline.

Fondant is a framework, created by ML6, that allows you to run your pipeline in a containerized environment. This is useful because it allows you to run your pipeline in a consistent environment, regardless of the operating system you are using.

## Components

This section contains the components that are used in the pipeline. Each component has its own README file that contains information about the component and how to set it up.

- [Biopython](./components/biopython_component/README.md)
- [Generate Protein Sequence Checksum](./components/generate_protein_sequence_checksum_component/README.md)
- [iFeatureOmega](./components/iFeatureOmega_component/README.md)
- [Peptide](./components/peptide_features_component/README.md)
- [UniKP](./components/unikp_component/README.md)

## Installation

To install the pipeline, you need to run the following command to install the requirements file:

```bash
pip install -r requirements.txt
```

Make sure you have Docker installed on your machine. You can download it [here](https://www.docker.com/products/docker-desktop). Check your Docker version and make sure it is at least `24.0.0`.

## Requirements

This section will go over the requirements needed to run the pipeline.

### Env variables

There are some environment variables that need to be set in order to run the pipeline. These are the following:

#### unikp_component

```yaml
HF_API_KEY=""
HF_ENDPOINT_URL=""
```

Place the `.env` file in the component folder where the component is located. Make sure this file is in the same level as the `Dockerfile`, `fondant_component.yaml`, and `requirements.txt` files.

### Data files

The pipeline will mount to the specified folder when executing the pipeline. This is done by using the `--extra-volumes` flag when running the pipeline.

The data folder should contain the following files:

- `protein_smiles.json`
  - see [UniKP Component](./components/unikp_component/README.md) for more information

## Executing the Pipeline

You can execute the following command to run the pipeline in your terminal:

```bash
PS> python pipeline.py
```

## Partition issue with Fondant

If you look at the code in the `pipeline.py` file, you will see that the `iFeatureOmega_component` has an additional parameter that is called `input_partition_rows`. This parameter is used to specify the number of rows that the input file will be partitioned into.

Fondant uses Dask to read the input file. Dask splits each partition into a different Pandas DataFrame. This is useful when you have a large file and you want to process it in parallel. However, with the iFeatureOmega component this for some reason causes an error. The error is related to the fact that the input file is partitioned into multiple files and the iFeatureOmega component is not able to find certain columns. This is a known issue and it is being addressed by the Fondant team.

For now, the workaround is to set the `input_partition_rows` parameter to the amount of rows inside the dataset, which in my case is 5 (test data). This will force Dask to make a partition for each row, which is not ideal, but it is the only way to make it work for now.
