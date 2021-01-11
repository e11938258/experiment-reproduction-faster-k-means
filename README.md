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
- not runnable with the latest p2 numpy version (1.16)


## TODO:
- check whether dataset dimensions match the paper
	- birch - MATCHES (100000 * 2)
	- covtype - NOT MATCHING(581012 * 55, paper says 150000 * 55)
	- mnist768 - MATCHES (60000 * 784)
	- synthetic - MATCHES (100000 * 100)
    - cup98lrn - MATCHES (95412 * 481)

- Find MSE for different algorithms & datasets