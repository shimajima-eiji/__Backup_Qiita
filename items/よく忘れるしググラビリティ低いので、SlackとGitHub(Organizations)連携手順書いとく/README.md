書き出せばシンプルなんだけど、知らないと結構ハマる話。

## 1. SlackにGitHub botを入れる
`https://(Your Workspace).slack.com/marketplace/search?q=github`

で、インストール。
この時点では、SlackでGitHubにつなげるようにしただけなのでまだやることがある

## 2. SlackのGitHub botに監視するリポジトリを指定する
```
/github subscribe (Your organizations)/(Repository)
```

必要な数だけ実行

### 2.1. Organizationsで実施する場合
既にアプリを入れてしまったので正攻法ではできない。
そのため、GitHub側からSlackBotを入れるようにする

`https://github.com/organizations/(Your organizations)/settings/reminders`


あとは権限とか見直しつつ、ガチャガチャやれば疎通確認できるはず
少なくとも、筆者の環境では投稿時点では動いていることを確認している
