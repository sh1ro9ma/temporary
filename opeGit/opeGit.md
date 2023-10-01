
## 環境準備

### 定番の用意

いつもの

    pipenv --python 3.9
    pipenv install --skip-lock flake8

### GitPython

    pipenv install --skip-lock GitPython

    [GitPython official](https://pypi.org/project/GitPython/)

    https://gitpython.readthedocs.io/en/stable/


    Name: GitPython
    Version: 3.1.37
    Summary: GitPython is a Python library used to interact with Git repositories
    Home-page: https://github.com/gitpython-developers/GitPython
    Author: Sebastian Thiel, Michael Trier
    Author-email: byronimo@gmail.com, mtrier@gmail.com
    License: BSD
    Location: d:\work\redmine\.venv\lib\site-packages
    Requires: gitdb
    Required-by:

    Name: gitdb
    Version: 4.0.10
    Summary: Git Object Database
    Home-page: https://github.com/gitpython-developers/gitdb
    Author: Sebastian Thiel
    Author-email: byronimo@gmail.com
    License: BSD License
    Location: d:\work\redmine\.venv\lib\site-packages
    Requires: smmap
    Required-by: GitPython

    Name: smmap
    Version: 5.0.1
    Summary: A pure Python implementation of a sliding window memory map manager
    Home-page: https://github.com/gitpython-developers/smmap
    Author: Sebastian Thiel
    Author-email: byronimo@gmail.com
    License: BSD
    Location: d:\work\redmine\.venv\lib\site-packages
    Requires:
    Required-by: gitdb

## 参考サイト

https://qiita.com/kanedaq/items/1f7e294b147a348fbe7e

## 認証情報の管理

Winキー
"Env" 入力
変数名： PY_USERNAME_TEST
変数値： py-test-name

    import os
    username = os.environ.get('MY_USERNAME')
    password = os.environ.get('MY_PASSWORD')
