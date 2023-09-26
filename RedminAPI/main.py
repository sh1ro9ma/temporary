from redminelib import Redmine

import setting

redmine = Redmine(setting.redmineURL, key=setting.redmineKEY, requests={'verify': False})

print(redmine)
