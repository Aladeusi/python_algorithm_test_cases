"""
This component of "autodeploy" dev-ops deployment pipeline 
pushes your projects, sources or libraries to github from 
your local machine on schedule basis.
"""
from toolbox import tb_shell 
import datetime


config={
    "repo_origin":"https://github.com/Aladeusi/python_algorithm_test_cases.git",
    "repo_local_path":"C:\\inetpub\python\\algorithms\\python_algorithm_test_cases",
    "account_username":"Aladeusi",
    "account_password":"Alad3iu5!"
}

def is_not_staged(res):
   status=True if "what will be committed" in res else False
   return status

def yet_to_commit(res):
   status=True if "Changes to be committed" in res else False
   return status

def uplink():
   res = tb_shell("cd "+config["repo_local_path"]+" & git status")
   if is_not_staged(res) or yet_to_commit(res):
      push_command="cd "+config["repo_local_path"]+" & git add --all & git commit -m '"+ str(datetime.datetime.now())+"' & git push "+config['repo_origin']+" master"
   return tb_shell(push_command)
        
# deploy repo specified in config        
response = uplink()

