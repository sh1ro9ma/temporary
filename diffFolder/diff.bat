REM 共通設定を読み込む
CALL commonSetting.bat

REM 比較フォルダの指定
set left_folder=D:\work\gitTest\diffTest
set right_folder=D:\work\gitTestRemote\difTestRem

REM WinMergeでの比較(Ver.2.16.15以降で実行すること)
call "%exe_file_winMerge%" /enableexitcode /r /wl /wr "%left_folder%" "%right_folder%"

REM WinMergeが差分を検出した場合、エラーコードが0以外に設定される
REM echo %ERRORLEVEL%
if %ERRORLEVEL%==0 (
    echo not found diff
    goto fin
)

if %ERRORLEVEL%==2 (
    echo unexpected error
    goto fin
)

echo found diff
echo copy right to left? Y/N
REM インデント内だと取得できないので注意
set /p overwriteR2L=
if /i "%overwriteR2L%"=="Y" (
    copy /y "%right_folder%" "%left_folder%"
    echo File overwritten
    goto fin
)

echo %overwriteR2L%

echo copy left to right? Y/N
set /p overwriteL2R=
if /i "%overwriteL2R%"=="Y" (
    copy /y "%left_folder%" "%right_folder%"
    echo File overwritten
)
echo %overwriteL2R%

:fin
pause
