@echo off
REM ファイルをコピーするバッチファイル
chcp 65001

REM コピー元ファイルのパス
set src_folder=lochooks\
set file_name=post-merge
set src_path=%src_folder%%file_name%

REM コピー先ファイルのパス
set dst_folder=.git\hooks\
set dst_path=%dst_folder%%file_name%

echo SRC:"%src_path%"
echo DST:"%dst_path%"
echo.

REM コピー元ファイルが存在するか確認
if not exist "%src_path%" (
    REM 処理を続行できないので終了
    echo Source file not found
    goto fin
)

REM ファイルをコピーしたら終了
if not exist "%dst_path%" (
    copy "%src_path%" "%dst_path%"

    REM 処理を終えたので終了
    echo File copy completed
    goto fin
)

REM 上書きを確認する
echo Destination file found
echo Do you want to overwrite? (Y/N)
set /p overwrite=
if /i "%overwrite%"=="Y" (
    copy /y "%src_path%" "%dst_path%"
    echo File overwritten
) else (
    echo File copy canceled
)

:fin
REM バッチファイルの実行を一時停止（キーを押すまで待つ）
pause
