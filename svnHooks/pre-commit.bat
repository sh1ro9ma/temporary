REM コミット対象のリポジトリ
set REPOS=%1

REM トランザクション番号
set TXN=%2

REM 取得した情報からコメント取得してファイル出力する
REM C:\Users\(USERNAME)\AppData\Local\Temp
svnlook log -t "%TXN%" "%REPOS%" > tmpSVNcmnt.txt

REM 出力したファイルに関する情報をさらにファイル出力
dir | FindStr "tmpSVNcmnt.txt" > sizSVNcmnt.txt

REM ファイルに関する情報を取得
set /p FindLine=<sizSVNcmnt.txt

REM 取得の終わったファイルを削除しておく
del tmpSVNcmnt.txt
del sizSVNcmnt.txt

REM ファイルサイズに相当する文字を取得する
REM 下記フォーマットを想定し、空白で区切った3番目の要素取得(下記なら0)
REM 2023/10/26  22:43                 0 test.txt
for /f "tokens=3 delims= " %%a in ("%FindLine%") do (
set /a SIZE=%%a
)

REM 一文字も入力されていなければ中断
REM ファイル出力している都合上改行文字の2byteが下限となっている
if %SIZE% leq 2 (
echo "Please input comment" >&2
exit 1
)

REM エラー無ければ正常終了
exit 0
