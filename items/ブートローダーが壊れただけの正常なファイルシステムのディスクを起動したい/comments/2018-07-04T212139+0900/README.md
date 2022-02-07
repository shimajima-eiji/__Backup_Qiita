私が主に使うのはRedHat/CentOSですが、そういう場面なら

* インストーラDVDで起動 ( 場合によってはPXEブート )
* 普通にインストーラの画面を出してから、Ctrl+Alt+F2あたりでシェルに抜ける
* 仮のディレクトリを(メモリ上に)作って元のディスクの領域をマウントし、そこにchroot

これでインストーラ実行中でありながら、元のシステムにアクセスできますので、後はgrubの修復を行います。
[RedHat社のドキュメント](https://access.redhat.com/documentation/ja-jp/red_hat_enterprise_linux/7/html/system_administrators_guide/sec-reinstalling_grub_2)が分かり易いです。
そこにも出てますが、BIOSモードかUEFIモードかで大きく変わりますので注意が必要です。
