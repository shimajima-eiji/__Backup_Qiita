
publishで更新する処理はCIでいうところの

```
- uses: increments/qiita-cli/actions/publish@v1
  with:
    qiita-token: ${{ secrets.QIITA_TOKEN }}
    root: "."
```

が実行しているからでは？という疑問
単純にローカルからnpx qiita pushだとどうか？
