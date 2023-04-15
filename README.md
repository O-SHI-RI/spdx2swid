# spdx2swid

IPAが開発したセキュリティ情報の収集ツールである、**mjcheck4** (<https://jvndb.jvn.jp/apis/myjvn/mjcheck4.html>) にSBOMのインポート機能が実装されましたが、
サポートフォーマットが *.swidtag* のみであり、SPDXなどのファイルフォーマットに対応していなかった為、 *.spdx* フォーマットのファイルを *.swidtag* に変換するスクリプトです。

# スクリプトの説明

SPDXは規格的にいくつかのファイルフォーマットをサポートしていますが、本スクリプトは *SPDX Tag/value documen*を対象にしています。
別のファイルフォーマットは現在サポートを検討していません。

```
git clone https://github.com/O-SHI-RI/spdx2swid.git
cd spdx2swid
python SPDX2SWIDTAG.py xxxx.spdx

```

スクリプト実行時の引数として、変換したいspdxファイルを渡してください。

# ProductList.txtについて

本リストは、IPAが公開している **MyJVN API** (<https://jvndb.jvn.jp/apis/index.html>)を経由して作成しています。2023年4月中旬のデータで作成していますが、
情報が古くなりますので、必要に応じて各々でデータを更新してください。

# ライセンス

BSD-2ライセンスとしています。
一部、ChatGPTによってコードを出力し、そのコードに変更を加えています。