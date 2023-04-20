# spdxtxt_coversion_mjcheck4

- IPAが開発したセキュリティ情報の収集ツールである**mjcheck4** (<https://jvndb.jvn.jp/apis/myjvn/mjcheck4.html>) にSBOMのインポート機能が実装されました。  
- 本機能がサポートするファイルフォーマットが現状 *.swidtag* のみとなっており、SPDX仕様のファイルは食わすことができないのでそれを変換するスクリプトです。  
- SPDXは仕様としていくつかのファイルフォーマット(json、yaml、rdf/xml、tag:value(テキスト)、xls)が利用可能ですが、**本スクリプトはtag:value(テキスト)形式のファイルを変換する為だけに作成しました。**  
- jsonやxmlなどのフォーマットからの変換はサポートしていません。  
- *.swidtag* フォーマットへの変換は行いますが、SWID Tagの仕様を満たしたファイルへの変換を行うわけではなく、単にmjcheck4が取り込める用にSPDXのファイルを変換するだけになります。*
- **SWID Tag仕様を満たしたファイルへの変換は行いません。**  
- mjcheck4に取り込む上で必要ではないSWIDタグの値についてはブランクとしています。

## スクリプトの使用

- 本スクリプトは **SPDX Tag/value document(.spdx)** を対象にしています。  
- 実行時には変換したい.spdxのファイルを実行時の引数として渡して下さい。  

```PowerShell
git clone https://github.com/O-SHI-RI/spdxtxt_coversion_mjcheck4.git
cd spdxtxt_coversion_mjcheck4
python spdxtxt_coversion_mjcheck4.py xxxx.spdx
```

## スクリプトの説明

スクリプトは下記流れで処理をしています。

1.  SPDXファイル内の *PackageName:* タグを検索し、そのコンポーネント名を取得。
2.  取得したコンポーネント名をJVN APIから出力したリスト(ProductList.txt)から検索し、CPE情報を取得。
3.  .swidtagで書き出し。

## その他

-   スクリプトではSPDXファイルから*Creator: Organization:* 及び*PackageName:* の値のみ取得しているため、パッケージのサプライヤー情報などは取得していません。
-   例えば[Virtual Box]がコンポーネントある場合、JVNのDBには複数のサプライヤーが登録されているため、mjcheck4インポート後に適切な方を選択してください。
-   これは一部のSBOM生成ツールでは、コンポーネント検出時にサプライヤー情報について*NOASSERTION*として記入していることがある為です。SPDXの仕様としては*NOASSERTION*で記入することは問題ないですが、mjcheck4ではCPE情報にサプライヤー情報がないと取り込めない仕様です。
-   mjcheck4の仕様上(2023年4月段階)、コンポーネントのバージョン情報はSBOMからインポートできません。これはインポート時にCPE情報にあるバージョン以降の情報を破棄する仕様の為です。
-   「コンポーネントの*いずれか*のバージョンに脆弱性がある」。。。というところまで、確認することができます。
-   収集起点日を古い日付(例：2010年など・・・)に設定すると、取り込んだコンポーネントに過去どれだけ脆弱性が報告されているかが確認できて楽しい。

## ProductList.txtについて

- IPAが公開している **MyJVN API** (<https://jvndb.jvn.jp/apis/index.html>)を経由して作成しています。  
- 2023年4月中旬のデータで作成していますが、情報が古くなりますので、必要に応じて各々でデータを更新してください。

## ライセンス

BSD-2ライセンスとしています。
一部、ChatGPTによってコードを出力し、そのコードに変更を加えています。
