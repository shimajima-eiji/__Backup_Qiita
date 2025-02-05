## 最新版
https://github.com/shimajima-eiji/Hosting2/tree/main/chrome%20extensions/chatmemo

## 謝辞
本当はAPIを使って自動でコメントを拾ってくる、という仕組みにしたかったんですが、そもそも環境を提供しているクライアントが自分のアカウントではなかったので物理的にできませんでした…

今回の運用は以下の通り。

1. チャットを投げる
1. メッセージをコピーしてアプリにも貼り付ける
1. アプリを配信する

## ユースケース
- ※チャット欄に書くものは大体参考用のURLか、質問への口頭回答＋解説
- スライドを画面共有する場合は、スライド自体に上書きしたり、ペンツールなどを使って直接書き込む
  - 最近はグラレコ（グラフィックレコーディング）にも挑戦
  - ホワイトボード（機能または物理）も使える

配信に乗らないのは※だけなので、質疑応答部分は（あとで振り返り確認しやすいように）Q&Aスライドを投影する形にすればよく、やはりスライド自体に書く事で解決できる

### なぜChrome拡張なのか？
参考URLを貼り付けている瞬間が圧倒的に多いため

基本的に講義時に共有したいURLなどがあればスライドにも盛り込むが、質問対応時はそうもいかない。
たとえば、質問内容に対して分かりやすい解説があるサイトをその場で案内したい場合や、実際に触ってみてほしいサイトなどを紹介する場合があり、ブラウザを使っている時にチャット欄に転送する使い方をする事が多い。
また、スライドを使っている時もやはり質問対応が発生するとブラウザに切り替えるので、想定している以上にスライドに書けば良くね？という機会は少なかったりする。

## どうやって作ったか？
本題。
使っていたのはcursor + Claude-3.5-sonnet（無料枠。月額50回まで）のみ。

:::note
以下、非エンジニア向けに開発現場のシミュレーションを想定したもの。ただし、講師またはメンターの解説を前提にした内容であるため、一人で読み進めないように。
必要であればAIに解説させること。
:::

### まずは初期バージョン（後述）を作る
結論から言うと、初期バージョン以上の品質での出力ができなかった。

「（自分は）ノーコード」と言うからには、プロンプト側で解決すべき問題と言えばそうだが、いきなり完成図を見据えて実装するエンジニアが何人いるだろうか、というのが気になった。
おそらく、AIも同じだろう。精度が高まったとは言っても、結局のところは設計書が不十分であれば出力も曖昧にならざるを得ない。
たとえば「出力はindex.htmlとstyles.cssとscripts.js。manifest.jsonの4ファイルのみ、外部ファイルはqrcode.jsを使う」まではなんとなく決められても、
これらを組み合わせてどういう形式にしていけばいいかは実装レベルまでの設計書（DBは使わないがクラス設計書など）を書くか、設計書を書くよりは要件だけAIに投げて叩き台のコードを書かせてブラッシュアップした方が早いと感じるのではないだろうか。
動かない設計書より動くコードの方が良い、とは私は思わない（実装速度だけ評価するなら異論はない）のだが、実際問題動かない設計書を動くコードに一瞬で書き換えられて、精度も8割ぐらいできているならエンジニアリング経験がある人なら設計書側を見直せばコードにすぐに反映されるということもあり、自力でコーディングを頑張らなくても良いようになった。

いきなり100%を目指さず、必須機能だけが入ったスモールな設計にできるかどうかが肝だろうか。
あまり参考にならないが、１ファイルにすると500行あたりから出力が怪しくなったのでファイル分割をする事も考えていかなければならないだろう。

最初から設計や要件を難しく考えるのではなく、なんとなくPoCを作らせてみるぐらいで生成させるのが良いだろう。
その結果が初期バージョンだった。

### テスト
実装をしたらテストをする。
動けばOKという感覚になりがちだが、特にデグレテストはしっかりやる。
AIの挙動はところどころステートレスなのでは？と思いたくなるぐらい記憶がぽっかりと抜け落ちる（少なくとも、人間が必要性を認識した上で書いたコードであれば間違って消すようなことはしない）挙動をするので、リファクタリングがリファクタリングではなくエンバグでしかなかったりするので、プロンプト一発で生成できないコードは全部疑うべきである。

#### ノーコード開発したコードをテストした所感
今回はcursorを使っているので生成結果とのdiffは取れているが

- 要件を（ある程度）正しく認識している
- システム設計イメージがわいている
- 開発経験がある
- コードが読める
- プロンプトを改善できる

