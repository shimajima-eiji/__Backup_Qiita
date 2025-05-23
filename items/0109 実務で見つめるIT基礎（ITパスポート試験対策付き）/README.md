:::note warn
## キーワード
- 覚える
  - レベル１：その場で話ができればOK。すぐ忘れよう（＝理解したレベルに落とそう）
  - レベル２：忘れてもいいようにするが、できればレベル3にしたい。後で見直ししやすくしよう
  - レベル３：忘れないようにしよう
- 覚えない（忘れる）
  - 覚える・レベル１（その授業時間が終わったらここへ）
  - 理解する
    - 後で見て思い出せるレベルを目指す
    - 覚える（に越したことはない）必要はないが、忘れたとしても何を言っているかは分かっている状態
  - 知る
    - 「よくわからないけど、なにか言ってたな」程度を目指す
    - 【知らない】からの卒業が目的
    - この時間中に理解が難しいものでも、一旦は「知らない」という状態にはならないようにしたい
:::

回を重ねるごとに実務的な重要度が高まっており、内容が複雑化している。
そのため、本稿より知っておく程度で良いものについての解説を省略していく。

## 覚えておくと良いもの
:::note
## 努力目標
なるべく覚えない（＝脳みそを疲れさせない）、覚える量を減らす努力をする
:::

脳のキャパシティ（＝学習疲れ）をなるべく回避するための道標として使って欲しい


## 理解しておきたいもの
:::note warn
めちゃくちゃ多いので、読んですぐ理解できなければ聞いてしまおう
今日学んで明日までに忘れることが目標
:::

脳のキャパシティ（＝学習疲れ）をなるべく回避するための道標として使って欲しい

### クライアントサーバーシステム
- クライアント＝サービスを受けたい人・コンピュータ
  - イメージとしてはお客様
  - シンクライアントの場合、処理だけでなくデータもサーバーに置くので、指示専門の端末になる
- サーバー＝サービスを提供する人・コンピュータ
  - イメージとしては事業者

試験範囲としてはサーバーの種類を問われることが多いが、実務を意識するならWebシステムにおける関係の方が大事で、

- クライアント→サーバー：要求することをリクエスト
- サーバー→クライアント：提供することをレスポンス

の方が学びという意味では重要。

### バッチ処理とリアルタイム処理
言葉を聞くだけなら間違えないと思うが「どういった時にバッチ処理・リアルタイム処理がいいのか？」が重要（実務としても、試験対策としても）

### システムダウンと復旧
:::note warn
用語を覚えようとする前に、目的を確認しよう！
:::

システム障害が発生した時にバックアップやリアルタイムにデータ最新化をどれだけ早くできるか、またそのコストはどうか？が重要

- 一般に、システム復旧が早いものの方が待機にもコストがかかる
- イメージしやすいのが、日中などの場合は復旧時間中もシステムの利用者たちを待たせるのにコストがかかる
  - 社内システムだと給与
  - 社外に提供しているサービスだと損害賠償

### サーバーの仮想化技術と運用
- 端末が独立した技術
  - スケールアップ：性能を高める
  - スケールアウト：端末を増やす（覚え方の例：今あるものを一部切り出すから「アウト」）
- 端末を連携する技術
  - クラスタリング：サーバー間連携。極端な話、１台の端末でも完結可能
  - グリッドコンピューティング：複数のコンピュータを連携して１台の高性能なコンピュータを作るもの。ドラゴンクエストでいうところのキングスライム

### 稼働率と故障〜復旧時間
- MTBFは回数、MTTRは時間
- 稼働率は特定の時間を切り抜いたもの。特に指定がない場合は、システムを起動し始めてから今日まで、と考えても良い

#### 直列システムと並列システム
基本的に、システムを直列である。たとえば簡単なECサイトを考えると、「Webサーバー・データベースサーバー・メールサーバーの全部が動いていてようやくOK」という状態。
この直列システムをいくつ足せば良いか（システムのバックアップ環境に切り替える際に、２並列で良いのか、３並列にしておくのか）を計算するために並列システムの稼働率を考えることが多い。

※同じシステムを想定するため稼働率をイコールで考える事が多いが、試験では理解度を問われるため稼働率が異なるシステムの計算をする事が多い印象

