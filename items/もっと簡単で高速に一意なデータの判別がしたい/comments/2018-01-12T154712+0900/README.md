こんな感じですかね。

```python:
cache = set()
while True:
    try:
        num = int(raw_input('input num: '))
        if num in cache:
            print '登録済み'
        else:
            cache.add(num)
            print '登録しました'
    except ValueError:
        pass
    except EOFError:
        break

print cache
```

---
> 例ではprintで濁していますが、順番を気にし始めるとややこしくなりそうな気がしました。以下サイトも参考にしてやってみます。

順序を気にするのなら組み込み辞書も不適かと。

---
> ご指摘のTrue/Falseはif notを使わないように配慮したのと、== Falseを書いて== Trueを書かないのが気持ち悪く感じたぐらいです。

複合的な条件ならまだしも、単項の条件式でnotを使いたくないというのはよく分かりません。
どうしてもnotを使いたくないのなら、処理の順序を逆転させればよかったのでは。

```python
def uniq(target):
    if cache.has_key(target):
        return True
    else:
        cache[target] = target
        return False
```

個人的には可読性以上に、無駄な比較が生じることが気になります。

```
(Python27)>python -m timeit "True"
10000000 loops, best of 3: 0.0255 usec per loop

(Python27)>python -m timeit "True == True"
10000000 loops, best of 3: 0.0581 usec per loop
```

---
[直前の記事](https://qiita.com/nomurasan/items/492e10e3a534eae8fca1)も拝見しましたが、Python3.xならば[functools.lru_cache](https://docs.python.jp/3/library/functools.html#functools.lru_cache)で解決しそうな内容ですね。

引数がハッシュ可能である必要があるのでリストは放り込めませんが...
引数に破壊的な操作をしなくて良いのであれば、タプルにしてしまえばよいかと。
