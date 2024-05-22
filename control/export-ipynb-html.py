
#used by both github workflow/hook and no git 
#log file - has last export time ; if = 0 ; never exported 

import configparser
import time
import os


NOTEBOOKS_DIR = '..\\notebooks'
HTML_EXPORTS_DIR = '..\\notebooks-html'
LOG_FILE = 'info.ini'

configp = configparser.ConfigParser()
configp.read(LOG_FILE)

LAST_EXPORT_TIME = configp['DEFAULT'].getint('last_export_time')

html_exports = html_files = [f for f in os.listdir(HTML_EXPORTS_DIR) if f.endswith('.html')]

for ipynb_file in os.listdir(NOTEBOOKS_DIR):
    #for each notebook 
    
    #get actual path ?
    ipynb_path = os.path.join(NOTEBOOKS_DIR, ipynb_file)

    #get file name
    ipynb_filename = os.path.splitext(ipynb_file)[0]

    if os.path.isfile(ipynb_path):  

        last_modified_time = os.path.getmtime(ipynb_path) #modification time - last change was made to a file 

        #check if it even has html export or if it was last modified after the last export
        if f"{ipynb_filename}.html" not in html_files or last_modified_time<=LAST_EXPORT_TIME:
            #export it 
            print('[USER; export-ipynb-htmml] exporting file '+ipynb_filename)    


configp['DEFAULT']['last_export_time'] = str(time.time())

#update the ini file
with open(LOG_FILE, 'w') as configfile:
    configp.write(configfile)
