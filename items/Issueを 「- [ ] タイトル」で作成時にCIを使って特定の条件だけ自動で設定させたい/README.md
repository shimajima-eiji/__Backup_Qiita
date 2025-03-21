# 発端・記事
https://qiita.com/private/a851656aa390e1be60b2

## ポイントのみ解説
疲れた

自分用メモに残すが、後で見直した時にAIにコードをぶん投げそうなので、そんな手間を掛けなくてもいいように準備するところまでをゴールにする。

### PATにrepoとproject権限が必要
Personal Access Token(PAT)の設定が必要。2種類の権限を作って使い分けるか、まとめて使えるものを用意しよう。

PATの設定は、GitHubアカウントにログインして以下を開く
https://github.com/settings/tokens

権限設定は以下の通り

- repo
  - Issue自体を書き換えるため必要。具体的にはラベル・マイルストーン・プロジェクト欄
  - ただし、プロジェクトはrepoだけではダメ
- project
  - GitHub APIを使用するため。projectはrepoに紐づかないので別権限が必要

### プロジェクト固有のIDを取得するスクリプトを用意する
- YOUR_PAT_REQUEST_READ_PROJECT: 前段で作成したもの
- YOUR_USERNAME: GitHubアカウント名
- YOUR_PROJECT_NUMBER: 
  - `https://github.com/users/(YOUR_USERNAME)/projects/(ここ)`

``` command.sh
curl -H "Authorization: bearer YOUR_PAT_REQUEST_READ_PROJECT" \
-H "Content-Type: application/json" \
-X POST \
-d '{"query": "query { user(login: \"YOUR_USERNAME\") { projectV2(number: YOUR_PROJECT_NUMBER) { id } } }"}' \
https://api.github.com/graphql
```

PVT_から始まるprojectV2が取れる

``` result.json
{"data":{"user":{"projectV2":{"id":"PVT_hogefugapiyo"}}}}
```

PATもPVT_も後で使うのでなくさないように。

### CIで使えるようにシークレット変数に登録（順不同）
1. repo権限を持つPAT（先ほど作成済）
2. read-project権限を持つPAT（先ほど作成済）
3. PVT_hogefugapiyo（先ほど取得済み）

を登録する。
ここでは説明を簡略化するため、1.2.をまとめて設定しておく
（以下コードでいう `YOUR_PAT_WITH_PROJECT_SCOPE` と `PROJECT_NODE_ID` にそれぞれ格納した）

### CIを書く
書いたコードをAIに丸投げしてコメントを追記後、手直ししている

