REM コミット対象のリポジトリ
set REPOS=%1

REM トランザクション番号
set TXN=%2

REM 取得した情報からコメント取得してファイル出力する
REM C:\Users\(USERNAME)\AppData\Local\Temp
svnlook log -t "%TXN%" "%REPOS%" > tmp.txt

REM 出力したファイルに関する情報をさらにファイル出力
dir | FindStr "tmp.txt" > siz.txt

REM ファイルに関する情報を取得
set /p FindLine=<siz.txt

REM 内容確認
REM echo "%FindLine%" >&2

REM ファイルサイズに相当する文字を取得する
REM 下記フォーマットを想定し、空白で区切った3番目の要素取得 
REM 2023/10/26  23:03                 0 test.txt
for /f "tokens=3 delims= " %%a in ("%FindLine%") do (
REM echo %%a >&2
set /a SIZE=%%a
REM echo %SIZE% >&2
)

REM 一文字も入力されていなければ中断
if %SIZE% leq 2 (
echo "Please input comment" >&2
REM del tmp.txt
exit 1
) else (
echo "else" >&2
REM del tmp.txt
exit 1
)

exit 0
