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

# PUllの実行
command = "git pull"
run_cmd_command(command, repo_directory)

# # プッシュを実行
# subprocess.run(["git", "push", "origin", branch_name], cwd=repo_directory, check=True)
