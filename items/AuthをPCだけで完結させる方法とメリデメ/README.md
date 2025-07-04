今はEnte Authの方がいいよ！というアドバイスをZennでいただいており、実際に使ってみたんですがすごくいい！

https://zenn.dev/nomuraya/articles/e7bb03c717793a7c8b70#comment-f48ba7d7e486f3

（マルチポストというよりはブラッシュアップ版をZennに置いて再検証した、というのが事実です）

Ente Authの導入編の記事を書こうかと思っているぐらいです。
こうご期待。

![扉絵バナーとして使える横長画像（16_9.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/122800/32dcd796-419f-4725-9511-1e4329beeb6a.png)

## お詫び・注意喚起
設定ミスって投稿が遅れました。
前日に記事を書くボタンから記事作成　→　当日に非公開設定で投稿しても、アドベントカレンダー側には関連付けがされないためご注意ください。

## 対象読者
:::note alert 
業務で絶対に使用しないようにしてください
また、業務で使用する端末（リモートワーク含む）への導入は厳禁です
:::

:::note warn
本稿は内容が過激であるため、以下の通り制限している旨を周知いたします。

- セキュリティリスクを学びたい方（＝本稿の作業はやらない方）
- 本稿の内容または類似したもので作業を実施した際は自己責任で行え、かつ関連記事の投稿者に責任追及しない方
- 本稿の以下を閲覧した時点で、注意書きの全内容を理解し同意したとみなし、これに異議を唱えない方
:::

以降、筆者は上記に該当しない方の閲覧を想定せず書き進めますので、上記にご理解をいただけない場合はブラウザバックをしていただけますか。
非常に強くお伝えしていますが、本稿の内容を実施する事は重大なインシデントになったり使用した事により不利益が生じる可能性が高い内容であるため、以降でも注意喚起を続けていきます。

---

---

:::note alert
注意書きをよく読みよく理解し、同意できない場合は閲覧できません。
閲覧された時点で同意したものとみなします。
:::

---

---

## 結論：個人ならアリ
スマホの破損や機種変に怯えることがなくなったのは大きいです！
authのsaveファイル自体もクラウドバックアップを取っておけばPCの機種変にも対応できます。

ただし、持ち運びしやすいシンクライアントPCからアクセスできる状態にすると危険がすぎるので、運用時には細心の注意を払う必要があります。
リスクとしては、ノートパソコンならスマホを落とす等紛失した時並のリスクがありますが、紛失率は持ち運びできないPCはほぼ０％（盗難リスクは一様にあります）と考える事ができるのもポイントです。
これはスマホに限る話ではありませんが、リモート接続などで見えてしまうヒューマンエラーのリスクはあります。

## 二段階Authを使って家族共用のパソコンでアカウントを強固に守る
家族分のログインアカウントを発行して、それぞれが任意で使えるようにする方がまだマシな気がします。
が、家族共用のアカウントを使っており、既に思い思いの設定など（学校の勉強用やライセンス）が入ってしまったため、アカウントを分けられないケースを想定します。

:::note warn
流出リスクや漏洩した際の二次災害を低減するためにも、複数人で運用するべきではありません。
:::

### 家族全員分のauthをアプリで一括管理する
「機種変更の手続きが面倒くさいからPCに移行して管理しよう」という趣旨には合っていますが、セキュリティを犠牲にしたくないという要件は満たせません。
セキュリティ要件が本当に必要がないのか、再度検討しましょう。

セキュリティ・運用面に問題がないなら実施してみます。
セキュリティ要件もある場合、共有アカウントの環境を変えるわけにはいかないので、新しく認証用アカウントを新たに追加して、そちらで認証させる案です。
夫婦共有で子供たちに伝えないものとして、よくあるのが結婚記念日＋子供の名前の組み合わせとかでしょうか。
しかし、結婚記念日自体はカレンダーに登録してしまっていたり等すると聡いお子さんならパターンから推測して解析する事ができてしまいます。

とはいえ、うまく運用できたとしても認証用のアカウントに切り替えてauthコードを発行するのは正直手間です。
普段使いしている共有アカウントにauthアプリを入れると家族全員が使えるので、ログインして欲しくないアカウントもログインできるようになります。
あるいは、こういったアカウントを使いたい場合は、これらのアカウントのみPCのauthアプリには入れず、個別で使用している端末に入れるのが良いでしょう。
もちろん、本来の趣旨である機種変更や唐突な破損に対するリカバリーはなくなりますので、管理には十分に注意してください。

### 家庭内不和で生じるインシデント対策
セキュリティの話ではなく、運用の話として捉えてほしいです。

複数人で運用する場合は内部犯対策を検討しなければなりません。
特に子供（中学生～実家暮らし）は知識をつけても善悪の判断や責任能力は弱いままなので、たとえばゲーム等で課金制限（お小遣いなどの制裁）に対する反発として、現状運用中のauthを削除するという暴挙に出る事が考えられます。
認証システムに慣れている成人なら、auth認証を削除するという事がどういう事か想像できますが、彼らに想像させるのも、出来たとしてどういうリスクが考えられるのかを予測させるのは不可能だと考えたほうが良いです。
（私見ですが、私も親の立場なので子供のことは信じてあげたいですが、家族のプロジェクトマネージャーという観点で言えば、高すぎるリスクを許容する事ができません）

