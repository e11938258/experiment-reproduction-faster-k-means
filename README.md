# Experiment-reproduction-faster-k-means

This is the code for the paper Reproducibility study - Faster k-means cluster estimation.

## 1 How to run:
### 1.1 Dataset runners:
All of the experiment configurations can be run using the datasets filename:
birch.py
covtype.py
minst.py
cup.py

Python2 is required due to requirements of the code provided by the author of the original paper.
E.g. python2 birch.py

Additional parameters such as the target MSE to converge or the number of replicates can be set in those scripts.
The following variables should be ovewritten:
REPETITION_COUNT = 20
MSE_TO_CONVERGE = 1


The code we are re-using is located in *originalrepo* folder and is a direct clone of the repository with modifications to the stopping criterion of the heuristic triangle inequality sped up K-Means as described in the report. The datasets are also included inside and need to be extracted prior to use. Our files to run the experiment configurations make use of the datasets from the original repository (https://github.com/siddheshk/Faster-Kmeans) as well as the, modified, implementation. Some utilities, such as dataset loading and experimentrunner, are located in the util/ folder. 
We made modifications to the birch dataset adding a space in a single row("770015   1000000" -> "770015    1000000") for easier processing so we provide it unzipped.

When a one of the dataset runners (1.1) are executed the results are written into the results/ folder. We have provided the results of our experiments in this folder as well and stored them in folders which have format <dataset>_<mse_level>_MSE. Example: Birch_3_MSE stands for Birch dataset results (birch.py) and 3% MSE.

The evaluation part is located in notebooks/ folder and contains the evaluation jupyter notebook. This notebook accepts a file from the results folder and calculates the reported results as well as does significance tests. 