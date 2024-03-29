記事が修正されないようなので、私が書き直します。

---

# for文【for(これ;これ;これ)】の内容を正しく説明できますか？

研修中ではよく以下のように説明されています。これは**間違いではありません**が正確な説明ではありません。


```php
for(
  変数の初期値;
  繰り返しの条件;
  カッコが終わった後にすること・繰り返しの条件が終わるようにする
) {
  // 処理
}
```

正確に説明する場合は以下のようになります。

```php
for(
  ループ前に一度だけ実行される(主に"変数の初期値"に使われる);
  ループ毎に処理を行う前に実行され真であれば処理を行う (主に"繰り返しの条件"に使われる);
  ループ毎に処理が完了された後に実行される (主に"繰り返しの条件の変数更新"に使われる) 
) {
  // 処理
}
```

【for(これ;これ;これ)】は一般的には、ループの「初期値」「条件」「条件変数の更新」を記述するところではありますが、実際には「**あるタイミングで処理を実行する**」というのが正確な理解です。したがって省略したりループとは無関係な処理を行うこともできます。実際にそのような使い方をしている例もあります。しかしながらあまりにも無関係な処理を書くとコードを理解するのが難しくなるため 【for(これ;これ;これ)】は「初期値」「条件」「条件変数の更新」として使うのが本来意図された利用方法です。

【for(これ;これ;これ)】を「初期値」「条件」「条件変数の更新」と理解するのは勘違いというわけではありませんが正確に理解しているとはいえません。慣れないうちは正確に理解していなくても十分ですが、正確に理解すると応用範囲が広がり、プログラミング言語やライブラリというのは、最初に理解した以上の使い方ができるように柔軟に設計されていることに気がつくでしょう。最終的には正確に理解することを目指してください。
