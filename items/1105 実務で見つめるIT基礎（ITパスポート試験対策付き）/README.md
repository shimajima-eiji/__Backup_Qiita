:::note warn
## キーワード
- 覚える
  - レベル１：その場で話ができればOK。すぐ忘れよう（＝理解したレベルに落とそう）
  - レベル２：忘れてもいいようにするが、できればレベル3にしたい。後で見直ししやすくしよう
  - レベル３：忘れないようにしよう
- 理解する
  - 後で見て思い出せるレベルを目指す
  - 覚える（に越したことはない）必要はないが、忘れたとしても何を言っているかは分かっている状態
- 知る
  - 「よくわからないけど、なにか言ってたな」程度を目指す
  - 【知らない】からの卒業が目的
:::

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

### 「はじめに」の目次（学習予定表）
- なぜこの作り（構成）になっているのか
- ITパスポート試験勉強をすること（受かることではない）が自身の今後にとってどのように活用できそうかイメージする

### 情報に関する理論
- アナログとデジタル
  - デジタルが0/1で表現される理由と、デジタルでアナログを表現する方法
- ビットをバイトに変換する理由

### コンピュータの構成とCPU
データの流れを追いかけよう

- 入力装置：ハードウェア→ソフトウェア
- 出力装置：ソフトウェア→ハードウェア
  - 入出力の制御にはハードウェア起因の問題とソフトウェア起因の問題があるため「動かない」トラブルへの対応は慎重に切り分け作業を行うこと
- 制御演算装置：処理するもの。1秒間にどれだけ処理できるか（クロック周波数が多いか）が重要
  - CPU: 汎用
  - GPU: 画像処理（AI・ブロックチェーン）
- 主記憶装置：覚えておくもの。寝たら忘れて良い（揮発性）
- 補助記憶装置

読み書きの権限としてそれぞれにRAM/ROMがあり、目的に応じて使い分ける
なお、主記憶装置にも補助記憶装置にもRAM/ROMがあるため、混同しないように（DVD-RAM/ROM。電気屋を見てみよう)

### AI：日進月歩の技術のため試験の出題傾向が読めないが、全部重要
- 機械学習
  - 教師あり：予測：分類
  - 教師なし：クラスタリング
  - 強化学習：最適化
- ディープラーニングとニューラルネットワーク
- AIの問題点
  - 過学習
  - ハルシネーション
  - 不適切な表現など
  - ディープフェイク

## 知っておくぐらいで良いもの
テキストに書いているが、ここに書いてないもの全部
ただし、試験前に詰め込んだほうがいいものを以下に置く

### 試験対策で頑張って覚えよう編
:::note warn
特に言及しない限り、覚えるレベル１で良い
:::

- 情報量の単位
  - 10^3 = 1000ずつとしているが、厳密には2^10=1024であること
- 文字コードの種類と、日本語は2バイトで1文字
  - テキストにマークしておこう！ UTF8
- コンピュータの構成とCPU
  - DRAM/SRAM
  - 補助記憶装置
    - ディスク装置
      - RAID(0/1/5)
    - 光ディスク
    - フラッシュメモリ
- 確率と統計
  - 順列と組み合わせ
  - 平均
  - 中央値・最頻値・範囲・分散・標準偏差
  - 正規分布
    - データの取り方が良くないケースだったり、データ自体が不正なケースなどもある
- 基数変換: 2 <-> 10 <-> 16進数
