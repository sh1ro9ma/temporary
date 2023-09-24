@echo off
REM ファイルをコピーするバッチファイル
chcp 65001

REM hookscriptの参照先ディレクトリを変更する
git config --local core.hooksPath .githooks

REM 変更後の状態を確認する
echo changed: local core hooksPath
git config --local core.hooksPath
pause
