> 以下、注意事項です。
- クライアントがGUIに対応していないと表示されない
- つまり、Desktop版からsshで接続する必要があります。
- Windows Subsystem for Linux(Bash on Windows on Ubuntu)だとダメでした。

LinuxでのGUIはX(X Windows System)を使っていますので、操作する側(画面・キーボード・マウスを使う側)で**Xサーバソフトウェア**を起動させておく必要があります。
「クライアントがGUIに対応していないと」は、正しくは「クライアントでXサーバをインストール・起動していないと」です。
で、Windows Subsystem for LinuxにはXサーバソフトが付属していません。それにWindowsそのものはXサーバの役割を持ちません。なので、何かしらXサーバソフトを用意する必要があります。( 今だと VcXsrv が良いと思います。qiitaにも幾つか記事があるようです )
