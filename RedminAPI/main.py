from redminelib import Redmine

import datetime

import setting


def getRedmineObj(local_r):
    if local_r is True:
        redmine = Redmine(setting.redmineURL, key=setting.redmineKEY, requests={'verify': False})
    else:
        # ZscalerのVPNクライアントを経由する
        proxies = {
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080",
        }
        redmine = Redmine(setting.redmineURL, key=setting.redmineKEY, proxies=proxies, requests={'verify': False})

    return redmine


def newIssue1(redmine_r, prj_r):
    issue = redmine_r.issue.new()
    issue.project_id = prj_r
    issue.subject = "チケットのタイトル"
    issue.tracker_id = 1                                             # トラッカー
    issue.description = "チケットの説明欄。\n 改行もできる。"
    issue.status_id = 1                                              # ステータス
    issue.priority_id = 1                                            # 優先度
    issue.assigned_to_id = 1                                         # 担当者のID
    issue.watcher_user_ids = [1]                                     # ウォッチするユーザのID
    # issue.parent_issue_id = 12                                       # 親チケットのID
    issue.start_date = datetime.date(2014, 1, 1)                     # 開始日
    issue.due_date = datetime.date(2014, 2, 1)                       # 期日
    issue.estimated_hours = 4                                        # 予想工数
    issue.done_ratio = 40
    # issue.custom_fields = [{'id': 1, 'value': 'foo'}]
    # issue.uploads = [{'path': 'C:\\dev\\python3\\redmine\\test.txt'}]
    # issue.custom_fields = [{'id': 1, 'value': 'foo'}]
    issue.save()


def newIssue2(redmine_r, prj_r):
    issue = redmine_r.issue.new()
    issue.project_id = prj_r
    issue.subject = "チケットのタイトル"
    issue.tracker_id = 1                                             # トラッカー
    issue.description = "チケットの説明欄。\n 改行もできる。"
    issue.status_id = 1                                              # ステータス
    issue.priority_id = 1                                            # 優先度
    issue.assigned_to_id = 1                                         # 担当者のID
    issue.watcher_user_ids = [1]                                     # ウォッチするユーザのID
    issue.save()


def showAttr(issue_r, mean_r, attrN_r):
    if hasattr(issue_r, attrN_r):
        info = getattr(issue_r, attrN_r)
        print(f"{attrN_r}:{info}")
    else:
        pass
        # info = None


# https://qiita.com/flcn-x/items/89e8f709277c9fbf6275#%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E6%83%85%E5%A0%B1%E3%81%AE%E5%8F%96%E5%BE%97
def infoIssue(issue_r):
    showAttr(issue_r, "id")                         # チケットID
    showAttr(issue_r, "url")                        # チケットURL
    showAttr(issue_r, "tracker.id")                 # トラッカーID
    showAttr(issue_r, "tracker.name")               # トラッカー
    showAttr(issue_r, "subject")                    # 題名
    showAttr(issue_r, "description")                # 説明
    showAttr(issue_r, "status.id")                  # ステータスID
    showAttr(issue_r, "status.name")                # ステータス
    showAttr(issue_r, "priority.id")                # 優先度ID
    showAttr(issue_r, "priority.name")              # 優先度
    showAttr(issue_r, "assigned_to.id")             # 担当者ID
    showAttr(issue_r, "assigned_to.name")           # 担当者名
    showAttr(issue_r, "parent")                     # 親チケットID
    showAttr(issue_r, "start_date")                 # 開始日
    showAttr(issue_r, "due_date")                   # 期日
    showAttr(issue_r, "estimated_hours")            # 予定工数
    showAttr(issue_r, "project.id")                 # プロジェクトID
    showAttr(issue_r, "project.name")               # プロジェクト
    showAttr(issue_r, "author.id")                  # 作成者ID
    showAttr(issue_r, "author.name")                # 作成者名
    showAttr(issue_r, "done_ratio")                 # 進捗率
    showAttr(issue_r, "created_on")                 # 作成日
    showAttr(issue_r, "updated_on")                 # 更新日
    showAttr(issue_r, "spent_hours")                # 作業時間

    showAttr(issue_r, "watchers.id")                # ウォッチャー ウォッチャーID
    showAttr(issue_r, "watchers.name")              # ウォッチャー ウォッチャー名
    showAttr(issue_r, "custom_fields.id")           # カスタム領域 カスタムID
    showAttr(issue_r, "custom_fields.name")         # カスタム領域 カスタム名
    showAttr(issue_r, "custom_fields.value")        # カスタム領域 カスタム値
    showAttr(issue_r, "attachments.id")             # 送付ファイル ファイルID
    showAttr(issue_r, "attachments.filename")       # 送付ファイル ファイル名
    showAttr(issue_r, "attachments.description")    # 送付ファイル ファイル説明
    showAttr(issue_r, "attachments.filesize")       # 送付ファイル ファイルサイズ
    showAttr(issue_r, "attachments.author")         # 送付ファイル ファイル著者
    showAttr(issue_r, "attachments.content_url")    # 送付ファイル ファイルURL
    showAttr(issue_r, "attachments.created_on")     # 送付ファイル ファイル作成日
    showAttr(issue_r, "changesets")                 # コミットログ
    showAttr(issue_r, "children.id")                # 子チケット 子チケットID
    showAttr(issue_r, "children.subject")           # 子チケット 子チケットタイトル
    showAttr(issue_r, "relations.id")               # 関連するチケット 関連ID
    showAttr(issue_r, "relations.issue_id")         # 関連するチケット 関連する自分のID
    showAttr(issue_r, "relations.issue_to_id")      # 関連するチケット 関連する相手のID
    showAttr(issue_r, "relations.relation_type")    # 関連するチケット 関連のタイプ


def showIssueList(issueLst_r):
    print("issue list")
    for cnt, iss in enumerate(list(issueLst_r)):
        print(f"iss:{cnt:03}")
        infoIssue(iss)
        print("")


def main():
    redmine = getRedmineObj(True)
    print(redmine)

    print("Prj List")
    projects = redmine.project.all()
    prj_name = ""
    for cnt, prj in enumerate(list(projects)):
        prj_name = prj.identifier
        print(f"{cnt:03}:{prj_name}")
    print("")

    # チケット情報の取得
    # https://python-redmine.com/resources/issue.html#all
    issues = redmine.issue.all()
    showIssueList(issues)

    # # https://python-redmine.com/resources/issue.html#filter
    # issues = redmine.issue.filter(assigned_to_id=prj_name)
    # showIssueList(issues)

    # issues = redmine.issue.filter(assigned_to_id=1)
    # showIssueList(issues)

    # newIssue1(redmine, prj_name)
    newIssue2(redmine, prj_name)


if __name__ == "__main__":
    main()
