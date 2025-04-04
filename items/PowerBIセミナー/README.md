## 本日のセミナー・イベント
デモデータだとは思うが、特定できる情報を書いているので非公開としたい。

### 凡例
筆者注による

:::note
講師から口頭による補足・ポイントなど
:::

:::note warn
考察・理解したこと
:::

## ハンズオン
かなり丁寧にご説明いただいていたため、手順をまとめる

### PowerBIを起動
事前に配布された資料を開く

### データが読み込めているか確認する
カラム：データ・画面右側
（このタイミングで保存作業もやってる）

:::note
PowerBIは自動保存機能がないため、こまめに保存しよう
:::

### データを閲覧する
ボタン：テーブルビュー・画面左側

### データ項目を追加する
リボン：「テーブルツール」より新しい列を追加

### 作成した列に関数を入力
```
滞在時間 = MINUTE([退店時刻] - [入店時刻])
```

:::note warn
凡例： `列名 = MINUTE([列名] - [列名])`かな？
:::

:::note
Excelだとわざわざヘッダー列を作って列名を作り、以下関数を書いていくが、上記コードのように書くと列全体に対して適用できる。列名もこのタイミングで設定している
:::

### 項目を追加（上の手順を再度）
```
利益 = [販売価格] - [仕入価格]
```

### 新しいメジャーを作成
リボン：「ホーム」より新しいメジャーをクリック
入力欄に以下を入力

```
平均滞在時間 = AVERAGE('売上データ管理'[滞在時間])
```

列ではなく、メジャーとして作成される。

:::note warn
変数（列名）を指定する場合、`'テーブル名'[列名]`で別テーブルを参照できる。テーブルに
:::

### 更に新しいメジャーを作成
```
売上利益 = SUM('売上データ管理'[利益])
```

### 同じく
```
COUNTROWS(FILTER('売上管理テーブル',[分類] == 'おにぎり'
```

:::note warn
レポートビューで表示させるために、分析したいデータ列とメジャーを作成したのかな？
:::

### レポートビューに戻る
ボタン：レポートビュー・画面左側

## ハンズオン・ダッシュボードを作る
Webサイトを作るのと同じ要領でできそう

:::note warn
表示項目についてはあらかじめテーブルビューの項目名から表示できるように指定しておく必要がありそう
:::

### ページ設定
レポートページの書式設定
キャンバスの背景から背景を変えてみよう。透過性は０％に（デフォルトで100%？）

:::note
Webサイトをノーコードで作成できるツール（ブロックエディタ）のような要領で作っていくのがいいかも
画面をみながらGUIでいじれる
:::

### 画面にチェックボックスを作る
視覚化カラム・ビジュアルのビルド→スライサー

ここでは年齢のみ指定

### 画面に表示項目を作る
視覚化カラム・ビジュアルのビルド→カード

ここでは売上利益のみ指定

### 
視覚化カラム・ビジュアルのビルド→円グラフ

ここでは滞在時間を指定

### 
視覚化カラム・ビジュアルのビルド→折れ線グラフ

ここではおにぎり・ホットスナック・弁当列名を指定
