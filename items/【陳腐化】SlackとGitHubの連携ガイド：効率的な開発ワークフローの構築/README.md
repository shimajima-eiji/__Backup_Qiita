開発チームの効率を高めるために、GitHubからの通知をSlackで受け取るための連携設定方法を解説します。これにより、コードの変更やプルリクエスト、イシューなどの重要な情報をチームのコミュニケーションハブで確認できるようになります。

### 1. SlackにGitHub Appをインストールする
まず、SlackワークスペースにGitHub Appをインストールします。

以下のURLにアクセスします：
https://<あなたのワークスペース>.slack.com/marketplace/search?q=github

検索結果から「GitHub」アプリを選択し、「Slackに追加」ボタンをクリックします。
必要な権限を確認し、「許可する」をクリックしてインストールを完了します。


注意: この段階では、SlackとGitHubの接続が確立されただけであり、まだ特定のリポジトリからの通知は設定されていません。

2. 監視対象のリポジトリを設定する
2.1 個別リポジトリの購読設定
通知を受け取りたいSlackチャンネルで以下のコマンドを実行します：
/github subscribe <組織名>/<リポジトリ名>
例：
/github subscribe microsoft/vscode
複数のリポジトリを監視したい場合は、それぞれのリポジトリに対して同じコマンドを実行します。
2.2 GitHub Organizationレベルでの設定
すでにSlackアプリをインストールしている場合は、GitHub側から連携を設定できます：

GitHub Organizationの設定ページに移動します：
https://github.com/organizations/<組織名>/settings/reminders

「Create reminder」ボタンをクリックします。
Slackワークスペースとチャンネルを選択し、通知を受け取りたいイベントタイプやリポジトリを指定します。
「Create reminder」をクリックして設定を完了します。

3. 通知のカスタマイズ
特定のイベントタイプのみを購読するには、以下のようにフィルターを追加できます：
/github subscribe <組織名>/<リポジトリ名> [issues|pulls|deployments|statuses|commits|releases]
例えば、プルリクエストとイシューのみを購読するには：
/github subscribe microsoft/vscode issues,pulls
4. 動作確認
設定が完了したら、以下のいずれかの方法で動作確認ができます：

テスト用のイシューを作成する
既存のプルリクエストにコメントを追加する
リポジトリに小さな変更をプッシュする

正しく設定されていれば、対応するイベントの通知がSlackチャンネルに表示されるはずです。
