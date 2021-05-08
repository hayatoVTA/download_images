# download_images_script
This program to save images by scraping from excite image search.（エキサイト画像検索からスクレイピングして画像を保存する）

1. [概要](#anchor1)
1. [使い方](#anchor2)
1. [詳細](#anchor3)
1. [English](#anchor4)

※renewal_scrapingブランチの内容が最新です。（Version 0.2 on May 9 2021）<br>
また、新しい方のコードでは利用方法が異なります。ほとんどコマンドラインで操作できるようになっているのでそちらをお勧めしてます。

## 概要<a id="anchor1"></a>

__画像を自動でスクレイピングして保存して任意のフォルダに保存することができるスクリプトです。__

### 対応OS

- macOS Catalina 10.15.7 (確認済み)<br>
(他のOSやバージョンでの確認が取れましたら報告していただけるとサービス改善に役立ちます)

### ディレクトリ構造
```
./
├── download_image.py
├── requirements.txt
└── image/
    └── 保存するディレクトリ名/
```

## 使い方<a id="anchor2"></a>

### 1:仮想環境を作成します（飛ばしてもOK）

```
$ python -m venv env
$ source env/bin/activate
```
### 2:必要なパッケージをインストールします

```
$ pip install -r requirements.txt
```

### 3:実際にスクリプトを実行します

- 検索したい画像の名前とディレクトリ名をクエリに指定します（自動的にimageフォルダの中にフォルダを作成してくれるので事前に作成する必要はないです。）

```
$ python download_image.py -q [検索したい画像名] [保存先ディレクトリ名(なんでもOK)]
```

- デフォルトの保存枚数は40枚ですが、20の倍数で保存枚数を指定することも可能です（検索エンジンの仕様上40〜選択できません、ご了承ください。途中で止めることもできます。）
その場合は、以下のクエリを付け加えます

```
$ python download_image.py -q [検索したい画像名] [保存先ディレクトリ名(なんでもOK)] -c [保存したい枚数(20の倍数)]
```

- ヘルプを見る
```
$ python download_image.py -h
```


## 詳細 <a id="anchor3"></a>

### 画面の見方 (まーちゃんver)

- [Debug] ・・・ スクリプト開始時のメッセージです
- [検索クエリ] ・・・ 検索クエリ名です
- [保存先ディレクトリ] ・・・ 保存先ディレクトリ名です
- [ダウンロード回数] ・・・ 保存する枚数です
- [Download] 任意のクエリ 1/40 ・・・ ダウンロード状況が把握できます
- [Error] ・・・ なんらかの理由でエラーが出た画像を教えてくれます
- [Result] 任意のクエリ success:40/44 ・・・ 結果です
- [Warning] URL Is Insufficient. ・・・ 保存できなかったエラーを教えてくれます
- [Failed URL] url ・・・ 保存できなかった URL を表示します

```
[Debug] Convert Number Of image.
[検索クエリ]：佐藤優樹
[保存先ディレクトリ]：masakisato
[ダウンロード回数]：40
[Download] 佐藤優樹 1/40
[Error] 佐藤優樹 2/40 https://test.jpg
[Download] 佐藤優樹 3/40
[Download] 佐藤優樹 4/40
・・・
〜〜〜〜〜中略〜〜〜〜〜
・・・
[Result] 佐藤優樹 success:40/44
[Warning] URL Is Insufficient.
[Failed URL] https://test.jpg
```
