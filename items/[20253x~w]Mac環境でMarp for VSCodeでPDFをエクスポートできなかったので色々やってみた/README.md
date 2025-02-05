## VSCodeでの操作・設定
https://qiita.com/firesign2023/items/bc20bc751cf43b66eb4c

これだけでは足りない！というのが本旨です。

:::note warn
たぶんおま環です
Mac環境でbrewを使っています
また、執筆時点で発生したものです
:::

# 結論：google-chrome.appは入っているか？
普段使いしてないから入れすらしてなかったんですが、原因はこれでした。
細かい

# やったこと
最終的に端末を変えて↑を実行して動いた、という状態でした。
問題が発生した端末は一回クリーンインストールした方がいいんじゃ？と思うぐらい年季の入った端末だったので、あまり参考にならないかもしれません。

## VSCodeに拡張機能を入れよう
https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode

VSCodeに、と書いておきながらですが実際に使ったのはVSCodeっぽい別のエディタです。

## marp-cliを入れよう
``` .zsh
brew install marp-cli
```

で、 `Error: /usr/local/Cellar/imagemagick/7.1.1-29_1 is not a directory` と怒られたので、imagemagickを入れてみる

``` .zsh
brew install imagemagick
```

brew古いんでは？問題。

```
brew update
brew upgrade
```

とんでもない時間がかかってしまった、やっぱりか〜。
気を取り直して続行

``` .zsh
brew install marp-cli
```

通った！

## PDFを作ろう
:::note alert
問題は解消せず…
:::

実行結果はsuccessとあるものの、PDFビューアーが開かれることもファイルが生成されることもなく。
念の為デスクトップに生成するようにパスを変えたので権限問題ではないはず、少なくとも別端末では生成されている。

dockerなりできれいな環境を作って生成させるぐらいまでやらないと原因調査もままならなさそう。
業務用途（ではあるけど、深刻度が高いわけ）じゃないし、頑張るより諦めようという結論になりました。
原因調査を頑張るより、Dockerなりで環境を分けるとか、クリーンインストールの手順を確立させた方がいいかも？
