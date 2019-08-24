import sys
import requests
from bs4 import BeautifulSoup
import os
import shutil

#指定したURLから入力例を取得して文字列のリストとして返す
def get_sample_inputlist(url):
    html = requests.get(url)
    soap = BeautifulSoup(html.text, "html.parser")
    sections = soap.findAll('section')

    samples = []
    for s in sections:
        h3 = s.find('h3').string
        if "入力例" in h3:
            sample = s.find('pre').string[:-1]
            samples.append(sample)
    return samples


# コンテストの問題数を返す
def get_task_num(url):
    html = requests.get(url)
    soap = BeautifulSoup(html.text, "html.parser")
    return len(soap.findAll('tr')) -1 # 問題ページのテーブル行数 - 1


#URLからコンテストの区分と名前を取得して返す
def parse_contest_type(url):
    # URLからコンテスト名を取得
    tokens = url.split('/')
    name = tokens[4]
    number = 0

    #ABC, AGC, ARC, Otherに分類
    tmp = name[0:3].upper()
    if tmp in ['ABC', 'AGC', 'ARC']:
        category = tmp
        number = name[-3:]
        # name = number
    else:
        category = "Other"

    return category, name, number


# コンテストのフォルダ、.py、サンプル入力などを作成する
def make_files(category, name, number, task_num, samples):
    contest_dir = f"./AtCoder/{category}/{name}"
    #フォルダ作成
    os.makedirs(contest_dir, exist_ok=True)
    os.makedirs(f"{contest_dir}/Samples", exist_ok=True)

    #.pyファイル作成
    for i in range(task_num):
        ch = chr(i+97)
        # .puファイルとサンプルフォルダ作成
        with open(f"{contest_dir}/{ch}.py", mode='w'):
            os.makedirs(f"{contest_dir}/Samples/{ch}", exist_ok=True)

        # サンプルtxt作成
        for si, s in enumerate(samples[i]):
            with open(f"{contest_dir}/Samples/{ch}/{str(si)}.txt", mode='w') as f:
                f.write(s)

    #テストスクリプトをコピー
    shutil.copyfile('test.sh' , f'{contest_dir}/test.sh')


# メイン関数
if __name__ == "__main__":
    url = input("トップページURL:")
    if url[-1] == '/':
        url = url[:-1]
        print(url)

    task_num = get_task_num(url + '/tasks')
    category, name, number = parse_contest_type(url)


    samples = []
    for i in range(task_num):
        ch = chr(i + 97)
        tmp_name = name.replace('-','_')
        task_url = f'{url}/tasks/{tmp_name}_{ch}'
        samples.append(get_sample_inputlist(task_url))
    
    make_files(category, name, number, task_num, samples)

    print()
    print(f'Category:{category} Name:{name} Number:{number}')
    print(f'Num of tasks:{task_num}')
    print(('<<< Ready!! >>>'))

    # for s in samples:
    #     print(s)