echo "コンテストの種類(ABC, AGC, ARC, Other)"
read TYPE
echo "コンテンスト番号/コンテスト名"
read NUMBER
echo "問題数"
read QNUM
dir=./AtCoder/$TYPE/$NUMBER
mkdir -p $dir
array=("A" "B" "C" "D" "E" "F" "G" "H")
for ((i=0; i<$QNUM; i++)); do
    touch $dir/${array[$i]}.py
done
echo $dir
cwd $dir