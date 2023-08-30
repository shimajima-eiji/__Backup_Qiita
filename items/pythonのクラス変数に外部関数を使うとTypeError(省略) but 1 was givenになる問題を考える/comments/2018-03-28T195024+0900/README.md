外部関数を組み込む意図がわかりませんが、やるなら静的メソッドとして放り込むのでは？

```python
def _outer():
    return 'outer'

class Inner:
    outer = staticmethod(_outer)

    def call_outer_function(self):
        print(self.outer())

Inner().call_outer_function()
```