### 稼働率の計算
:::note
式をそのまま覚えようとするのではなく、式の意味を理解しよう
:::

まず、直列・並列によらず稼働率と故障率で考える。

```math
\begin{array}{rcl}
\text{稼働率} &=& \frac{MTBF}{MTBF + MTTR} \\
&& \text{全体の時間に対する、システムが正常に動作している時間の割合} \\
\\
\text{故障率} &=& 1 - \text{稼働率} = 1 - \frac{MTBF}{MTBF + MTTR} \\
&& \text{全体の時間に対する、システムが故障している時間の割合}
\end{array}
```

したがって、直列システムは全ての稼働率の掛け合わせで求められる。

#### 並列システムが動いている条件を考える

1. 全てのシステムが同時に故障する確率を求めて
1. 100％から同時故障率の差を求める

ことで求められる。

```math
\begin{array}{rcl}
システム全体の稼働率 &=& 1 - ((1-A) \cdot (1-B)) \\
&& \text{ここで、} \\
&& A: \text{Aシステムの稼働率} \\
&& B: \text{Bシステムの稼働率} \\
&=& 100\% - (\text{Aシステムの故障率}) \cdot (\text{Bシステムの故障率}) \\
&=& 100\% - \text{AとBの故障率}
\end{array}
```

となる。
同じように、３並列以上はこうなる。

```math
\begin{array}{rcl}
システム全体の稼働率 &=& 1 - ((1-A) \cdot (1-B))  \cdot (1-C)) \\
\end{array}
```

後ろに故障率（100% - 追加したシステムの稼働率）を追加していく。

### システムの評価
システムは故障しないに越したことはないが、故障しても問題が小さいようにすることも重要だ。
故障しにくくするために誤作動しない（できない）ように安全ロックをかける方法もある。
故障した時にシステムを止めるのか、故障しても動かし続けられるようにするのかを考える。
なお、何をしたら壊れるか・どこまでなら壊れないかを予め把握しておき、運用で回避するのも重要。

なお、故障する・しないに関わらずシステム全体を考える場合はコストが密接に関わってくる。
たとえばスマートデバイスの購入・利用を考えた時に

- 2・3年縛りの総コスト
  - 初期投資
  - 月額料金。イメージしやすいように敢えてサブスクと呼ぶ

が生じる。
総額から考えた時に、端末料金を一括で支払っていても月々支払いにしても総コストは変わらないので「実質料金」と言っている。
（が、実質料金という言葉が苦手な方も多いと思うので、実質の意味を正しく認識しておこう）

### 例で学ぼう！エッジコンピューティング・エンベデッドシステム
- エッジコンピューティング（インターネットは関係ない。近辺のデータ集積基盤となるサーバーを置いてデータを管理すること）
  - スマートホーム
    - Amazon Echo
    - Google Home
    - Line Clova
  - Apple Watch
  - 
- エンベデッドシステム（インターネットに繋がっていなくてもOK）
  - 電子レンジ
  - デジタルカメラ
  - エアコン

これらをインターネットにつなげればIoTデバイスとなる。
通常、いわゆるパソコンやスマホで動画を見る時のような大容量の通信に対応する規格よりは、省電力で広域の無線通信規格が求められる。

#### インターネットに接続するリスク
便利とセキュリティはトレードオフである。
たとえば防犯カメラを考えた時に、インターネットを介して不在時にも来客を知る事ができる。
ただし、正しいセキュリティ設定・運用をしないと防犯カメラが盗撮カメラになってしまうリスクがある。

### サーバー仮想化技術がもたらしたビジネスのソリューション
:::note
実務でも試験でも頻出するのが本項だが、業界人以外にとってはただの暗記問題でしかないので用語解説はしない。考え方や歴史に注目していく。
:::

ソリューション＝方法・手段。解決することを期待する

基本的には何かしらの課題があって、その課題を解決するためのビジネスという意味合いが強い。
課題解決の方法を具体的にサービス名やシステム環境から見つめていく。
いわゆる「システム化」の幅が広がったことで、業務の幅も広がったが、同時に（業務に限らず）システムの高難度化を意味するようになった。
その結果、個々人の情報リテラシ（情報能力）が求められるようになり、能力差による格差が顕在化するようになった、という新しい課題を生み出してしまう結果となっている。
