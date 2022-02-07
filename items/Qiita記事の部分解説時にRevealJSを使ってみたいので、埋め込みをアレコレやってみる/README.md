## 結論
運用対処に依るところが大きいが、実現はできた。

## 発端
Qiitaスライドにすると、ページ全体がスライドになってしまうので非常に使いにくい。
そこで、部分的なコード解説を視覚的にやる方法を考えたところ、CodePenで読めるものなら埋め込めるのでは？と気付いたので検証してみる。

## 解決方法
CodePenのHTMLに埋め込みタグを入れてしまう。
Qiitaに直接埋め込みタグを書いても相手にされないので、QiitaでCodePenの埋め込みが読める点に目をつけて、CodePenが読んだ埋め込みタグを間接的に表示させられないかというもの。

<p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="jOGpzqZ" data-user="nomuraya" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/nomuraya/pen/jOGpzqZ">
  QiitaにRevealJSを埋め込めるか</a> by nomura (<a href="https://codepen.io/nomuraya">@nomuraya</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
[スライドをフルサイズで見る](https://codepen.io/nomuraya/full/jOGpzqZ)[^1]
[^1]: 【フルサイズのURL】今回はCodePenのビューを貼り付けたが、よく考えたら埋め込みコード内のURLに直接飛ばす手が一番手っ取り早いかもしれない。

Qiitaでの使用感はQiitaスライドには及ばないが、スライドをフルサイズで見る方法を提示する方法で回避できそう。

### 注釈
