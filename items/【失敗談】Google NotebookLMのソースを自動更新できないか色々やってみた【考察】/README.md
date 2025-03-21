:::note
本稿は失敗談としてはいるが、可能性は感じているので継続していきたい
:::

## TL;DR
やりたかったことは以下。

- NotebookLMのデータソースを自動で取得したい
  - ダメらしい。以下URLに試行錯誤の痕跡を残す
- フォルダ以下をまとめて取得したかった
  - これもダメ。ファイル単位で指定が必要のこと

https://docs.google.com/document/d/14D_19MK3bAH-zoeGho_fdbOTO8-V5ntVzdIlURBD9_I/edit?usp=sharing

## 発端
https://omoshiroai.connpass.com/event/323123/

やなしまさんのLTでGoogleNotebookLMの話があり、めちゃくちゃ便利じゃん！ってなった。
で、自分でも使ってみようと思ってガチャガチャやってみた所感をまとめておく。

## Google NotebookLMが使えると何が嬉しいか？
詳細は語らないが、ナレッジ管理ツールにAIが入った版
予めデータソースを突っ込んでおいて、ChatGPTとかを使う感覚でデータ検索ができる

## 所感
### イケてる！…のか？
書いてない内容とGeminiが連携しているらしい！
→自力検証してみたものの、あまりそういう印象は受けない。データソースがないから回答を返せない、という結果がGemini連携の部分だとしたら期待している回答は得られていないことになる
今の所、通常のGPTsサービスを使った方がまだ便利な感じはする

データソースの数を手動でも増やしながらどうなるかは様子見したい

### データソースに限定した範囲での検索システムとしては優秀
外部検索に頼らないということは、データソースに特化した検索サービスを作りやすいという事でもある
同様のサービスはesa、Notionのようなナレッジ管理ツールから勉強用に作ったブログなど色々あるが、

### AIにカンニングノートを作らせる
たとえば、学習ノートの内容をテキスト化してNotebookLMに食わせておけば、テスト時に堂々カンニングできるやん！というのが真っ先に閃いた使い方だ。
もちろん、普段からしっかりノートを執っていることが前提になるので、カンニングのためにノートを執ることで学習効率を高められるなら、勉強法としては良いのではないだろうか？
（私も講師という立場であるためこのような目的自体はいただけないが、学習効果が上がる取り組みとしては評価している、の意）

一応、プロンプトエンジニアリングの練習にもなるし、プロンプトを意識したなんちゃってRAGを作成するわけだから、そういった意味でも知見は得られる。
まるで思春期時代のあの頃を思い出すような話でむず痒さはあるが、いつの時代も自発性・積極性を発揮できるのはこういった裏技発見的なところが大きいのだろうと思う。

### AI活用を前提にしたナレッジ管理手法が身に付く
私が感じたのはこれが大きい。
人間の情報管理とは結構雑なもので、微妙な表記揺れは多く発生したものだ。
で、AIが入ることでこのような表記揺れを気にせずナレッジを溜めることができるようになった。

しかし、AIは万能ではない。
人間の分かりやすさを損なうことなく、AIがまとめやすいように書くことがどういう事なのかを考える事ができる。
極端な表現をすれば、自分用のノートであっても、必ずAIという第三者が介入する事である程度のフォーマットを考えるようになる。
そして、整理された有用なフォーマットとは何かを考えることになり、結果的にノート自体の品質が高まっていく。
ノートの品質が高まると読みやすさに直結するため、結果的に品質の高いナレッジ管理が実現できる。
もちろん、ナレッジ自体の品質もあるのだが、ナレッジ管理の品質が低いせいでナレッジが活かされないという状況は防ぎやすくなることを期待する。

## 結論：NotebookLMの改善とともに、自身のナレッジマネジメントスキルの向上を図ろう
NotebookLMというサービスを通じて、自身のスキルアップができるのであれば万々歳だ。
できればNotebookLM自体をサイトを超えたナレッジ管理ツールのスーパーアプリとして活用しやすい状況になることを期待する。
