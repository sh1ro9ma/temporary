import subprocess
import glob
import os


PATH_EXE_WINM = r'"C:\Program Files\WinMerge\WinMergeU.exe"'
PATH_DIFF_LEFT = r'D:\work\gitTestRemote\difTestRem'
PATH_DIFF_RIGHT = r'D:\work\gitTestRemote\difTestRem2'

OPT_WINM_UPACK = '-unpacker'

PLGIN_UPACK_LST = [
    {
        'Ext': '.xlsx',
        'Plg': 'CompareMSExcelFiles.sct'
    },
    {
        'Ext': '.xls',
        'Plg': 'CompareMSExcelFiles.sct'
    },
    {
        'Ext': '.docx',
        'Plg': 'CompareMSWordFiles.sct'
    },
]


def run_diff_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print("Error:", result.stderr)
            return None
    except Exception as e:
        print("Error:", str(e))
        return None


lPathLst = glob.glob(PATH_DIFF_LEFT + "\\*")
rPathLst = glob.glob(PATH_DIFF_RIGHT + "\\*")

# 同名ファイルを取得する
tgtFileLst = []
for lFilePath in lPathLst:
    lFileName = os.path.basename(lFilePath)

    for rFilePath in rPathLst:
        rFileName = os.path.basename(rFilePath)

        if lFileName == rFileName:
            cmpInfo = {
                'fileName': lFileName,
                'lFilePath': lFilePath,
                'rFilePath': rFilePath
            }
            tgtFileLst.append(cmpInfo)


# 順番に差分比較を行う
for tgtFile in tgtFileLst:
    # ファイルに応じたプラグインを利用する
    plugin = None
    for unpack in PLGIN_UPACK_LST:
        if unpack['Ext'] in tgtFile['fileName']:
            plugin = unpack['Plg']
            break

    # コマンドを作成する
    # 必要ならプラグインも指定する
    command = f'{PATH_EXE_WINM} {tgtFile["lFilePath"]} {tgtFile["rFilePath"]}'
    if plugin is not None:
        command = command + f' {OPT_WINM_UPACK} {plugin}'

    # 比較を実行する
    res = run_diff_command(command)