という下地があったので、結果的にノーコードにできたというのが感覚値としては近い。
ぶっちゃけ、未経験ならAIにコードを書かせる（＝プロンプトエンジニアリングを頑張る）よりは、自力で理解できそうなフェーズまで来たなら軽微な修正を相談しながら自分で書くつもりでやった方が結果的に早いし、力もつくだろう
AIの精度が上がってくればこの問題も解決していくのだろうが、現時点（執筆・初投稿時点）ではまだまだAIによってプログラマーの仕事がなくなる、なんて事はなさそうだ。
ましてや、システムエンジニアレベルだと「具現化されていないシステムへのイメージを具体に落とし込み、実装または運用における問題点を察知する」というスキルが必要であるため、どうしても経験値が必要になる。
AIと壁打ちしながらある程度は解消する事ができたとしても、システム運用やトラブルシューティングにおける「経験知」はなかなかデータ化されにくいからか、AIが苦手とする分野のように感じる。

:::note
#### コラム
人間側も同じ理由で「AIに親しんでいないユーザーがプロンプトエンジニアリングを頑張る」というのはやはり時間もかかるし、精度も落ちてしまうので双方の歩み寄りが重要だなと感じている。
たとえ、将来的にAI側の精度が高まるとしても、AIの能力をより多く引き出すという職人レベルの仕事スキルは絶対必要になるのではなかろうか。
たとえば、車の運転は免許さえ取れれば誰でもできるが、早いタイムを出すために車を速く走らせる技術であったり、また車自体の性能を上げることでタイムを削っていくのは専門家でないと難しいのと同じように。
速さを求めないとしても、例えばバスやタクシー、電車などを自動運転にするか？というと法整備や異常ケースへのシステム側での対応が難しい部分もあるなど、完全性の担保が難しいという問題もある。
システムやAIを利活用するのが人間である以上「仕事がなくなる」とは、技術的な課題以外も含めてではないだろうか、と筆者は考えている。
:::

### gitを使ってソースコードを保存する
タイミング的に挟めなかったのでここで言及するが、１機能を作るごとにgitを使ってプログラムのソースコード自体のバージョンを管理する。
とはいえ、個人開発だと最初のセーブ（first commitとも）はある程度まとまった状態でアップする事が多いだろうか。
プロジェクトなどで複数人メンバーで開発する場合は、プログラムを書く前に環境構築を行い、全員の開発環境を整えるという事をやる。
この時によく使われるのがDockerというコンテナを使った仕組みであり、またDocker自体がインフラ側のソースコードの塊（IaCとも）であるため、これ自体もgitで管理できる。
後述の初期版はこの時に作ったコードである。

### 機能追加
初期バージョンでは、メッセージを送信して編集・削除をする機能があればとりあえずよかった。
ここに、運用していった時の不満や要望をキャッチアップしていく。研修でいう「二次開発」である。
これらも当然「自分は」ノーコードである。

- 【機能】一部ブラウザの挙動により、編集・削除ボタンの挙動（ポップアップウィンドウの表示）が使えない問題を解消する
  - 編集ボタンを押すと、投稿欄やボタンが更新機能に置き換わる
  - 編集のキャンセルが必要
  - 削除ボタンをミスタッチした時に消えるとまずいので、人間が意図的に押した事をある程度担保したい
- 【機能】文字が小さくて見えないので拡大してほしい
  - ブラウザの標準機能の拡大は拡張機能に適用されない
  - いわゆる拡大縮小アプリを使うと、なんのための拡張機能かわからない→実装へ
  - 文字の拡大自体はできたが、拡張機能の初期設定だとウィンドウサイズが狭いため、見切れてしまう
  - ウィンドウ枠の上限と下限は決まっている
  - 運用対処：ウィンドウ枠の限界にあわせて配信環境側をいじったり、場合によってはコメントメッセージの書き方も変える必要がある
- 【機能】新しいマニフェストのバージョン（３）に対応したい
  - これから作り始めるのに、将来的に使えなくなる前提だとライフサイクルが短すぎて勿体無い
  - とはいえ、新バージョンのサンプルや運用対処（制約があるのは分かったが、解決するためのソリューション）は自分で考えるしかない
  - 特にCDNが使えない＝バージョン管理をこちらでする必要がある？という問題を抱え続けることになる
    - アップデートをしないで運用するよりはなんぼかマシだろう
- 【機能・不採用】文字の拡大縮小ボタンを画面スクロールに追従させたい
  - 文字の拡大縮小は最初にサイズ確認する時ぐらいしか使わない
  - 画面が小さいのでこれ以上置くと見たいものが見れなくなった
  - 頻繁に切り替える事はないはず
