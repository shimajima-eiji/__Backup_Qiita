# QiitaCLIを使ってQiitaのWebエディタで書いた記事も丸ごとGitHubでバックアップ・管理する方法

## 結論
Qiitaの記事をGitHubでバックアップ・管理するには以下のコマンドを実行します：

```bash
npx qiita pull
git add -A
git commit -m "qiitaバックアップ"
git push
```

GitHub Actionsで定期実行すれば、自動的にバックアップを取得できます。

## 詳細解説

### QiitaCLIとは？

QiitaCLIはQiitaが提供する公式のコマンドラインツールで、ローカル環境からQiitaの記事を作成・編集・管理することができます。Webエディタだけでなく、お気に入りのエディタやIDEを使った記事作成をサポートしています。

### セットアップ手順

1. **準備するもの**
   - GitHubアカウント
   - Node.js環境（npxコマンドを使用するため）
   - Qiitaアカウントとアクセストークン

2. **初期設定**

   ```bash
   # プロジェクトフォルダの作成
   mkdir qiita-backup
   cd qiita-backup
   
   # Gitリポジトリの初期化
   git init
   
   # QiitaCLIの初期設定
   npx qiita init
   ```

   `qiita init`実行時に必要な情報：
   - Qiitaのアクセストークン（Qiitaの設定ページから取得）
   - ユーザー名
   - その他の基本設定（プロンプトに従って入力）

3. **GitHubリポジトリとの連携**

   GitHubで新しいリポジトリを作成し、ローカルリポジトリと連携します。

   ```bash
   git remote add origin https://github.com/あなたのユーザー名/リポジトリ名.git
   ```

### 記事のバックアップ方法

1. **手動でバックアップする場合**

   ```bash
   # Qiitaから記事を取得
   npx qiita pull
   
   # 変更をコミット
   git add -A
   git commit -m "qiitaバックアップ"
   
   # GitHubにプッシュ
   git push origin main
   ```

2. **GitHub Actionsで自動化する場合**

   リポジトリのルートに `.github/workflows/backup.yml` ファイルを作成します：

   ```yaml
   name: Qiita Backup

   on:
     schedule:
       - cron: '0 0 * * *'  # 毎日午前0時に実行
     workflow_dispatch:      # 手動実行も可能

   jobs:
     backup:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Setup Node.js
           uses: actions/setup-node@v3
           with:
             node-version: '16'
             
         - name: Fetch Qiita articles
           run: npx qiita pull
           env:
             QIITA_TOKEN: ${{ secrets.QIITA_TOKEN }}
             
         - name: Commit changes
           run: |
             git config --global user.name 'GitHub Actions'
             git config --global user.email 'actions@github.com'
             git add -A
             git diff --quiet && git diff --staged --quiet || git commit -m "Automatic backup of Qiita articles"
             
         - name: Push changes
           uses: ad-m/github-push-action@master
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             branch: ${{ github.ref }}
   ```

   **注意事項：** GitHub ActionsでQiitaのアクセストークンを使用するには、GitHubリポジトリの「Settings」→「Secrets and variables」→「Actions」でシークレット変数 `QIITA_TOKEN` を作成し、Qiitaのアクセストークンを設定してください。

### QiitaCLIの便利な機能

- **記事の一覧取得**: `npx qiita list`
- **新規記事の作成**: `npx qiita new 記事のファイル名`
- **記事のプレビュー**: `npx qiita preview`
- **記事の投稿**: `npx qiita publish 記事のファイル名`

### バックアップの活用方法

GitHub上でバックアップした記事は以下のように活用できます：

1. **バージョン管理**: 記事の変更履歴を追跡できます
2. **ブランチ機能**: 実験的な内容を別ブランチで作成可能
3. **コラボレーション**: Pull Requestを使った共同編集
4. **バックアップ**: Qiitaのサービスに依存せず記事を保存

## まとめ

QiitaCLIとGitHubを組み合わせることで、Webエディタで書いた記事も含めてQiitaの全記事を効率的にバックアップし管理できます。GitHub Actionsによる自動化で、定期的なバックアップも簡単に設定できるため、大切な技術記事を安全に保存しながら効率的に管理できます。

初期設定に少し手間はかかりますが、一度設定してしまえば自動的にバックアップが取得されるので、技術記事を書く方には非常におすすめの方法です。
