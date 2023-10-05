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
        print(f"{mean_r}\t{attrN_r}\t{info}")
    else:
        pass
        # info = None


# https://qiita.com/flcn-x/items/89e8f709277c9fbf6275#%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E6%83%85%E5%A0%B1%E3%81%AE%E5%8F%96%E5%BE%97
def infoIssue(issue_r):
    showAttr(issue_r, "チケットID",     "id")
    showAttr(issue_r, "チケットURL",    "url")
    showAttr(issue_r, "トラッカーID",   "tracker.id")
    showAttr(issue_r, "トラッカー",     "tracker.name")
    showAttr(issue_r, "題名",           "subject")
    showAttr(issue_r, "説明",           "description")
    showAttr(issue_r, "ステータスID",   "status.id")
    showAttr(issue_r, "ステータス",     "status.name")
    showAttr(issue_r, "優先度ID",       "priority.id")
    showAttr(issue_r, "優先度",         "priority.name")
    showAttr(issue_r, "担当者ID",       "assigned_to.id")
    showAttr(issue_r, "担当者名",       "assigned_to.name")
    showAttr(issue_r, "親チケットID",   "parent")
    showAttr(issue_r, "開始日",         "start_date")
    showAttr(issue_r, "期日",           "due_date")
    showAttr(issue_r, "予定工数",       "estimated_hours")
    showAttr(issue_r, "プロジェクトID", "project.id")
    showAttr(issue_r, "プロジェクト",   "project.name")
    showAttr(issue_r, "作成者ID",       "author.id")
    showAttr(issue_r, "作成者名",       "author.name")
    showAttr(issue_r, "進捗率",         "done_ratio")
    showAttr(issue_r, "作成日",         "created_on")
    showAttr(issue_r, "更新日",         "updated_on")
    showAttr(issue_r, "作業時間",       "spent_hours")

    showAttr(issue_r, "ウォッチャー ウォッチャーID",       "watchers.id")
    showAttr(issue_r, "ウォッチャー ウォッチャー名",       "watchers.name")
    showAttr(issue_r, "カスタム領域 カスタムID",           "custom_fields.id")
    showAttr(issue_r, "カスタム領域 カスタム名",           "custom_fields.name")
    showAttr(issue_r, "カスタム領域 カスタム値",           "custom_fields.value")
    showAttr(issue_r, "送付ファイル ファイルID",           "attachments.id")
    showAttr(issue_r, "送付ファイル ファイル名",           "attachments.filename")
    showAttr(issue_r, "送付ファイル ファイル説明",         "attachments.description")
    showAttr(issue_r, "送付ファイル ファイルサイズ",       "attachments.filesize")
    showAttr(issue_r, "送付ファイル ファイル著者",         "attachments.author")
    showAttr(issue_r, "送付ファイル ファイルURL",          "attachments.content_url")
    showAttr(issue_r, "送付ファイル ファイル作成日",       "attachments.created_on")
    showAttr(issue_r, "コミットログ ",                     "changesets")
    showAttr(issue_r, "子チケット 子チケットID",           "children.id")
    showAttr(issue_r, "子チケット 子チケットタイトル",     "children.subject")
    showAttr(issue_r, "関連するチケット 関連ID",           "relations.id")
    showAttr(issue_r, "関連するチケット 関連する自分のID", "relations.issue_id")
    showAttr(issue_r, "関連するチケット 関連する相手のID", "relations.issue_to_id")
    showAttr(issue_r, "関連するチケット 関連のタイプ",     "relations.relation_type")


def infoIssue2(issue_r):
    showAttr(issue_r, "チケットID",       "id")
    showAttr(issue_r, "チケットURL",      "url")
    showAttr(issue_r, "トラッカー",       "tracker")
    showAttr(issue_r, "題名",             "subject")
    showAttr(issue_r, "説明",             "description")
    showAttr(issue_r, "ステータス",       "status")
    showAttr(issue_r, "優先度",           "priority")
    showAttr(issue_r, "担当者",           "assigned_to")
    showAttr(issue_r, "親チケットID",     "parent")
    showAttr(issue_r, "開始日",           "start_date")
    showAttr(issue_r, "期日",             "due_date")
    showAttr(issue_r, "予定工数",         "estimated_hours")
    showAttr(issue_r, "プロジェクト",     "project")
    showAttr(issue_r, "作成者",           "author")
    showAttr(issue_r, "進捗率",           "done_ratio")
    showAttr(issue_r, "作成日",           "created_on")
    showAttr(issue_r, "更新日",           "updated_on")
    showAttr(issue_r, "作業時間",         "spent_hours")
    showAttr(issue_r, "ウォッチャー",     "watchers")
    showAttr(issue_r, "カスタム領域",     "custom_fields")
    showAttr(issue_r, "送付ファイル",     "attachments")
    showAttr(issue_r, "コミットログ ",    "changesets")
    showAttr(issue_r, "子チケット",       "children")
    showAttr(issue_r, "関連するチケット", "relations")


def showIssueList(issueLst_r):
    print("issue list")
    for cnt, iss in enumerate(list(issueLst_r)):
        print(f"iss:{cnt:03}")
        infoIssue2(iss)
        print("")

def test():
    # https://srbrnote.work/archives/4946
    import inspect
    tgtObj = list(issues)[0].watchers
    print(tgtObj)
    print("1--------------------------------------------")
    print(type(tgtObj))
    print("2--------------------------------------------")
    print(dir(tgtObj))
    print("3--------------------------------------------")
    print(inspect.getmembers(tgtObj))
    print("4--------------------------------------------")
    attrs = inspect.getmembers(tgtObj)
    attrLst = [x for x in attrs if not callable(x[1])]
    print(attrLst)
    print(attrs)
    print("5--------------------------------------------")
    print(vars(tgtObj))  # dictオブジェクトの存在確認して実施すればいい
    print("6--------------------------------------------")
    dicti = vars(tgtObj)
    for dic in dicti:
        print(dic, type(dic))
    print("7--------------------------------------------")
    print(dicti["_resources"])
    print("8--------------------------------------------")
    for di in dicti["_resources"]:
        print(di)


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
    # newIssue2(redmine, prj_name)

    # get して オプション代入してsaveでもいい
    # https://python-redmine.com/resources/issue.html#update-methods
    redmine.issue.update(
        1,  # issueのid指定
        description='foo',       # 説明欄も置き換わる。更新履歴も一応は残って差分を確認できる。
        notes='A journal note',  # チケット下部に表示されるコメント欄と思ってよさそう
        done_ratio=60,
    )


if __name__ == "__main__":
    main()
