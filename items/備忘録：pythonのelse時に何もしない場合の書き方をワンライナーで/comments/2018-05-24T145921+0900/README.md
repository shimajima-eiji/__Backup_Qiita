> この例から、message = message or 'no message'　のような形で変数に格納していますが、変数に値がない場合のみ変数に値を格納する処理を実行したい、という場合だとまた違うケースになりますでしょうか。

注意が必要です。
message に 'no message' が代入されるのは、message が None, False, 数値の0(0, 0.0, 0+0j), 空文字列・空配列・空集合('', [], (), {}) のときです。boolに変換するとFalseになる値たちです。
値が空文字列や数値0のときも「値がない」としていいのであれば正しく動作しますが、None のときだけ「値がない」としたいときなどはif文や条件式（俗にいう三項演算子）で書かないといけません。

```py
>>> bool(None)
False
>>> bool(0)
False
>>> bool('')
False
>>> bool('0')
True
>>> bool([])
False
>>> bool([''])
True
```
