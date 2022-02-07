（タイトルの比較対象は私の知る範囲です）

いろいろなページを斜め読みしてたんですが、結局よくわからなかったので、forkして設定すれば動くようなものを目指しました。
forkして後述のシークレット変数を設定すれば動くので、試してみてください。

https://github.com/shimajima-eiji/__Githut-Action_demo

ほとんどREADMEに書いてます。

## ソースコード
https://github.com/shimajima-eiji/__Githut-Action_demo/blob/main/.github/workflows/add_dummy.yml

``` /.github/workflows/add_dummy.yml
# 本稿で解説時点のコード
name: small git push  # (任意で変更できる。Github Actionsの一覧で表示される名称)

on: [push]

jobs:
  run-shell-command:
    runs-on: ubuntu-latest
    steps:  # name欄が実行結果を見れるものなので、何でもかんでもワンライナーにすれば良いというわけでもなさそう
      - uses: actions/checkout@v2  # git clone (this)
      - name: git setting
        run: |
          git config --global user.email "${{ secrets.EMAIL }}"  # Settings->Secretsで追加
          git config --global user.name "${{ secrets.USER }}"
      - name: Commit files
        run: |
          TZ=JST-9 date '+%Y/%m/%d %H:%M:%S (%Z)' >dummy  # Github ActionsのタイムゾーンがUTCなので、これをJSTに変更
          git add .
          git commit -m "Update dummy by Github Actions" -a
          git pull
          git push
```

## 実行結果
`/dummy`に実行した時点の日付を出力する。  
試しに、README.mdを適当に変更してpushすればGithub Actionsが動いていることが確認できる。

## 開発アドバイス
とりあえず困ったら`pwd`したり`ls -l`で実行結果を見てみると何をすればいいかとっかかりが見えてくると思います。
コミットログが汚染されるので、開発用の捨てるリポジトリを一つ作ってガチャガチャやると精神的にも良いです。