- 【機能・不採用】一番上または下へスクロールするボタンがほしい
  - あると便利。それは分かる。一日で最後の講義のまとめとして使いたい
  - 画面が小さいのでこれ以上置くと見たいものが見れなくなった・２
  - 今後、画面に追従するボタン系の実装はやらないと決めた

箇条書きにした内容を順次実装し、１機能作るたびにやはりテストをする。
テスト工程については１次開発と同じなので省略。

### リファクタリング
ここまでの内容を全部やってみると冗長なコードが多かったり、適切にクラス化すれば可読性や保守性を高められる書き方になっている事が多い。
とはいえ、意味がわからないと思うので、初期版のコードと最新版のコードを意味が分からなくて良いのでなんとなく眺めてみよう。
念のため、クラス自体やメソッドにコードコメントを添えておいたが、おそらく解説は必須だろう。
（テキスト化しようとしたのだが、書いている途中にアレコレと気になって差し替えたため、口頭解説＋デモにする）

:::note
#### 講義メモ
あの機能も追加しよう、この機能も作ろう…とやっていると「あれとこれは同じ事をやってるから使いまわせるよね！」＝再利用性と保守性の観点から機能をまとめておいた方が便利な事がある。
また「この仕組みを応用して似たような機能を作ろう」といった点から拡張性にも富ませる事ができる。

裏を返すと、複雑性や依存性が高まってしまう事があるため、この辺りの匙加減が難しいところだ。

という話を、うまく噛み砕いて解説したい。
:::

#### AIのリファクタリングは破壊的
敢えてpythonチックな表現を使うが、人間がリファクタリングをする場合はよほど深刻な問題を抱えた機能でもない限り大掛かりな修正はしない。
機能追加時にコピペしてきたコードをまとめたりとか、変数名や関数名の見直しとかマジックナンバーを撲滅する、型宣言や出入り口の監視・判定強化など。
機能追加のカテゴリにはなるがシステム例外（ネットワークに繋がらない、サーバーから応答がない、ディスク容量がない…）をtry-catchするのが大きな仕事だろうか。

AIにリファクタリングをさせると、既存のコードをいじりすぎないようにしよう、なんて発想はない。
プロンプト側で「関数の引数やreturnのデータ型を変えずにクラスまたは構造体を再設計しろ」と言ってもお構いなしに何かをやらかしたコードを持ってくる。
動けば御の字で、大体の場合何かを間違えて出力してくる。
新規開発で精度80%だと嬉しいが、変更で精度80%でデグレありはただのトラップでしかない。AIではなく人間だったなら「どんな嫌がらせだ」と怒るだろう。

逆に言うと、初期版を作る段階と違って要件が明確に固まっており、参考にできる動く状態のコードが手元にあるので、教師データが存在するのだから、AIが生成する精度も80%程度としても間違え方も意味のわかる失敗の仕方をしてくるだろう。
少なくとも、同じリファクタリングという目的で初期版の頃のプロンプトと最新版時点でのプロンプトは書き方が変わっているはずだ。
つまり、すべての要件を満たす状態のコードを使って人間が書くプロンプト自体が変わったため、AIの生成結果も変わったという事実に注目したい。どちらも精度が80%だったとしても、その意味合いは異なる。

その上で、敢えて80%程度の精度を肯定的に評価する。
つまり、人間ではできないリファクタリングのアプローチをAIにやらせて、良い書き方をベースに人間側がレビューをすれば良い。
この工程だけはノーコードでできないため、本稿執筆においてはピンポイントにコードの書き方について「コードを日本語コメントに直し、日本語コメントからコードを書き起こせ」という形でプロンプトを書いてリファクタリングを実施している。
クラスやメソッドの長いコメントは、そのままAIへのプロンプトになったのだ。

## 運用
（次の講義後に追記）

## 参考: 初期バージョン
最新版はGitHubリポジトリを参照。

<details>
<summary>コード: index.html</summary>

