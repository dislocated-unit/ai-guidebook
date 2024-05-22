
import subprocess
import nbformat
from nbconvert import HTMLExporter
import json
import time

"""
runs a given python script
"""
def RUN_python_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except Exception as e:
        print(f"ERR: handler-app-window: {e}")


"""
check if a notebook is empty 
"""
def IS_notebook_valid(notebook_path):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:

            notebook_content = json.load(f)

            if "cells" not in notebook_content or not notebook_content["cells"]:
                print(f"No Cells: {notebook_path}")
                return False
            
            return True       
                 
    except json.JSONDecodeError:
        return False
    
"""
get human readble time from time timestamp
"""

def GET_readable_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))