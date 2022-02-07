```python
from itertools import chain

ll1 = [['1A', '1B', '1C'], ['2A', '2B'], ['3A', '3B', '3C', '4D']]
list(
    map(print, chain(*ll1))
)
```
