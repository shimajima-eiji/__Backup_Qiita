クラスにしてみたり

```pycon
>>> class String(str):
...     def insert(self, index, insertee):
...         return self[:index] + insertee + self[index:]
... 
>>> String('test').insert(2, '--hoge--')
'te--hoge--st'
```
