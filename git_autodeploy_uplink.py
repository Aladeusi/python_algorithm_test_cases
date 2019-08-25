"""
This component of "autodeploy" dev-ops deployment pipeline 
pushes your projects, sources or libraries to github from 
your local machine on schedule basis.
"""
from shell import shell
import subprocess
import os
from toolbox import tb_shell 


config={
    "repo_origin":"",
    "repo_local_path":"C:\\inetpub\python\\algorithms\\python_algorithm_test_cases",
    "account_username":"Aladeusi",
    "account_password":"Alad3iu5!"
}

def uplink():
    res = tb_shell("")

res = git status
if 'untracked files present' in res:
    res=git add --all & git push origin master
    
