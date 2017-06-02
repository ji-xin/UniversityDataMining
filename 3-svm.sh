# https://www.cs.cornell.edu/people/tj/svm_light/svm_rank.html

cd data
../svm/svm_rank_learn -c 3 2-train.txt 3-parameter.dat

echo ""
echo "[INFO] End of Training"
echo ""


../svm/svm_rank_classify 2-train.txt 3-parameter.dat 3-prediction_train.dat
echo ""
../svm/svm_rank_classify 2-test.txt 3-parameter.dat 3-prediction_test.dat