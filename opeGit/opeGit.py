import os
import git

import time

FILE_NAME = "あすきー.txt"
FOLDER_PATH = r"D:\work\gitTest"
FILE_PATH = FOLDER_PATH + "\\" + FILE_NAME

TGT_ALL = "."

nowTimeStr = str(time.time())

with open(FILE_PATH, mode="a") as f:
    f.write(nowTimeStr + "\r")


# Pushしたいgitリポジトリのフォルダへ移動する
os.chdir(FOLDER_PATH)

# オブジェクト用意
repo = git.Repo()

# 先に最新を取得する
remOrg = repo.remotes.origin
remOrg.pull()

# 一式コミットする
commitComment = "test" + nowTimeStr
repo.git.commit(TGT_ALL, '-m', commitComment)

# プッシュする
remoteName = "origin"
origin = repo.remote(name=remoteName)
origin.push()
