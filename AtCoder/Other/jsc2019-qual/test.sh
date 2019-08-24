task=$1
for file in `\find ./Samples/$task -maxdepth 1 -type f | sort`; do
    echo "<入力:$file>"
    cat $file
    echo "\n<出力>"
    python $task.py < $file
    echo "-----------------------"
done