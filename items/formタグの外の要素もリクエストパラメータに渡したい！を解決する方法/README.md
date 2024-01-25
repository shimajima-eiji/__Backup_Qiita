## 結論
```
<form action='' id='target'>
（中略）
</form>
```

のように、formにIDを設定しておいて、

```
<input form='target' name='outform'>
```

のように、formタグの外でもform要素にformのIDを入れると、formIDをsubmitした際にパラメータを渡せる。

## 検証コード
https://shimajima-eiji.github.io/Hosting2/for_blog/form_out.html

CodePenで埋め込もうと思ったけどsubmit（遷移）が必要なのでGitHubPagesでホスティングする。

## 発端・参考
https://note.com/kakidamediary/n/n85a5aa43749b

---

## ポエムとか
元々はReactだとオーバースペックすぎる簡単なWebアプリを作ろうとしていて、手頃なWebフレームワークを探していたところRemixに辿り着いたので、その過程でtableタグとformタグを組み合わせたいシーンが出てきた。
で、いつも何も考えずに

```
<form ...>
  <table>
    ...
  </table>
</form>
```

みたいに書いていたのだが、複数のformで値を使い回したいシーンが出てきた。
今回は結局JavaScriptの介入が必要になってしまったのだが、そもそもの話としてformタグの外の要素をformに埋め込むという方法を知らなかったので、凝ったことをしなければ使えそうな気がしたので、formタグの講義資料などでいつか役に立つことを期待する。
