from genericpath import exists, isfile
import os
import sys
import datetime
req_path = input("Enter your path: ")
age = 3  # No of days older than
if not os.path.exists(req_path):
    print("Please provide valid path")
if os.path.isfile(req_path):
    print("Please provide directory path")
    sys.exit(2) #2 means no return exit code; 1 means return exit code True
today = datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_create_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        diff_days = (today - file_create_date).days
        if diff_days > age:
            print(each_file_path, diff_days)
