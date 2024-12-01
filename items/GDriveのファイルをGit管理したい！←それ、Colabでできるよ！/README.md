:::note warn
先に結論を書きますが、ColabでやるよりGDrive Sync的なアプリを入れて同期しつつローカルでgitコマンド使う方法が一番楽です
:::

## 手順
### 1. いつも通りColabを開く
これからコマンドを打ち込んでいくのでどこでも良いですが、新規作成した方がいいかも。

https://colab.research.google.com

せっかくなので「Colab-GitHub連携.ipynb」とでも言っておきますが、ファイル名に意味はありません。

### 2. GDriveをマウントする
実行後、ファイルツリーにdriveが追加されれば完了（セキュリティレベルにより外部設定が必要）

```
# Refer: 
# コマンドで操作できるように、GDriveをColabのファイルシステム上にマウントする。
# 実行後、ファイルツリーにdriveが追加されれば完了（セキュリティレベルにより外部設定が必要）
from google.colab import drive
drive.mount('/content/drive')
```

後で振り返れるように、コードコメントにも残しておきます。

## 

## 別解
Sync GoogleDriveみたいなアプリを使ってローカル上からgitコマンドを実行するのとやっていることは同じです
