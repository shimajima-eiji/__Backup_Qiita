
## 発端
QiitaCLIをガチャガチャいじっていて気がついたが、publishで更新する処理はCIでいうところの

```
- uses: increments/qiita-cli/actions/publish@v1
  with:
    qiita-token: ${{ secrets.QIITA_TOKEN }}
    root: "."
```

が実行しているからでは？という疑問。
単純にローカルから`npx qiita push`だとどうか？
→`npx qiita push --all`としないと新しいファイルが追加されなかったので修正。

## 検証結果
更新された！本ファイルで確認。

```
---
title: QiitaCLIで作成したファイル（ローカル）はpublish時にIDを更新してくれるのか？
tags:
  - QiitaCLI
private: false
updated_at: ''
id: 
organization_url_name: null
slide: false
ignorePublish: false
---
```

が

```
---
title: QiitaCLIで作成したファイル（ローカル）はpublish時にIDを更新してくれるのか？
tags:
  - QiitaCLI
private: false
updated_at: '2024-06-13T14:15:04+09:00'
id: 384f130aba7ea537937b
organization_url_name: null
slide: false
ignorePublish: false
---
```

になった。変更差分だけ取り出すと、

| 行数 | 変更前 | 変更後 |
| --- | --- | --- |
| 6 | updated_at: '' | updated_at: '2024-06-13T14:15:04+09:00' | 
| 7 | id:  | id: 384f130aba7ea537937b |

であるので、qiita pushによって元ファイルへの更新も同時に行なっていることがわかった。
慣れてくると勘違いしがちだが、qiita pushはあくまでqiitaへのアップロードなのでgit pushはまた別に行う必要がある。

ただし、CIを実行すると

```
- uses: increments/qiita-cli/actions/publish@v1
  with:
    qiita-token: ${{ secrets.QIITA_TOKEN }}
    root: "."
```

のタイミングでgit pushも実施される（コミッターはgithub actions[bot])

## 実はこっそり別の検証も
いったんpublishした状態でpublicフォルダ・ディレクトリから記事ファイルを削除して、もう一度publicに追加し直す、という操作をやってみた。
どうやら記事ID(FrontFormatter)で管理しているらしいので、新しくファイルが追加される、ということはないらしい。
よく考えたらそれはそうで、別の端末またはディレクトリにgit cloneして複数の環境を作ってもqiita pullされない限りは環境差異が生じないことになる

逆に言えば、いったん記事をpublishした環境とは別の場所でqiita pullしてそこからまたpublishをすると、別の場所ではqiita pullしないと最新版にならないよね、という話にもなる。
これはgitと同じ考え方ができるので納得感もある。

QiitaCLIは（Webエディタでの編集による競合を考えなければ）運用可用性はある！
