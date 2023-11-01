REM コミット対象のリポジトリ
set REPOS=%1

REM トランザクション番号
set TXN=%2

REM 取得した情報からコメント取得してファイル出力する
REM C:\Users\(USERNAME)\AppData\Local\Temp
for /f "usebackq delims=" %%a in (`svnlook log -t "%TXN%" "%REPOS%"`) do (
set COMMENT=%%a
)

REM 一文字も入力されていなければ中断
if "%COMMENT%" =="" (
echo "コメントを1文字以上入力してください。" >&2
exit 1
)

REM エラー無ければ正常終了
exit 0