authではないですが、こういった大事なものを管理する時に採用されがちなのが、家族で一番権限を持つ人だけが使用できるようにするとかですね。
authでも同様に管理する必要がありますが、ライフイベント後（単身赴任・独り立ちなど）でも他の家族が使えるように移行とバックアップはしっかりやりましょう。
ここで作業をミスすると使いたい時に使えない、なんて事も起こりえますので慎重に。

## やり方
:::note warn
メリデメをしっかり理解してもらった上で、やり方の話をしていきます。
ヒューマンエラーがどうとかセキュリティリスクについて、以降は無視します。
:::

今回はwinauthを採用します。
技術的要件は、

- windows機である
- サードパーティーを入れられる

winauthを入れられる要件はこれだけです（執筆時点）
将来的にwinauthが使えなくなる可能性はありますが、代替アプリが出てくるとかOSをアップデートしないなどの対応を検討する必要がある事は認識しておくべきかと思います。

## 使い方
起動したらaddで登録したいauthenticationを入れてください。
種類が色々ありますが、winauthのアイコンが変わるぐらいでどれでも一緒です。
多少登録が楽になるぐらいでしょうか。私はAuthenticatorしか使っていませんが、きちんと運用できています。

試しにgoogleなり、普段使っている2FAを何か入れてみてください。
ただし、過去に登録している情報は削除（更新）される可能性が高いため、既に運用中のものを登録する場合は注意してください。
私が確認した、複数のauthを入れられるものだとamazonでしょうか。

## バックアップ
winauthだと２つの方法があります。
どちらも内容は平文なので、端末を超えてバックアップする場合（クラウドストレージなど）は管理方法に注意しましょう。

### Exportを使う
addで登録したデータをExportする事で、別の環境でImportして内容を復元できます。
Importのデフォルトがxmlで、Exportするファイルはtxtなので、拡張子はしっかり確認しておきましょう。

### WinAuthの保存ファイル（`%AppData%\Roaming\WinAuth\winauth.xml`）を使う
winauth.exeを実行した後の設定ファイルをそのまま使い回す案です。
こちらの方が確実ですね。

## (Mac向け)他の方法
従来の方法ではスマホアプリのauthenticatorを入れているはずです。
ということは、PCにスマホアプリを入れられるスマート端末エミュレーターがあれば同じことができます。
私が使っている中で手っ取り早く環境を作れたのはBlueStacksとかNoxPlayerとかでしょうか。
「スマホゲーム　PC」あたりで検索すると情報が多いです。
ポイントは、「ガチャゲーをPCで遊ぶ」というアプローチの情報が多い事です。
開発目的だと途端に情報がなくなったり、難しくなったりします。
この辺りのググラビリティは課題なんでしょうか？

エミュレーターの入れ方は本稿では取り扱わないですが、スマホのエミュレーターのauthenticatorでもしっかり認証されます。
タイトルが「AuthをPCだけで完結させる方法」なので、この方法もアリとしましたが、Windows以外だとほぼこれしか方法がありません。
MacなどからWindowsにリモート接続して、Windows上のアプリを起動するという方法もなくはないです。

これも実際にやってみたんですが、認証するためにエミュレーター起動してパスコード通して（これは省略可）アプリ立ち上げてコード開ける…という作業をやる事になります。
私は面倒くさくなって採用して一週間も経たずに廃止しました…

ここで言いたいのは、運用に耐えるかどうかは別として、出来ないこともないです。
ただし、おま環で上手くいかない可能性も考えられます。

## リスク
実機・エミュレーター・winauthのいずれのパターンでも、以下に留意しておく必要があります。

- 【エミュレーター】アプリやエミュレーターのOSのサポートが失効する
- 【エミュレーター】エミュレーター自体のバージョンアップで互換性が消失する
- OSなどシステムアップデートでアプリが使えなくなる
- 物理的にデバイスが故障する

と言った場合のトラブルの保証は誰にもできません。
特に実機でトラブルが発生した場合に、authenticator関連の保証はgoogleやAppleにはできない事を留意しましょう。

## AuthをPCだけで完結させる方法とメリデメ
セキュリティリスクを厚めに、運用リスクにも少々言及しました。
特に実機の障害リスクについては普段意識しにくい部分（記憶に新しいものだと、KDDIの通信障害など）なので、防災訓練ではないですが定期的にリスクの見直しをする機会を作るのが良いでしょう。
エンジニアには少ないと思いますが、たとえば外勤で社内システムにアクセスする（専用アプリを開いて入力があるなど）業務の場合は特に。

少し難しい話ですが、SREまたはセールスエンジニアの方は、障害発生時の対応について保守業務または契約の提案ができると営業にありがたがられる傾向があります（実体験）
直近だと、Authは関係ないのですが講師業に従事している際にクライアントPCの環境トラブルが発生した際に現場で対応するのか、あるいはサポートチームに対応を引き継げるのかだけでも心理的負荷がかなり違うので、研修パッケージを提供されている方は教室運営の体制構築の際はぜひご検討いただきたいです。

こういった障害を予測して対策する、という考え方は本稿の内容のみに限らず、業務のあらゆるシーンで活用できます。

## 次の記事
- [(11日目) README.md書いてますか？ドキュメンテーションを強化する「docsify」の紹介](https://qiita.com/nomurasan/items/676503670a68b53952ff)
- [カレンダーページ](https://qiita.com/advent-calendar/2022/oreno_nomurasan2022)