``` for_advent-calendar.yml
# このファイルは、GitHub Actionsのワークフローを定義しています。
# GitHub Actionsは、GitHubリポジトリ内で自動的にタスクを実行するための機能です。

name: Issue Automation for アドベントカレンダー  # このワークフローの名前

# このワークフローがいつ実行されるかを定義
on:
  issues:
    types: [opened]  # Issueが作成されたり編集されたときに実行

jobs:  # 実行されるジョブの定義
  automate_issue:  # ジョブ名
    runs-on: ubuntu-latest  # このジョブが実行される環境（ここではUbuntu最新版）
    steps:  # ジョブ内で実行される一連のステップ
      - name: Automate Issue  # このステップの名前
        env:  # 環境変数の設定
          # これらの変数は、GitHubの機密情報やIssueの情報を含んでいます
          GITHUB_PAT: ${{ secrets.YOUR_PAT_WITH_PROJECT_SCOPE }}  # GitHub Personal Access Token。前段の作業でやったもの
          ISSUE_TITLE: ${{ github.event.issue.title }}  # Issueのタイトル
          ISSUE_NUMBER: ${{ github.event.issue.number }}  # Issueの番号
          ISSUE_ID: ${{ github.event.issue.node_id }}  # IssueのID
          PROJECT_ID: ${{ secrets.PROJECT_NODE_ID }}  # プロジェクトのID。これも前段の作業で格納したもの
        run: |  # 実行するシェルスクリプト
          # Issueのタイトルが「adcal」で始まるかチェック
          if [[ "$ISSUE_TITLE" == adcal* ]]; then
            echo "Issue title matches the condition. Proceeding with automation."
            
            # 「アドカレ」ラベルを追加。今回は決め打ちだが、シークレットに入れておくと使い回しが楽
            # curlコマンドを使用してGitHub APIにリクエストを送信
            label_response=$(curl -s -X POST \
              -H "Authorization: token $GITHUB_PAT" \
              -H "Accept: application/vnd.github.v3+json" \
              "https://api.github.com/repos/${{ github.repository }}/issues/$ISSUE_NUMBER/labels" \
              -d '{"labels":["アドカレ"]}')
            echo "Label response: $label_response"
            
            # 「マイルストーンID:1」のマイルストーンを設定。本当はここもシークレットにすべきだね
            # 同様にcurlを使用してマイルストーンを設定。
            milestone_response=$(curl -s -X PATCH \
              -H "Authorization: token $GITHUB_PAT" \
              -H "Accept: application/vnd.github.v3+json" \
              "https://api.github.com/repos/${{ github.repository }}/issues/$ISSUE_NUMBER" \
              -d '{"milestone":1}')
            echo "Milestone response: $milestone_response"
            
            # Issueをプロジェクトに追加
            # GraphQL APIを使用してIssueをプロジェクトに追加
            project_response=$(curl -s -X POST \
              -H "Authorization: bearer $GITHUB_PAT" \
              -H "Accept: application/vnd.github.v3+json" \
              -H "Content-Type: application/json" \
              https://api.github.com/graphql \
              -d "{\"query\":\"mutation {addProjectV2ItemById(input: {projectId: \\\"$PROJECT_ID\\\" contentId: \\\"$ISSUE_ID\\\"}) {item {id}}}\"}")
            echo "Project response: $project_response"
            
            echo "Issue #$ISSUE_NUMBER has been automated for アドカレ"

          # Issueのタイトルが「adcal」で始まらない場合。通常のIssueのケースなのでエラーではない。そもそも何もしなくていいんだけど、今回はみやすさのため追加
          else
            # Issueのタイトルが条件に一致しない場合のメッセージ
            echo "Issue #$ISSUE_NUMBER does not start with アドカレ. No automation applied."
            echo "Issue title: $ISSUE_TITLE"
          fi
```

コマンドの部分が面倒臭い。
全部curlを使ってGitHub APIを叩いている。
通常通りIssueを追加するだけならIssue_template.mdなりを使えばいいんだけど、今回は `- [ ] タイトル` からconvert to issueにするのでこの方法は使えない

## 運用：GitHub ProjectでIssueをリポジトリ横断で管理したい
:::note alert
Issueテンプレートを使いたかったので、結果的に`- [ ] タイトル`での運用をやめた
:::

:::note
Issueを作成する時にCIを実行するという要件は満たせているため、無駄ではない
:::

実は本稿は記事を公開する前（9/21）に下書きで置いていたのだが、我ながらめちゃくちゃ有用だな、と思った（試験運用しようと思って、思い出すために何度も開いた）ので、個人でもGitHub Issueでチケット運用する場合は一時的にブックマーク・後で読むに入れておくことをお勧めする。

### ユースケースを考える

#### 仕様を知る
- プロジェクト自体へのアクセス権限を設定できる
- リポジトリ（Issue）へのアクセス権限を設定できる
- パブリックなプロジェクトにクローズドなリポジトリのIssueを登録しても、リポジトリへのアクセス権限がなければIssueは見れない
  - Issueがあることは公開権限がなくてもわかる

（この項目を書いている日付も特定できるが、気にせず公開する）
https://github.com/users/shimajima-eiji/projects/8/views/1

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/76b94d2f-f2cc-028c-1f24-9ba4ced04250.png)

見直してみると「Issueを書くリポジトリを間違えたな」と思う事もあるので、リポジトリ別に見れた方がいいね。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/be7f50bf-7135-acb3-649a-0cf33cc45099.png)

