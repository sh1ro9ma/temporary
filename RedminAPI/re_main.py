from redminelib import Redmine
from redminelib.managers.standard import ProjectManager
from redminelib.resources.standard import Issue
from redminelib.resultsets import ResourceSet

import setting


def get_redmine_obj() -> Redmine:
    """Redmine全体のオブジェクトを取得する"""
    return Redmine(setting.REDMINE_URL, key=setting.REDMINE_KEY, requests={"verify": False})


def get_users(redmine: Redmine) -> None:
    """Redmineオブジェクト中のユーザ情報を取得する"""
    for user in redmine.user.all():
        print(f"ID: {user.id}, 姓:{user.lastname}, 名: {user.firstname }, Email: {user.mail}")


def get_projects(redmine: Redmine) -> ResourceSet:
    """Redmineオブジェクト中のプロジェクトリストを取得する"""
    project_mng: ProjectManager = redmine.project
    projects: ResourceSet = project_mng.all()
    return projects


def get_digits_in_list_length(input_list_r: list) -> int:
    """
    指定されたリストの長さの桁数を取得する

    Args:
        input_list_r (list): 桁数を取得したいリスト

    Returns:
        int: リストの桁数

    Examples:
        >>> get_digits_in_list_length([1, 2, 3])
        1
        >>> get_digits_in_list_length(list(range(100)))
        3
    """
    return len(str(len(input_list_r)))


def get_attr_value(issue_r: Issue, attr_name_r: str) -> str:
    if hasattr(issue_r, attr_name_r):
        attr_value = str(getattr(issue_r, attr_name_r))
    else:
        attr_value = ""

    return attr_value


def get_ticket_id(issue_r: Issue) -> dict[str, str]:
    """チケットIDを取得する

    Args:
        issue_r (Issue): IDを取得したいチケットオブジェクト

    Returns:
        dict: 日本語文字列をキーとしたチケットID
    """
    return {"チケットID": get_attr_value(issue_r, "id")}


def get_watcher(issue_r: Issue) -> dict[str, str]:
    """チケットのウォッチャーを取得する

    ウォッチャーの情報はリストで保持されている。
    リストからIDと名前のペアを取得し、1つの文字列に連結してdictの値にする。
    w

    Args:
        issue_r (Issue): ウォッチャーを取得したいチケットオブジェクト

    Returns:
        dict[str, str]: ウォッチャーNをキーとした、IDと名前の値を保持するdict
    """
    watcher: dict = {}
    min_index = 0
    if min_index < len(issue_r.watchers):
        for index, watcher_info in enumerate(issue_r.watchers):
            watcher[f"ウォッチャー{index}"] = f"ID={watcher_info.id} NAME={watcher_info.name}"
    else:
        watcher[f"ウォッチャー{min_index}"] = ""

    return watcher


def get_issue_dict(issue_r: Issue) -> dict:
    """チケットオブジェクトからチケット情報のdictを取得する

    Args:
        issue_r (Issue): 情報を取得したいチケットオブジェクト

    Returns:
        dict: 一連の情報を保持したdict
    """
    attr_dict_list = {}
    attr_dict_list.update(get_ticket_id(issue_r))
    attr_dict_list.update(get_watcher(issue_r))

    return attr_dict_list


def show_issue_list(issue_list_r: ResourceSet) -> None:
    for now_cnt, iss in enumerate(issue_list_r):
        issue_count = f"iss:{now_cnt:0{get_digits_in_list_length(issue_list_r)}}"
        issue_dict = get_issue_dict(iss)
        issue_list = [issue_count, issue_dict]
        print(issue_list)


def main() -> None:
    redmine = get_redmine_obj()
    get_users(redmine)
    projects = get_projects(redmine)

    for cnt, project in enumerate(projects):
        prj_name = project.identifier
        print(f"{cnt:0{get_digits_in_list_length(projects)}}:{prj_name}")

        issues = redmine.issue.filter(project_id=prj_name, status_id="*")
        show_issue_list(issues)


if __name__ == "__main__":
    main()
