cd data
../svm/svm_rank_learn -c 3 train.txt parameter.dat
echo ""
echo "[INFO] End of Training"
echo ""
../svm/svm_rank_classify train.txt parameter.dat prediction.dat