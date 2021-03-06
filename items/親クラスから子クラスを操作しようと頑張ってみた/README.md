オブジェクト指向の良さが活かせない私がハマるポイントです…
今回はPython2系で。

# やりたいこと
- Baseクラスで宣言したものをそれぞれのクラス間で使えるようにしたい
- 親クラスで子クラスを管理したい
→そもそもこのアプローチが既に設計レベルで問題な気もしますが…

ちょっと考えてみました。

# クラスの中にクラスを作ってみる方法

``` inbound_class.py
class Base:
  def __init__(self, arg):
    self.arg = arg
    self.hoge = self.Hoge(arg)
    self.fuga = self.Fuga(arg)

  def print_classname(self, string)
    print self.arg, string

  class Hoge:
    __hoge_var = 'hoge'
    def __init__(self, arg):
      self.arg = arg
    def print_classname(self)
      print self.arg + __hoge_var

  class Fuga:
    __fuga_tuple = ['fuga']
    def __init__(self, arg):
      self.arg = arg
    def print_classname(self)
      print self.arg + __fuga_tuple[0]

print Base('test').hoge.print_classname()

# クラスを継承する方法

``` inheritance.py
class Base:
  def __init__(self, arg):
    self.arg = arg
    self.hoge = self.Hoge(arg)
    self.fuga = self.Fuga(arg)

class Hoge(Base):
  __hoge_var = 'hoge'
  def __init__(self, arg):
    self.arg = arg
  def print_classname(self)
    super().print_classname(self.arg + __hoge_var)

class Fuga(Base):
  __fuga_tuple = ['fuga']
  def __init__(self, arg):
    super().__init__(arg)
  def print_classname(self):
    super().print_classname(self.arg + __fuga_tuple[0])

print Base('test').hoge.print_classname()
```

# 課題
なんとなくやりたい事は伝わればいいんですが、要は同じ要素をそれぞれの子クラスに入れるんじゃなくて、親クラスに入れて子クラスからもそれぞれに呼べるようにしたい、と。
そういう話なんですが、こういう事をやる場合はdefだと上位の階層に変数を定義するとか、classだとselfとかが使えますね。

とはいうものの、上記コードはエラーになります。
正直、この辺り（やりたい事は上記、ただし実装をどうすれば良いか、よく分からなかっていない）でいつもdefをネストして作っています。
defのネストも好きじゃないのでやりたくないんですが、こちらの方が直感的というか、とりあえず動くものが出来るんで扱いやすいんですよね。
このコードもclassをdefに変えてメソッドのselfを消したら期待した通りに動くものになります。
defでネストしまくればやりたい事は実現できていますが、あまりにもスマートからかけ離れていることと、見やすくするためだけにdefを使っている面があるので、あんまり良い使い方・作り方ではありません。
