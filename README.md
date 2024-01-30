# SDM-report2
(1)	テストランナーの実行
　テストに失敗しているのは、sample4であり、A=0.1、B=999を引数としたとき、関数の戻り値は-1であるというテストケースである。正常に計算が行われた場合、関数の戻り値はAとBを乗算した値であり、関数実装に当たっての要件として、A, Bの入力範囲は1～999の整数であるため、A=0.1であるケースで戻り値は-1となるはずであるが、実際には計算結果である99.9が出力されているため、テストが失敗していると考えられる。
(2)	テストケースの作成
テストケース作成についての戦略を提示する。
テストケースとして考えるべき条件は、
・	入力条件に含まれる数値
・	入力条件に含まれない数値
: AまたはBが範囲外の整数である場合
: AまたはBが小数を含む場合
・	数値ではない入力
: AまたはBに数字以外を含む場合
: AまたはBが全て数字以外で構成される場合
　として、これに基づいてテストケースを作成し、gitのレポジトリに追加した
(3)	バグの修正
変更したテストケースでユニットテストを行った結果、
・	入力値がA<Bでない場合、-1が出力される
・	入力が小数であっても計算が行われる
・	入力のどちらかが数値であれば片方がそうなくとも計算を行おうとする
・	数とそうでない文字が混ざっている場合、計算を行おうとする
といったバグを発見できた。
　これらをテストケースをパスするようcalc_mul.pyを修正し、gitにコミットした。
修正の具体的な内容は、以下の通りである。
・	正則表現が小数を含んでいてもマッチする、変数の部分的な文字又は文字列でマッチするようになっていたのを修正。文字列の先頭と終端を指定し、変数全体が0~9の文字で構成されている場合のみマッチするようにした。
・	正則表現を修正した結果、入力は整数のみを想定するため、a, bをfloat型からint型へ変更した。
・	aiとbiについてのif文で論理演算がorだったことから、どちらかが条件を満たせばvalidがTrueになっていたためandに修正した。
・	不必要な大小比較条件を削除した
