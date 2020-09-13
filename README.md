# download_images

### 画像を自動でスクレイピングして保存してくれるやつ

※branchをmasterからrenewal_scrapingに切り替えてgit cloneしてください。変更内容があります。
また、新しい方のコードでは利用方法が異なります。ほとんどコマンドラインで操作できるようになっているのでそちらをお勧めしてます。

ディレクトリ構造
```
./
├── data
|  └── keywords.txt
├── image
└── download_image.py
```

### 使い方

##### 1:保存したい画像名と、フォルダ名をkeywords.txtに記述します

例)りんごという画像をappleフォルダに格納したいとき 
```
りんご,apple
```

自動的にimageフォルダの中にappleフォルダを作成してくれるので事前にappleフォルダは作成する必要はないです。

##### 2:保存したい枚数を指定します

download_image.pyの中の変数'N'に好きな枚数を指定してください。

##### 3:実行します

ターミナルまたはコマンドプロンプトetc...で実行します。
logが表示されながらjpg画像が次々と保存できます。
