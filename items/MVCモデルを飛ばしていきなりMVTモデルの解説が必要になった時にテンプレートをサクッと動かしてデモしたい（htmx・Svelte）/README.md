:::note warn
いわゆるやってみた系であり、どちらかを推奨するものでもないし、そのような意図もない
:::

## 対象者
- プログラミングスクールなどを含むプログラミング独学中・レッスン中の方
  - エンジニアリング経験（例えば大学生の研究開発を含む）はない
- 現在のスキル感として「とりあえず動く状態を作ろう」を目標値に設定している方
- あるいは、上記についてよく分からない方

## 発端・課題
- Webフレームワークの動作を解説している際に、テンプレートエンジンとサーバー（コントローラー）からの値の受け渡しについてハマった受講生の疑問を解消する方法がないか調査していた。
- 当該受講生には「困ったらとりあえずAIに聞いてみると何かしら情報が返ってくる。最初から正解は返ってこないが、AIを上司だと思って根気よく現状を伝え、解決アドバイスを引き出せるように質問を考えてみよう」と指導しているため、彼らにも達成可能な方法でかつ手取り早くテンプレートエンジンの強みを理解してもらえる教材を用意したい

## なぜhtmxとSvelte？
大前提としてMVTモデルの解説で、特にTについての説明を行いたいものとする
リクエスト・レスポンスを使っているテイで変数処理や表記ルール・条件が従来のサーバーサイドスクリプトの書き方と違うよね、というのが伝わればゴールとする。

- `.html` １つで完結できる（擬似的なサーバーコントローラー的なスクリプトを書ける）
  - CDNで使える
  - 変数をscriptタグの外で展開できる
- できればifやfor(forEach)も解説したいが、従来説明したい内容に沿わなくなりそうなので要件外
- テンプレートエンジンの説明自体にあまり時間をかけたくないので、（今回の場合、htmxやsvelte自体の）コードが直感的であってほしい

コードが直感的というのはどう表現すればいいんだろう？
開発体験だからDX？

## htmxとは
- 公式



- GitHub



## Svelteとは
- 公式



- GitHub



## hello worldのコード・実行環境で比較
- 実行環境はGitHub Pages
- CDNを使用しているため、実践開発の環境とは異なる
  - なるべく公式の書き方に準拠しているが、できる限りAIに丸投げして解決できればいいな、で書いている

### htmx
1ファイルで完結できる、というかした

https://shimajima-eiji.github.io/Hosting2/htmx/helloworld.html

https://github.com/shimajima-eiji/Hosting2/tree/main/htmx

```
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>htmx Example on GitHub Pages</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body>
    <h1>htmx Example(json)</h1>
    <button hx-get="demo.json" hx-target="#json_preview" hx-trigger="click">
        jsonからメッセージを取得
    </button>
    <div id="json_preview"></div>

    <script>
        document.body.addEventListener('htmx:afterOnLoad', function(event) {
            if (event.detail.elt.id === 'json_preview') {
                var response = JSON.parse(event.detail.xhr.responseText);
                event.detail.elt.innerText = response.message;
            }
        });
    </script>

    <h1>htmx Example(html)</h1>
    <button hx-get="demo.html" hx-target="#html_preview" hx-trigger="click">
        外部htmlを取得
    </button>
    <div id="html_preview"></div>

</body>
</html>
```

分業したい場合は、ファイル（画面）ごとに書くか、ビルドを前提にコードを書き直すべきなのだろう。
「変数が分かる程度のデザイナーならページを作りやすそう」という意味ではSCSS感があるな。



### svelte
:::note alert
結論としてCDNで動かせておらず、svelte単体を評価できない
本稿においてはコピペだけでhelloworldができない（環境構築を含む）＝学習コストが高いという考え方による
:::

#### ちょっとだけ・原因追及
CDNで検証を試みたがうまく動かないらしい？
エラーメッセージを読むと`new Svelte`でnot definedと怒られるので、CDNの読み込み同期の問題か宣言の問題だろう。

https://shimajima-eiji.github.io/Hosting2/svelte/helloworld.html

```
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Svelte CDN Example on GitHub Pages</title>
    <script src="https://unpkg.com/svelte@3/dist/svelte.min.js"></script>
</head>
<body>
    <div id="app"></div>

    <script id="template" type="text/svelte">
        <main>
            <h1>Hello {name}!</h1>
            <input bind:value={name}>
        </main>
    </script>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const data = {
                name: 'world'
            };

            const template = document.getElementById('template').innerHTML;

            if (typeof Svelte !== 'undefined') {
                new Svelte({
                    target: document.getElementById('app'),
                    props: data,
                    template: template
                });
            } else {
                console.error('Svelteが読み込まれていません。');
            }
        });
    </script>
</body>
</html>
```



## 結果考察
CDNで動く・動かないというだけでhtmxを使う事はあってもsvelteを使う事はないだろうな、という結論をつけてしまう。
あくまでも執筆時点というのと、そもそもSvelteはCDNの使用を想定していない（ビルドを前提に作っている）のでhtmxの比較対象としては違うのだが、初学者にとってはそんな事は考慮すらされない。
また、ペルソナへの説明という意味ではこのレベル以上に深掘りすると「ただ難しい話をされただけ」という印象を与えかねないため、まだ足りない＝やりすぎと置く。

シンプルにコードコピペ＋ホストサーバーにファイルを置いただけで動いたのがhtmxなので、テンプレートエンジンの強みを解説する時にはこちらを使う方が安全度が高そうだ。

別解、というとちょっとニュアンスが異なるが、PythonでいえばStreamlitのようなものが使えるか？
これも要検証だが、本稿から外れそうなので対象外としているが、別記事で取り扱うことも検討する。
