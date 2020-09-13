import os
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, quote

N = 300

# 画像のURLを取得する関数
def get_image_url_list(query):
    endpoint = 'https://imagesearch.excite.co.jp/'
    # 画像のURLを入れるリストを準備
    url_list = []
    for page in range(1, int(N / 20) + 1):
        request = '{}?q={}&page={}'.format(
            endpoint, quote(query.encode('utf-8')), page)
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
    print('keyword = \'{}\', N = {}'.format(query, N))
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
            save_path = '{}/{}.jpg'.format(save_dir, save_name + str(num))
            # 写真をダウンロード
            urlretrieve(img_url, save_path)
            success_cnt += 1
            time.sleep(1)

            print('[Download] {} {}/{}'.format(query, id, N))
        except Exception as e:
            error_url_list.append(img_url)
            error_cnt += 1

            print('[Error] {} {}/{} {}'.format(query, id, N, img_url))
        id += 1

    print('[Result] {} success:{}/{}'.format(query,
                                             success_cnt - error_cnt, success_cnt + error_cnt))
    if N != success_cnt + error_cnt:
        print('[Warning] URL Is Insufficient.')
    # ダウンロード失敗した画像のURL
    for error_url in error_url_list:
        print('[Failed URL] {}'.format(error_url))
    print('')


# テキストファイルから検索するクエリ, 保存する画像のファイル名を取得する関数
def get_keywords(path='./data/keywords.txt'):
    with open(path) as f:
        keywords = []
        for line in f:
            keyword = line.strip().split(',')
            keywords.append(keyword)
    return keywords


if __name__ == '__main__':
    if N % 20 != 0:
        N = (int(N / 20) + 1) * 20
        print('[Debug] Convert Number Of image.')
    keywords = get_keywords()
    for keyword in keywords:
        # 画像のURLを取得
        img_url_list = get_image_url_list(keyword[0])
        # 画像をダウンロード
        download_image(img_url_list, keyword[0], keyword[1])