```index.html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>チャット形式メモアプリ</title>
    <!-- QRCodeライブラリを先に読み込む -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <style>
        body {
            width: 300px;
            font-family: Arial, sans-serif;
        }

        #chat-container {
            height: 300px;
            overflow-y: auto;
            border: 1px solid #ccc;
            padding: 10px;
        }

        .message {
            margin-bottom: 10px;
        }

        .message .actions {
            font-size: 0.8em;
            color: #888;
        }

        #input-container {
            margin-top: 10px;
        }

        #message-input {
            width: 70%;
        }

        /* QRコード用の新しいスタイル */
        .qr-codes {
            margin: 10px 0;
        }

        .qr-wrapper {
            margin: 10px 0;
            padding: 10px;
            background: #f5f5f5;
            border-radius: 4px;
        }

        .url-text {
            margin-bottom: 5px;
            word-break: break-all;
            font-size: 0.9em;
            color: #0066cc;
        }

        .qr-code {
            display: inline-block;
        }

        .qr-code img {
            display: block;
            margin: 0 auto;
        }
    </style>
</head>

<body>
    <div id="chat-container"></div>
    <div id="input-container">
        <input type="text" id="message-input" placeholder="メッセージを入力">
        <button id="send-button">送信</button>
    </div>
    <!-- script.jsを後で読み込む -->
    <script src="script.js"></script>
</body>

</html>
```

</details>

<details>
<summary>コード: script.js</summary>

```script.js
document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    let messages = [];

    // メッセージを読み込む
    chrome.storage.local.get(['messages'], (result) => {
        if (result.messages) {
            messages = result.messages;
            renderMessages();
        }
    });

    // メッセージを保存する関数
    function saveMessages() {
        chrome.storage.local.set({ messages: messages }, () => {
            console.log('メッセージが保存されました');
        });
    }

    // メッセージを表示する関数
    function renderMessages() {
        chatContainer.innerHTML = '';
        messages.forEach((msg, index) => {
            const messageElement = document.createElement('div');
            messageElement.className = 'message';

            // メッセージテキストの div
            const textDiv = document.createElement('div');
            textDiv.textContent = msg.text;

            // URL を検出して QR コードを生成
            const urls = extractUrls(msg.text);
            const qrContainer = document.createElement('div');
            qrContainer.className = 'qr-codes';

            if (urls.length > 0) {
                urls.forEach(url => {
                    const qrWrapper = document.createElement('div');
                    qrWrapper.className = 'qr-wrapper';

                    // URL 表示
                    const urlText = document.createElement('div');
                    urlText.className = 'url-text';
                    urlText.textContent = url;
                    qrWrapper.appendChild(urlText);

                    // QR コード生成用の div
                    const qrElement = document.createElement('div');
                    qrElement.className = 'qr-code';
                    qrWrapper.appendChild(qrElement);

                    // QR コード生成
                    new QRCode(qrElement, {
                        text: url,
                        width: 128,
                        height: 128,
                        colorDark: "#000000",
                        colorLight: "#ffffff",
                        correctLevel: QRCode.CorrectLevel.H
                    });

                    qrContainer.appendChild(qrWrapper);
                });
            }

            // アクション部分
            const actionsDiv = document.createElement('div');
            actionsDiv.className = 'actions';
            actionsDiv.innerHTML = `
            <a href="#" class="edit" data-id="${index}">編集</a> | 
            <a href="#" class="delete" data-id="${index}">削除</a>
        `;

            messageElement.appendChild(textDiv);
            messageElement.appendChild(qrContainer);
            messageElement.appendChild(actionsDiv);

            chatContainer.appendChild(messageElement);
        });
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    // URL 抽出用の新しい関数を追加
    function extractUrls(text) {
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        return text.match(urlRegex) || [];
    }

    // メッセージを追加する関数
    function addMessage(text) {
        messages.push({ text: text, timestamp: new Date().getTime() });
        saveMessages();
        renderMessages();
    }

    // 送信ボタンのクリックイベント
    sendButton.addEventListener('click', () => {
        const text = messageInput.value.trim();
        if (text) {
            addMessage(text);
            messageInput.value = '';
        }
    });

    // Enterキーでの送信
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendButton.click();
        }
    });

    // 編集と削除の機能
    chatContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('edit')) {
            const id = e.target.getAttribute('data-id');
            const newText = prompt('メッセージを編集', messages[id].text);
            if (newText !== null) {
                messages[id].text = newText;
                saveMessages();
                renderMessages();
            }
        } else if (e.target.classList.contains('delete')) {
            const id = e.target.getAttribute('data-id');
            if (confirm('このメッセージを削除しますか？')) {
                messages.splice(id, 1);
                saveMessages();
                renderMessages();
            }
        }
    });
});
```

</details>

<details>
<summary>コード: manifest.json</summary>

```manifest.json
{
    "manifest_version": 2,
    "name": "メモアプリ",
    "version": "1.0",
    "description": "Zoomやライブ配信用のメモアプリ",
    "permissions": [
        "storage"
    ],
    "content_security_policy": "script-src 'self' https://cdnjs.cloudflare.com; object-src 'self'",
    "browser_action": {
        "default_popup": "index.html"
    }
}
```

</details>
