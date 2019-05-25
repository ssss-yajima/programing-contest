echo "コンテストの種類(ABC, AGC, ARC, Other)"
read TYPE
echo "コンテンスト番号"
read NUMBER
echo "問題数"
read QNUM
dir=./AtCoder/$TYPE/$TYPE$NUMBER
mkdir -p $dir
array=("A" "B" "C" "D" "E" "F" "G" "H")
for ((i=0; i<$QNUM; i++)); do
    touch $dir/$TYPE$NUMBER${array[$i]}.py
done
