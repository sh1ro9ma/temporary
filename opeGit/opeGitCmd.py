import subprocess


def run_cmd_command(command, repoPath):
    try:
        result = subprocess.run(command, cwd=repoPath, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, check=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print("Error:", result.stderr)
            return None
    except Exception as e:
        print("Error:", str(e))
        return None


# プッシュ対象のブランチ名
branch_name = "master"

# Gitリポジトリのディレクトリパス
repo_directory = r"D:\work\gitPushTest\temporary"

# 最新取得
command = "git pull"
run_cmd_command(command, repo_directory)

# ステージング
command = "git add ."
run_cmd_command(command, repo_directory)

# コミット
command = "git commit -m commit by script"
run_cmd_command(command, repo_directory)

# # プッシュ
# command = "git push master"
# run_cmd_command(command, repo_directory)
