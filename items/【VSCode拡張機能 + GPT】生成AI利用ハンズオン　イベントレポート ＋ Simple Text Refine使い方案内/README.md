## イベントページ
https://linuc.community/

コミュニティに参加してSlackでイベントページの案内をゲット！

## やり方
1. VSCode開く
1. [simple-text-refine（拡張機能）](https://marketplace.visualstudio.com/items?itemName=yasuraok.simple-text-refine)をいれる
1. OpenAIキーを入れる（Lionコミュニティの好意でテストアカウントをお借りしてます）
    1. 以下（画像１）を参照（やばい情報なのでAPI Key部分は手動で消してます）
1. VSCodeのエクスプローラーでどこかのフォルダを開いておく（そうしないと次の作業で「workspace is not selected」とエラーになってしまう）
1. `simple text refine open prompt file`を選択。実行するとその場で.promptファイルが作られる
    1. 以下（画像２）を参照
1. プロンプトに従い、元となる情報を書く
    1. 本稿では後述の「指示.md」をベースに記事を書かせることにする
    1. なお、先ほどの.promptに後述のプロンプトを追記している
1. **翻訳したい範囲を選択して** からsimple text refine: call LLM with selected Text
    1. 以下（画像３）を参照
1. 生成元と生成後の内容でdiff取れる。Gitのコンフリクトを直しているような感覚で作業ができる
    1. 以下（画像４）を参照

画像１
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/d9ea6d0b-0b2c-14ae-89a5-9aff70bb982e.png)

画像２
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/19105150-28e2-f580-dd1d-7a5397c65441.png)

画像３
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/252da3ac-73b4-58ca-393e-1cee6fd53d96.png)

画像４
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/d3e1e24c-23f7-49f5-4de5-c0cf75e5289a.png)


## 「simple text refine open prompt file」を実行すると生成されるファイル
```.prompt
- label: 添削
  description: |
    作成中の技術文書を添削し修正案を返してください。
    文中で<<と>>で囲まれた部分はあなたへの指示であり、またXXXと書かれた部分はあなたに埋めて欲しい箇所です。
    メモ書きのようになっている箇所に対しては、自然な文章になるように補正してください。
    その際、箇条書きを地の文に変更したり、適当な見出しを追加するなどの形式変更もしてかまいません。
- label: メール
  description: |
    メールやチャットの投稿下書きを書いているユーザーから作成中の文章が与えられるので、添削し修正案を返してください。
    書き始めで文章が不足していたり不連続と思われる場合はそれを補完し、ほぼ完成している場合は文体の改善などをメインに修正してください。
```

ここにプロンプトを書いていくイメージ。
中身は見ての通り、ただのyamlファイル。

## VSCodeマーケット
```
Name: simple-text-refine
Id: yasuraok.simple-text-refine
Description: 
Version: 0.0.6
Publisher: yasuraok
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=yasuraok.simple-text-refine
```

## やってみた 

### 内容
我ながらマジかよ、と思う内容で記事を書かせてみます。

``` 指示.md
以下のソースコードを説明してください

function add(a,b) {
  return a + b;
}

```

### プロンプト
```
- label: ブログ執筆
  description: |
    ユーザーが頑張って作ったプログラムの背景や工夫点などをテックブログで紹介しようと思っています。
    以下の方針に基づいてブログ記事の原稿のMarkdownを返してください。
    - ユーザーの入力がREADMEやソースそのものと思われる場合は、その内容を加味してテックブログ記事を生成する
    - 既にある程度テックブログの体裁になっているものは、改善や誤字脱字の修正を行う
      <<と>>で囲まれた部分はユーザーからの指示です。指示を踏まえて改善してください。
```

を追加し、このプロンプトを適用します。

### GPT4.md
``` GPT4.md
# シンプルなJavaScript関数の魅力: `add`関数の紹介

プログラミングの世界において、基本的な知識はしっかりと確実なソフトウェア開発に不可欠です。今回は、JavaScriptでのプログラミングを始めたばかりの方や、基本に立ち返りたい経験者に向けて、最も基本的な関数の一つである加算関数 `add` を紹介します。

## `add` 関数とは?

`add` 関数は、その名の通り、2つの数値を引数に取り、それらを足し合わせた結果を返します。ここでは、この関数の構造を簡単に解説し、どのようにして数値の加算が行われるのかを説明します。

### 関数の定義

以下が `add` 関数のソースコードです。

¥```javascript
function add(a, b) {
  return a + b;
}
¥```

### パラメータと戻り値

この関数定義にはいくつかの重要な部分があります。まず、関数名 `add` は、この関数の目的—数値の加算—を端的に表しています。続いて、この関数は2つのパラメータ `a` と `b` を取ります。これらは加算される2つの数値です。

重要なのは、`return` ステートメントです。この行では、パラメータ `a` と `b` を `+` 演算子で加算し、その結果を関数の呼び出し元に返しています。

### 使い方

`add` 関数の使用は非常にシンプルです。2つの数値を引数として渡し、関数を呼び出すだけです。以下はその例です。

¥```javascript
let result = add(5, 7);
console.log(result);  // 出力: 12
¥```

この例では、5と7という2つの数値を`add`関数に渡しています。関数はこれらの値を加算し、その結果12を返します。

## まとめ

`add`関数はJavaScriptプログラミングにおける基本ですが、そのシンプルさと効率性から、どんな規模のプロジェクトにおいても便利なツールとなることでしょう。この関数の背後にあるプリンシプルを理解することは、より複雑な関数を作成するための基礎となります。

最後に、プログラミングは練習あるのみです。実際に手を動かして、さまざまな関数を自身で作成し、その動作をテストしてみることをお勧めします。
```

### Claude3(opus)
``` Claude3(opus).md
こちらのソースコードをテックブログ記事風に紹介してみました。

# シンプルに数値を足し算する関数を作ってみた

こんにちは。今回は、JavaScriptで2つの数値を受け取って、その合計値を返す関数 `add` を作ってみました。
ソースコードはこちら。

¥```javascript
function add(a, b) {
  return a + b;
}
¥```

とてもシンプルな関数ですが、2つの引数 `a` と `b` を取り、それらを加算した結果を `return` で返しています。
例えば以下のように使うことができます。

¥```javascript
const result1 = add(1, 2);
console.log(result1); // 3

const result2 = add(10, 5); 
console.log(result2); // 15
¥```

引数に渡した2つの数値を足し合わせた結果が返ってくるというわけです。

数値の加算というごく基本的な処理ですが、関数化しておくことで再利用しやすくなり、コードの見通しも良くなります。
このように、よく使う処理は積極的に関数にまとめていくのが良いでしょう。

JavaScript初心者の方にとっては、とてもわかりやすいコードだと思います。
本記事が、関数の書き方の理解に少しでも役立てば幸いです。

<<もう少し具体的な使用例を1つ入れて、関数化することのメリットをより伝えるようにしてください。>>
```

### おまけ
自分でも書いてみました

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/1115ce53-b5e9-2d7f-c0ae-4a56af32780f.png)

と、↑の記事を読ませてタイトルを考えてもらいました

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/0ae5de63-6e2f-1828-b9fb-70460008bc74.png)

```
1. **VSCodeでプログラム添削を効率化！生成されるMarkdownファイルで編集作業がラクラク**
2. **JavaScriptの基本を理解する：`add`関数の使い方とメリットをテックブログで解説**
3. **プログラミング初心者必見！シンプルなJavaScript関数の世界を楽しもう**
```

らしいです。
参考にはしましたが、採用はしませんでした（目的が違うのと、プロンプトが雑すぎた）
