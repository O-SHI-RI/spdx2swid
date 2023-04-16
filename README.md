# spdx2swidtag

IPAが開発したセキュリティ情報の収集ツールである、**mjcheck4** (<https://jvndb.jvn.jp/apis/myjvn/mjcheck4.html>) にSBOMのインポート機能が実装されましたが、
サポートファイルフォーマットが *.swidtag* のみであり、SPDXなどのファイルフォーマットに対応していなかった為、 *.spdx* フォーマットのファイルを *.swidtag* に変換するスクリプトです。

## スクリプトの使用

SPDXは規格的にいくつかのファイルフォーマットをサポートしていますが、本スクリプトは *SPDX Tag/value document(.spdx)*を対象にしています。
別のファイルフォーマットは現在サポートを検討していません。

```
git clone https://github.com/O-SHI-RI/spdx2swid.git
cd spdx2swid
python SPDX2SWIDTAG.py xxxx.spdx
```

スクリプト実行時の引数として、変換したいspdxファイルを渡してください。

## スクリプトの説明

スクリプトは下記流れで処理をしています。

    1.  SPDXファイル内の *PackageName:* タグを検索し、そのコンポーネント名を取得。
    2.  取得したコンポーネント名をJVNのサイトから出力して作成したリスト(ProductList.txt)から検索し、CPE番号を取得。
    3.　.swidtagで書き出し。

## 留意事項

-   スクリプトではSPDXファイルから *PackageName:* のみを取得しているため、ベンダー情報などは取得していません。
-   例えば、下記画像のように[Virtual Box]などは、JVNのリストに複数ベンダーが登録されているため、mjcheck4インポート後に適切な方を選択してください。
-   mjcheck4の仕様上(2023年4月段階)、コンポーネント/パッケージのバージョン情報は、SBOMからインポートできません。
-   故に、mjcheck4を使って、利用しているコンポーネントバージョンと脆弱性情報のマッチングは不可能です。
-   単に利用しているコンポーネントのいずれかのバージョンに脆弱性がある。。。というところまで、確認することができます。

![mjcheck4使用イメージ](img/mjcheck4_sample.png)

-   収集起点日を古い日付(例：2010年など・・・)に設定すると、取り込んだコンポーネントに過去どれだけ脆弱性が報告されているかが確認できて楽しい。

## ProductList.txtについて

本リストは、IPAが公開している **MyJVN API** (<https://jvndb.jvn.jp/apis/index.html>)を経由して作成しています。2023年4月中旬のデータで作成していますが、
情報が古くなりますので、必要に応じて各々でデータを更新してください。

## ライセンス

BSD-2ライセンスとしています。
一部、ChatGPTによってコードを出力し、そのコードに変更を加えています。
