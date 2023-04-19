# spdx2swidtag

IPAが開発したセキュリティ情報の収集ツールである、**mjcheck4** (<https://jvndb.jvn.jp/apis/myjvn/mjcheck4.html>) にSBOMのインポート機能が実装されました。  
本機能がサポートするファイルフォーマットが現状 *.swidtag* のみとなっており、一部のSBOM生成ツールが出力するSPDX仕様のファイルは食わすことができないのでそれを変換するスクリプトです。  
但し、SPDXは仕様としていくつかのファイルフォーマット(json、yaml、rdf/xml、tag:value(テキスト)、xls)を利用可能ですが、本スクリプトはtag:value(テキスト)形式のファイルを変換する為だけに作成しています。  
jsonやxmlなどのフォーマットからの変換はサポートしていません。  
また、***.swidtag* フォーマットへの変換は行いますが、SWID Tagの仕様を満たしたファイルへの変換を行うわけではなく、単にmjcheck4が取り込んるようにSPDXのファイルを変換するだけになります。繰り返しとなりますがSWID仕様を満たしたファイル変換は行いません。**  
故に、mjcheck4に取り込む上で必要ではないSWIDタグについてはブランクとしています。

## スクリプトの使用

本スクリプトは *SPDX Tag/value document(.spdx)*を対象にしています。  
他のファイルフォーマットに対する変換はサポートしていません。  
実行時には変換したい.spdxのファイルを実行時の引数として渡して下さい。  

```
python SPDX2SWIDTAG.py xxxx.spdx
```

## スクリプトの説明

スクリプトは下記流れで処理をしています。

    1.  SPDXファイル内の *PackageName:* タグを検索し、そのコンポーネント名を取得。
    2.  取得したコンポーネント名をJVNのサイトから出力して作成したリスト(ProductList.txt)から検索し、CPE番号を取得。
    3.　　.swidtagで書き出し。

## 留意事項

-   スクリプトではSPDXファイルから *PackageName:* のみを取得しているため、ベンダー情報などは取得していません。
-   例えば、[Virtual Box]などがコンポーネントある場合、JVNのDBには複数ベンダーが登録されているため、mjcheck4インポート後に適切な方を選択してください。
-   mjcheck4の仕様上(2023年4月段階)、コンポーネント/パッケージのバージョン情報は、SBOMからインポートできません。
-   故に、mjcheck4を使って、利用しているコンポーネントバージョンと脆弱性情報のマッチングは不可能です。これは、CPEとして記載される情報の内、mjcheck4のＳＢＯＭインポート機能がバージョン以降の情報を破棄する仕様の為です。(現状)
-   単に利用しているコンポーネントのいずれかのバージョンに脆弱性がある。。。というところまで、確認することができます。
-   収集起点日を古い日付(例：2010年など・・・)に設定すると、取り込んだコンポーネントに過去どれだけ脆弱性が報告されているかが確認できて楽しい。

## ProductList.txtについて

本リストは、IPAが公開している **MyJVN API** (<https://jvndb.jvn.jp/apis/index.html>)を経由して作成しています。  
2023年4月中旬のデータで作成していますが、情報が古くなりますので、必要に応じて各々でデータを更新してください。

## ライセンス

BSD-2ライセンスとしています。
一部、ChatGPTによってコードを出力し、そのコードに変更を加えています。
