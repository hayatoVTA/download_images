# -*- coding: utf-8 -*-
import os
import time
import argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, quote

N = 0

# パーサーを作る
parser = argparse.ArgumentParser(
        prog='test.py', # プログラム名
        usage='【 利用方法 】', # プログラムの利用方法
        description='ご利用いただくにはスペース区切りで次のコマンドを入力してください => python download_image.py -l 保存したい画像の名前 作成するフォルダ名 --count 保存回数 (保存回数は20の倍数のみ選択可能, デフォルト=20)', # 引数のヘルプの前に表示
        #epilog='end', # 引数のヘルプの後で表示
        add_help=True, # -h/–help オプションの追加
        )

# 引数の追加
parser.add_argument('-l','--query', nargs='+')
parser.add_argument('-c', '--count', default=20)

# 画像のURLを取得する関数
def get_image_url_list(query):
    endpoint = 'https://imagesearch.excite.co.jp/'
    # 画像のURLを入れるリストを準備
    url_list = []
    for page in range(1, int(N / 20) + 1):
        request = (f"{endpoint}?q={quote(query.encode('utf-8'))}&page={page}")
        response = urlopen(request)
        resources = response.read()
        html = BeautifulSoup(resources, 'html.parser')
        # 画像のURLを抜き取る
        for a_tag in html.find_all('a'):
            url = a_tag.get('href')
            # 画像のURLのみ入れる
            if (url.find('http://') >= 0 or url.find('https://') >= 0) and url.find('excite.co.jp') == -1:
                url_list.append(url)
    # 画像のURLのリストを返す
    return url_list

# 画像をダウンロードする関数
def download_image(img_url_list, query, save_name):
    # 画像を保存するディレクトリを指定
    save_dir = './image/' + save_name
    # 画像を保存するディレクトリを作成
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    print(f'keyword = \'{query}\', N = {N}')
    id = 1
    # ダウンロード成功した回数
    success_cnt = 0
    # ダウンロード失敗した回数
    error_cnt = 0
    # ダウンロード失敗した画像のURLを入れるリストを準備
    error_url_list = []
    for img_url in img_url_list:
        try:
            num = '{0:04d}'.format(id)
            save_path = (f'{save_dir}/{save_name + str(num)}.jpg')
            # 写真をダウンロード
            urlretrieve(img_url, save_path)
            success_cnt += 1
            time.sleep(1)

            print(f'[Download] {query} {id}/{N}')
        except Exception as e:
            error_url_list.append(img_url)
            error_cnt += 1

            print(f'[Error] {query} {id}/{N} {img_url}')
        id += 1

    print(f'[Result] {query} success:{success_cnt - error_cnt}/{success_cnt + error_cnt}')
    if N != success_cnt + error_cnt:
        print('[Warning] URL Is Insufficient.')
    # ダウンロード失敗した画像のURL
    for error_url in error_url_list:
        print(f'[Failed URL] {error_url}')
    print('')

# 引数を解析し、0枚ではないときに実行可能
# 入力コードが間違っている際は説明がでます
for _, value in parser.parse_args()._get_kwargs():
    if _ == 'count':
        N += int(value)
    else:
        if value is not None:
            keyword = value

            if N != 0:
                N = (int(N / 20) + 1) * 20
                print('[Debug] Convert Number Of image.')
                print(f'[検索クエリ]：{keyword[0]}')
                print(f'[保存先ディレクトリ]：{keyword[1]}')
                # 画像のURLを取得
                img_url_list = get_image_url_list(keyword[0])
                # 画像をダウンロード
                download_image(img_url_list, keyword[0], keyword[1])
        else:
            print('使い方はヘルプを参照してください(python download_image.py -hで実行するとhelpを参照できます)')
