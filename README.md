# experiment-reproduction-faster-k-means

## Factors to experiment with (add your own here)
* python version
* numpy versions
* different OS
* different seeds
* memory constraints
* single-threaded (if applicaple)


## Running issues
- python version not mentioned - 2 required
- datasets not formatted easily - we modified the dataset
	- birch space removal


## TODO:
- check whether dataset dimensions match the paper
	- birch - MATCHES (100000 * 2)
	- covtype
	- mnist768 - MATCHES (60000 * 784)
	- synthetic - MATCHES (100000 * 100)
