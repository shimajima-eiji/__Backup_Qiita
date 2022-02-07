mapはデータを作り出すもので、printに対して使うのは良くないと思うのですがいかがでしょう？

```py:一番下が生成されたリスト
>>> list_in_list = [['1A','1B','1C'],['2A','2B'],['3A','3B','3C','4D']]
>>> list(map(lambda lists:list(map(print, lists)) , list_in_list))
1A
1B
1C
2A
2B
3A
3B
3C
4D
[[None, None, None], [None, None], [None, None, None, None]]
```

sumを使ってフラット化したリストを作ってからprintする方がまだマシな気がします。

```py:フラット化したリストを作ってからprint
>>> list_in_list = [['1A','1B','1C'],['2A','2B'],['3A','3B','3C','4D']]
>>> print(*sum(list_in_list, []), sep='\n')
1A
1B
1C
2A
2B
3A
3B
3C
4D
```

itertools.chainを使う方がより良いと思います。

```py
>>> from itertools import chain
>>> list_in_list = [['1A','1B','1C'],['2A','2B'],['3A','3B','3C','4D']]
>>> print(*chain(*list_in_list), sep='\n')
1A
1B
1C
2A
2B
3A
3B
3C
4D
```

多重リストのフラット化は こちらも参考にしてみてください。
[pythonでflatten - Qiita](https://qiita.com/shiracamus/items/fb85943ed34d5ec09c4f)
