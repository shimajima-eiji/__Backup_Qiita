## 結論
settings.jsonに

```
    "settingsSync.ignoredSettings": [
        "(除外したいキー)"
    ],
```

を指定するだけ。

### 例（最小構成）
```
    "simple-text-refine.prompt_path" : "(promptファイルのパス)",
    "settingsSync.ignoredSettings": [
        "simple-text-refine.prompt_path"
    ],
```

### 設定画面からみる
当該項目に「(同期されていません)」と表示される

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/98c4104c-cacd-e64d-a153-9708674fa1fd.png)

## 発端
https://marketplace.visualstudio.com/items?itemName=yasuraok.simple-text-refine

を使っていて、WindowsとMacで同じアカウントを活用しており、これを同期（バックアップが目的）しているのだが、当然パスが違うので片方で設定して使用すると、もう片方の端末では使えないという状態になる
どちらも共通の環境で使えるようにWSL+Remote WSL構成にしたり色々やっていたが、VSCodeの環境構築のために色々手を尽くすのはなんだかなぁ、と思ったので、本格的にVSCodeの同期設定の課題解決に乗り出した。

対応した方法が↑の結論の通り。

## Simple Text Refine以外でも使えそうなもの
端末固有のパスを設定するものはほぼ全てが該当しそう
他にも端末固有に限定せず、色々な利用シーンがありそう
今すぐ使わないにしても、とりあえず一つ設定しておくとこのページをいちいちブックマーク・あとで読むなどに登録しなくて済むので、使っていない設定でもとりあえず置いておく、というのがおすすめ。

よく分からない場合は、本稿と同じように設定しておくと良いかも。
拡張機能置いときます
↓↓↓

https://marketplace.visualstudio.com/items?itemName=yasuraok.simple-text-refine
