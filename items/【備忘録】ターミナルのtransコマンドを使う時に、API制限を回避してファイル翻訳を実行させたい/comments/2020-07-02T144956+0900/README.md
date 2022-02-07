`/bin/sh`(dash)でランダム

```sh
$ echo scale=0\;`< /dev/urandom tr -dc 0-9|fold -12|head -1`%5+5|bc -l
9
```

あと`input`と`output`は`input="$1"`と`output="$2"`みたいにコマンドライン引数にしたいですね。
