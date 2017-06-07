## Program website

https://github.com/Ji-Xin/UniversityDataMining

## How to run these codes

* `$ mkdir data`
* `$ python 1-0-parse_name.py`
* `$ python 2-preprocess.py`
* `$ ./3-svm.sh`
* `$ python 4-analyse.py`

The SVM code is downloaded from [https://www.cs.cornell.edu/people/tj/svm_light/svm_rank.html](https://www.cs.cornell.edu/people/tj/svm_light/svm_rank.html).

## Results

| The original rank | The predicted score | The predicted rank |             University name              |
| :---------------: | :-----------------: | :----------------: | :--------------------------------------: |
|         5         |     76.00011164     |         2          | Columbia University in the City of New York |
|        55         |     53.02081989     |         50         | University of Washington-Seattle Campus  |
|        115        |     41.40878801     |        118         |   University of Oklahoma-Norman Campus   |
|        150        |     37.50624646     |        152         |              SUNY at Albany              |
|        200        |     26.8471974      |        220         | University of Colorado Denver/Anschutz Medical Campus |
|        228        |     26.18748815     |        220         |     University of Missouri-St Louis      |