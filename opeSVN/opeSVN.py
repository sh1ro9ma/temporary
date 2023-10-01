import subprocess


def run_svn_command(command):
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


def exportFile():
    repository_url = r"file:///D:/work/svnTest/テスト/trunk"
    destination_folder = r"D:\work\svnTest\test用2"

    latest_revision_command = f"svn export {repository_url}@HEAD {destination_folder}"
    run_svn_command(latest_revision_command)

    # previous_revision = 100  # 一つ前のリビジョン番号を指定
    # previous_revision_command = f"svn export {repository_url}@{previous_revision} {destination_folder}"
    # run_svn_command(previous_revision_command)


def getString(tgtStr_r, startMark_r, endMark_r):
    resStr = ""

    # 開始位置を取得
    start_index = tgtStr_r.find(startMark_r)
    if -1 == start_index:
        print(f"開始位置が見つかりません。: {startMark_r=}")
        return resStr
    else:
        # 開始位置を補正しておく
        start_index += len(startMark_r)  # 検索文字数そのもの分をシフトする

    # 終了位置を取得する
    end_index = tgtStr_r.find(endMark_r)
    if -1 == end_index:
        print(f"終了位置が見つかりません。: {endMark_r=}")
        return resStr

    # エラーチェックする
    if start_index > end_index:
        print("開始位置と終了位置が逆転しています。")
        return resStr

    # 文字列を取得する
    resStr = tgtStr_r[start_index:end_index]
    resStr = resStr.strip()
    return resStr


file_path = r"D:\work\svnTest\ローカル\trunk\フォルダ1\おはようございます.txt"
log_command = f"svn log {file_path}"
res = run_svn_command(log_command)
resLst = res.splitlines()
for res in resLst:
    isInfoRow = all(char in res for char in ('r', '|', 'line'))
    if True is isInfoRow:
        revNum = getString(res, "r", "|")
        print(f"{res}: get No. {revNum=}")
