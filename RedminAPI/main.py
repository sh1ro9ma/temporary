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


def newIssue(redmine_r):
    issue = redmine_r.issue.new()
    issue.project_id = 'Test1'
    issue.subject = 'サブジェクト'
    issue.tracker_id = 1                                             # トラッカー
    issue.description = 'チケットの内容をしめす。\n改行もできる。'
    issue.status_id = 1                                              # ステータス
    issue.priority_id = 1                                            # 優先度
    issue.assigned_to_id = 1                                         # 担当者のID
    issue.watcher_user_ids = [1]                                     # ウォッチするユーザのID
    issue.parent_issue_id = 12                                       # 親チケットのID
    issue.start_date = datetime.date(2014, 1, 1)                     # 開始日
    issue.due_date = datetime.date(2014, 2, 1)                       # 期日
    issue.estimated_hours = 4                                        # 予想工数
    issue.done_ratio = 40
    issue.custom_fields = [{'id': 1, 'value': 'foo'}]
    # issue.uploads = [{'path': 'C:\\dev\\python3\\redmine\\test.txt'}]
    issue.custom_fields = [{'id': 1, 'value': 'foo'}]
    issue.save()


def main():
    redmine = getRedmineObj(True)
    print(redmine)

    projects = redmine.project.all()
    for prj in list(projects):
        print(prj)

    issues = redmine.issue.all()
    print(issues)

    newIssue(redmine)


if __name__ == "__main__":
    main()
