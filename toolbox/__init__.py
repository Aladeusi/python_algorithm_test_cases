import sqlite3
import html2text
import shlex
from subprocess import call as sp_call
from subprocess import Popen, PIPE



def sqlite_fetch(path, query):
    """
    Connects to sqlite database specified in {path}, runs query in {query} and returns array of records.\n
    Relies on sqlite3 library. Ensure that this library is available in your python enviroment.
    """
    # createing sqlite conection object
    connection = sqlite3.connect(path)
    # creating cursor object
    cursor=connection.cursor()
    # runing sql query to return record
    response= cursor.execute(query)
    #connection.close()
    return response

def convert_html2text(html_string):
    """
    Returns regular text of an html encoded string {html_string}.\n
    Relies on html2text library. Ensure that this library is available in your python enviroment.
    """
    return str(html2text.html2text(html_string).encode("utf-8")).replace("\\r\\n", "")



def tb_shell(command):
    """
    Execute shell command(s) and return output printed on the shell as string.
    """
    args = shlex.split(command)

    proc = Popen(args, stdout=PIPE, stderr=PIPE, shell=True)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return str(out)