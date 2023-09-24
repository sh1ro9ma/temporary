REM 共通設定を読み込む
CALL commonSetting.bat

REM 比較フォルダの指定
set left_folder=D:\work\gitTest\diffTest
set right_folder=D:\work\gitTestRemote\difTestRem

REM WinMergeでの比較
start "" "%exe_file_winMerge%" /r /wl /wr "%left_folder%" "%right_folder%"

pause
