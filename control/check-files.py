
"""
offline file checker - for each file in notebook dir :
- checks if export has ever been made (if it exists for that file)
- checks if an export has already been made since the last time the export happened 
"""

import configparser
import time
import os

#user
import GUIDEBOOK_FUNCTIONS as GF

CONTROL_DIR = '..\\control'
NOTEBOOKS_DIR = '..\\notebooks'
HTML_EXPORTS_DIR = os.path.abspath('..\\notebooks-html') #juypter needs an absolute path location 
EXPORT_SCRIPT = 'export-ipynb-html.py' 
LOG_FILE = 'info.ini' #log file - has last export time ; if = 0 ; never exported 

#open the log ini file
configp = configparser.ConfigParser()
configp.read(LOG_FILE)

LAST_EXPORT_TIME = configp['DEFAULT'].getint('last_export_time')

# Change to the notebooks directory
os.chdir(NOTEBOOKS_DIR)

#get all html files currently inside the html dir
html_exports = html_files = [f for f in os.listdir(HTML_EXPORTS_DIR) if f.endswith('.html')]

for ipynb_file in os.listdir(NOTEBOOKS_DIR):
    #for each notebook 
    
    #get actual path ?
    ipynb_path = os.path.abspath(ipynb_file)

    #get file name
    ipynb_filename = os.path.splitext(ipynb_file)[0]

    if os.path.isfile(ipynb_path):  

        #modification time - last change was made to a file 
        last_modified_time = os.path.getmtime(ipynb_path) 

        html_name = f"{ipynb_filename}.html"

        #check if it even has html export or if it was last modified after the last export ; newer time -> bigger + check if it has any cells
        if  GF.IS_notebook_valid(ipynb_path) and (html_name not in html_files or last_modified_time<=LAST_EXPORT_TIME):

            print(f"exporting : {ipynb_filename} last modified on: {GF.GET_readable_time(last_modified_time)}")
            #export it 
            
            os.system(f'jupyter nbconvert --to html --execute {ipynb_path} --output-dir {HTML_EXPORTS_DIR}')

#change to the notebooks directory
os.chdir(CONTROL_DIR)

#update last full export/check time
new_time = int(time.time())

print(f'time updated from {GF.GET_readable_time(LAST_EXPORT_TIME)} to: {GF.GET_readable_time(new_time)}')

configp['DEFAULT']['last_export_time'] = str(new_time)

#update the ini file
with open(LOG_FILE, 'w') as configfile:
    configp.write(configfile)
