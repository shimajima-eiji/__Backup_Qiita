:::note warn
実際にノンプログラマー研修で使った資料をQiitaアドカレ用に編集したものである。
本稿はハンズオンがメインであり、座学が少ないのは資料中の解説が多いためである。解説パートは思い出しながら書いているため、漏れ抜けが多く生じている。
:::

:::note
著作権や公開権を含む諸権利は当方に帰属しているため、公開などによる問題はない
:::

## やること
https://qiita.com/nomurasan/items/32a0b3e8a9551b1b2152

## かかった時間
動作確認込み30分
自力で全部やろうとしたら2時間ぐらいはかかっているだろう。
加えて、コーディングのモチベーションがあまり高くないメンタル状態であり、そもそも深夜25時にやってるので能率も悪いはず。そう考えると同じ時間・タイミングで実施していたと仮定すると2時間で終わらなかった可能性は高い。

## やったこと
これはある程度プログラミング経験があったり、コーディングやシステム設計の知見があったのでできたことかな、と思ってる。

- 開発丸投げ
  - 出力されたコードをコピペして実行、エラーを投げ返す
- コードを読んで原因特定
- コピペでどうしても解決できない（エラーにはなっていないが問題が解決できない）場合、異なる方針やアプローチを検討し、AIにコーディングの指示を出す
  - いわゆるプロンプトエンジニアリング部分。文章を考えるだけでなく、問題点や課題を指摘しているため設計＋AIスキルが必要

## やらなかったこと
- コード
  - エラー調査
  - 原因調査
  - デバッグ
- AI
  - 凝ったプロンプトエンジニアリング
    - １プロンプトを書くのに20秒以上考えたり書く時間も使っていない
    - ただし、原因分析や検討し、試行錯誤した回数は8回/1時間
      - 闇雲にやっていたら更に試行回数は増えただろうし、時間もかかっているはず
  - RAGを使う、AIを選定する
    - 困ったらとりあえずperplexity
    - GitHub Copilotを使うべきだったが、有料はなるべく使いたくない気持ち…
- ツール
  - ブラウザのみ、GitHub上で完結
  - コマンド系、ローカル開発環境（Remote-VSCode含む）の使用を禁止（制限をかけたというより、使わずになんとかした）
  - もちろん、github.dev(ワークスペース)も未使用

## 追記・研修実施所感
AIを使うとコーディング能力はあまり大きな違いが出てこないんだろうな、と思った反面、AIをどうやって使うかは活用スキルが必要だし、AIと議論をしながら前に進めるには設計を含めた現場スキルがないとAIの誤りや問題点を指摘し、改善提案は難しい。
スキル０の人が学習目的に使う事はできるが、スキル０の状態で即戦力か？というと微妙だ。
これはIT業界だけでなく、他の業界でAIが使えたとしても即戦力にはならないだろうな、というのが正直な感想だ。
