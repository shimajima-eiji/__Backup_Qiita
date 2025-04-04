# せっかくのMeetupなので自己紹介要素を多めにいきます

---

## 本日のスライド
`https://qiita.com/nomurasan/items/b04d22a305d9a722d8d3`

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/5cc770ca-986d-91df-a249-d37afc05c118.png)

---

## 来歴
:::note
<font color="white">ミッション：研修だけで終わらないエンジニア育成と定着を促進する</font>
:::

- IT/AI/DX推進役、エンジニアオンボーディングコンサル・講師
  - 元々はWebアプリエンジニア畑の出身
  - 最近の課題は研修後施策としての研修Well-Being立案
  - その他、DevRelなどエンジニアの働きやすさの啓蒙活動に注力
- LiONではIT講師の立場では教材作成や認定試験、講師育成
- 趣味で勉強会に参加しており、オープンソースカンファレンス系や技術書典、技書博に一般参加常連
  - 10代の頃から日本全国の同人誌即売会に毎週参加して新刊を作成していた時期があり、個人出版や印刷の知識はそこそこある

---

## 生成AI活用分科会とは？
- 公式(Slackより)
  - > GPTやClaudeなどの生成AI (LLM) を活用して、執筆系のアウトプットなどを効率化できないか、についてざっくばらんに模索するチャンネルです
- 私の理解・見解
  - ChatGPT(OpenAI API)やClaude(Anthropic)を活用してLiONコミュニティ活動に寄与できないかを検討する
  - 現状はテキスト生成がメインだが、執筆用の資料作成なども活用したい

---

## Simple Text Refineとは
https://marketplace.visualstudio.com/items?itemName=yasuraok.simple-text-refine

- VSCodeの拡張機能
- ChatGPT(OpenAI API)やClaude(Anthropic)を活用して回答結果をテキストファイル文中またはVSCodeタブに反映する強力な公正支援ツール

作者はLPI Japanの安良岡さん。
元々は教材作成や試験問題の作問を支援するツールだったそう。
私が個人的に気に入って活用範囲を汎化できないか、ユーザーフィードバックを一方的に送っている

https://github.com/yasuraok/SimpleTextRefine

---

# デモ（コード解説例）

---

## 設定例
```
{
    "simple-text-refine.api_key_openai": "", // OpenAI APIキー
    "simple-text-refine.api_key_anthropic": "", // Anthropic APIキー
    "simple-text-refine.model": "openai/gpt-3.5-turbo",  // 使用するモデル。後述
    "simple-text-refine.prompt_path": "",  // プロンプトファイル
}
```

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/6c9ff56b-ea1c-8e1d-6604-0cd968c20f1d.png)

---

# 勉強会・ハンズオンの機会を作って流行らせたい…

---

# 課題

---

## Simple Text Refineに期待していること
:::note
<font color="white">教材スライド（PDF）をマークダウンで書けるようにしたい</font>
:::

- 資料をGitで管理したい
- plantUMLとかmarmaidとかで作図しても良い
  - とはいえ、自力で書くのが面倒なので、diffが見れるので超助かる

---

## 生成AI活用分科会に期待していること、やりたいこと
:::note
<font color="white">脱・パワーポイント、Googleスライド</font>
:::

- マークダウンで教材スライドのレイアウト調整に対応できる状態
- GUI自体は悪くないので、編集した内容をコードにしてほしい
- Text2Textにこだわらず、Text2X（教材資料作成の図表、イラスト、動画教材作成など）も検討したい

---

## 将来的にやりたいこと
:::note
<font color="white">メタバースAIによる教育機会の創出、提供</font>
:::

- 既にメタバースプラットフォーム上での学生向け教育サービスはある
- エンジニア教育の観点では、仮想空間上（物理空間では見えないもの）で仮想技術を可視化すると学習能率が上がるはず、という仮説を持っている

:::note
<font color="white">開発入門者の「やりたい」を実現する仕組み作り</font>
:::

- （教育機会の都合で）Webアプリやインフラエンジニア以外の育成機会が提供されていない
  - 入門するにしても技術的に難しい、講師の確保や教材作成が難しい
  - どうしても現場経験が前提・必要になってしまう