というわけで、作った。
いい感じだ。

#### 運用
運用目線で、繰り返しになるが公開範囲を確認しておく

- 公開したいIssueはパブリックなroadmapリポジトリ
- 日報はプライベートなdiaryリポジトリに書いているとする
- プロジェクト自体はオープン（誰でも見れる）

Issueを全体公開をするためには、２段階の公開設定をしておく必要があるので安心だ。
なお、日報は一日ごとに#を書かれるしプライベートな内容を書き込む可能性が高い。
roadmapにはプライベートな内容を書くことはない、とする

### 運用を意識した実装
まず、Issue自体にはより複雑な内容を埋め込みたいので、メンテナンス性を高めるために`.github/ISSUE_TEMPLATE/name.md`と組み合わせることにする。

``` .github/ISSUE_TEMPLATE/name.md
ここに色々書いていく。今回はメイン
```

これをCIと組み合わせる。特にテンプレートではプロジェクトを追加できない。
（ラベルとマイルストーンはリポジトリに依存するのでできる）
ここで想定する運用要件として、Issueをプロジェクトに追加するとリポジトリを横断できるという強みがあるので積極的に活用していく。

``` command.shからPVT_だけ取得する.sh
PROJECT_NODE_ID=$(curl -H "Authorization: bearer YOUR_PAT_REQUEST_READ_PROJECT" \
-H "Content-Type: application/json" \
-X POST \
-d '{"query": "query { user(login: \"YOUR_USERNAME\") { projectV2(number: YOUR_PROJECT_NUMBER) { id } } }"}' \
https://api.github.com/graphql \
| jq -r '.data.user.projectV2.id')
```

として、変数で受け取れるようにしておくと捗る。
が、AIに聞いたところ、こんな事をしなくてももっと楽な方法で構築できるらしい

``` yml
# TITLE_PATTERN: 対象となるIssueのタイトルのパターン（正規表現）
# PROJECT_NUMBER: 対象となるプロジェクト番号
# ADD_TO_PROJECT_PAT: repoとproject権限があるもの

name: Issueをプロジェクトに追加

on:
  issues:
    types: [opened]  # デバッグするならeditedを入れると楽

jobs:
  add-to-projects:
    runs-on: ubuntu-latest
    steps:
      - name: Issueのタイトルをチェック
        id: check_title
        env:
          TITLE_PATTERN: ${{ secrets.TITLE_PATTERN }}
        run: |
          TITLE="${{ github.event.issue.title }}"
          if [[ $TITLE =~ $TITLE_PATTERN ]]; then
            echo "PROCESS_ISSUE=true" >> $GITHUB_OUTPUT
            echo "REPORT_DATE=$(echo $TITLE | awk '{print $2}')" >> $GITHUB_OUTPUT
          else
            echo "PROCESS_ISSUE=false" >> $GITHUB_OUTPUT
          fi

      - name: プロジェクトにIssueを追加
        if: steps.check_title.outputs.PROCESS_ISSUE == 'true'
        uses: actions/add-to-project@v0.5.0
        with:
          project-url: https://github.com/users/${{ github.event.issue.user.login }}/projects/${{ secrets.PROJECT_NUMBER }}
          github-token: ${{ secrets.ADD_TO_PROJECT_PAT }}

      - name: 処理結果を記録
        if: steps.check_title.outputs.PROCESS_ISSUE == 'true'
        run: |
          echo "日報 ${{ steps.check_title.outputs.REPORT_DATE }} を各プロジェクトに追加しました。"

      - name: 処理をスキップ
        if: steps.check_title.outputs.PROCESS_ISSUE == 'false'
        run: echo "Issueのタイトルが指定されたパターンと一致しません。処理をスキップします。"
```

これは便利！

## 【追記】運用所感
この記事の下書き自体はかなり早い時期に書き上げていて、その後運用していて色々な気付きがあったが、まとめきれていないので現行版でGoとした
落ち着き次第、続報を書きたい
