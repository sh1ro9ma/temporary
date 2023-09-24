@echo off
REM ファイルをコピーするバッチファイル

REM コピー元ファイルのパス
set source_file=lochooks\post-update

REM コピー先フォルダのパス
set destination_folder=.git\hooks\

REM コピー元ファイルが存在するか確認
if not exist "%source_file%" (
    echo "can't find copy file"
    goto fin
)

echo "src ok"
pause
REM コピー先ファイルが存在するか確認
if exist "%destination_folder%\File.txt" (
    echo コピー先ファイルが既に存在します。上書きしますか？ (Y/N)
    set /p overwrite=
    if /i "%overwrite%"=="Y" (
        copy /y "%source_file%" "%destination_folder%\File.txt"
        echo ファイルを上書きコピーしました。
    ) else (
        echo コピーをキャンセルしました。
    )
) else (
    copy "%source_file%" "%destination_folder%\File.txt"
    echo ファイルをコピーしました。
)


:fin
REM バッチファイルの実行を一時停止（Enterキーを押すまで待つ）
pause
