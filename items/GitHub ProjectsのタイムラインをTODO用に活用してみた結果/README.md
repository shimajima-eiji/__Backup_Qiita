
## 運用中
https://github.com/users/shimajima-eiji/projects/8

## GitHub ProjectsでリッチなTODO管理がしたい
これが今日の本旨。
あくまで個人タスクのTODO管理をするぐらいの目標だったが、しっかりと運用すれば小規模なプロジェクト管理程度ならGitHubで完結できそう。
今期ではプロジェクト管理やナレッジ管理はJIRAやnotionを活用していたが、これをGitHub ProjectsやGitHub Wikiで完結していくことを目標にしたい。

### 脱線・現実的な話としてGitHubだけで完結できるのか？
難しいと思われる。
多くの場合プロジェクト管理ツールは使い方を覚えるのが大変なので結局Excel神話になったり、GitHub Wikiはナレッジ管理として使うには機能面に不満がある。
なんなら、GitHub WikiはユースケースによってはGitHub Discussionsが競合になるので、似たような機能があることで運用が分かりにくくなる事もよくはない。
細かいことをいうと、GitHub Wikiはプライベートリポジトリでは（無料のため）使えない。

## 仕様確認： GitHub ProjectsのタイムラインとリポジトリのIssue/Milestoneとの関連
まず、タイムラインの仕様を確認してみよう。
運用中のプロジェクトからスクリーンショットを公開する

### ゲストから閲覧できる画面
![GitHubProject_public.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/0f7f9c72-838f-0bcc-c4b4-1b51447e3964.png)

### 管理者から閲覧できる画面（個人プロジェクトだが見せられないものが入ってるので一部のみ）
![GitHubProject_private.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/0e7626ed-4019-ca57-e0ad-c2638f5fdf9c.png)

### 公開状況
まず、大事なのはゲストと管理者の公開内容が異なるという点に注目する。
そもそも、運用中の本プロジェクトはゲストに公開する前提で作成しているため、この運用方法は実際のプロジェクトの管理方法として運用する上で問題があるが、今回は仕様に注目するためご容赦願いたい。
せっかくなので、if文の構造のように捉えてもらうと良い

- if: ゲストユーザーである
  - if: プロジェクトがpublicである
    - if: Issueがpublicなリポジトリで起票されたものである
      - （※後述）
    - else:
      - Issueがあることは分かるが、内容は表示されない（You can't see this item）
  - else:
    - プロジェクトが見つからない
- else:
  - 管理者または権限のあるユーザーは全部見れる
  - （※後述）

このことから、以下のように考える事ができる

- プロジェクトへのアクセス権限： プロジェクトがprivateである場合、「プロジェクト」に招待されていないユーザーはアクセスできない
- リポジトリへのアクセス権限： プロジェクトがpublicでも、リポジトリがprivateである場合、「当該リポジトリ」に招待されていないユーザーはアクセスできない

の、二重の権限設定が必要

#### （※後述） タイムラインに反映される項目
ここからは、画面に対応する項目のマッピングである

- 画面左の項目名: Issueタイトル名
- ⭐︎タイムライン上の項目名: Issueタイトル名
  - うまく活用すると色々できそうだが、設定が面倒くさいので１日のみ表示で統一
  - タイムラインに置くとしたら開始日か、複数のマイルストーンで一覧できなくなった場合はマイルストーンの締日に置いて何のタスクが終了するのか見えるようにした
- タイムラインの緑の線とタイトル: Issueに紐づいたマイルストーンの締日と、マイルストーン名
  - Issueをクローズしてもマイルストーンはクローズされないので、定期的なメンテナンスが必要

タイムライン上への表示だけ設定がいるが、正直あまり使ってないのでいらないかもしれない
ただし、複数のマイルストーンの終了日が同じ日にバッティングすると一覧上ではまとめられてしまうため、マイルストーン名を参照したい場合は注意。
同一マイルストーンを複数のIssueに付与した場合は問題ない

### 運用上の課題
- どのリポジトリにIssueを書くか気にする必要がある
  - Projectの仕様として、リポジトリを横断する事ができる
  - リポジトリに対して紐づける場合は気にしなくて良いが、今回は公開タスク・非公開タスクを一元管理したい
  - 公開範囲が違う場合は慎重な運用が必要。非公開にしなくてもいいタスクを非公開リポジトリに書く事も
- Issueをクローズしても、プロジェクトのタイムライン上にも残るし、全てのIssueをクローズしてもマイルストーンはクローズされない
  - これも結構手間。JIRAとかRedMineの方が使いやすい
  - 対策として、クローズしたIssueはProjectからアーカイブするし、1マイルストーン1Issueの運用を徹底して、一つのマイルストーンに複数のIssueがない状態を担保
    - そもそも運用方針としてどうかと思うが、Issueを親と子に分けて、親だけマイルストーンを設定し、サブタスクは親Issueを見れば分かるようにしている
    - サブタスクを書く時は `- [ ] タスク名`の形式を採用。タスク名部分はプレフィクスつけたり文字列検索しやすいようにする
    - 親Issueを横断したい場合、サブタスク専用のラベルをつけてもよい
    - 軽微なサブタスクはIssue化しない、親Issueから独立できるほど重たいサブタスクはIssue化する
      - ただし、コントリビューションをつけたいので一律でIssue化しておく。親Issueは起票日をつけてラベルで管理する
      - 検索時は親Issue専用のラベルで確認し、古い日付のタスクを優先して片付けたり、親Issueから切り離したり、クライアントの回答待ちなど自分でどうしようもない状態になったら申し送り用のIssueを作ってこれもタイムライン化するために専用のマイルストーンを作る

JIRAなどのツールの使い方を覚える時にも感じた問題をGitHub Projectにも感じている。
このような仕様の問題はあまりにも特殊すぎて学習コストも運用コスト、そしてリカバリが必要になりそうなので本格的に導入はできないな、というのが所感だ。

## また一つ賢くなった
と、思う事にする。
バッドノウハウはうまく行かない方法だと、切り捨てられがちだが、バッドノウハウも集めればしっかりとした学びになるので、失敗したから失敗だと思わず「いくつもある成功しないパターンを一つ見つけた」と発見ごとのようにとらえるとプラスの学びになる。
今回は「しくじり」として投稿したが「しくじり」というよりは「うまく行かない方法を見つけた」という発見を共有した。
ぜひ、あなたの「うまく行かない発見」を共有していただきたいと願う。
