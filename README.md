## How to run these codes

* `$ mkdir data`
* `$ python 1-0-parse_name.py`
* `$ python 2-preprocess.py`
* `$ ./3-svm.sh`
* `$ python 4-analyse.py`

The SVM code is downloaded from [https://www.cs.cornell.edu/people/tj/svm_light/svm_rank.html](https://www.cs.cornell.edu/people/tj/svm_light/svm_rank.html).

## Results

| The original rank | The predicted score | The predicted rank | University name                          |
| :---------------: | :-----------------: | :----------------: | ---------------------------------------- |
|         5         |     75.80960972     |         2          | Columbia University in the City of New York |
|        55         |     52.77087185     |         50         | University of Washington-Seattle Campus  |
|        115        |     41.46118543     |        118         | University of Oklahoma-Norman Campus     |
|        150        |     37.39428332     |        152         | SUNY at Albany                           |
|        228        |     26.08926273     |        220         | University of Missouri-St Louis          |