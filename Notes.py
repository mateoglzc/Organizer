# Automation Notes

# import system library
import os
import shutil

print(f"The os name is: {os.name}")

# Current Working Directory
# print(os.getcwd())

# To print absolute path on your system 
# print(os.path.abspath())
  
# To print files and directories in the current directory on your system
# print(os.listdir()) 

def files(path):
    for file_ in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_)):
            yield file_

def directories(path):
    for nfile in os.listdir(path):
        if os.path.isfile(os.path.join(path, nfile)):
            pass
        else:
            yield nfile

DOWNLOAD_PATH = os.path.expanduser('~\Downloads')
Dowload_folder = list(files(DOWNLOAD_PATH))
folders_created = list(directories(DOWNLOAD_PATH))

if os.name  == "nt":
    for file_ in Dowload_folder:
        name, extension = os.path.splitext(file_)
        if extension in folders_created:
            shutil.move(f"{DOWNLOAD_PATH}\\{file_}", f"{DOWNLOAD_PATH}\\{extension}")
        else:
            try:
                os.mkdir(f"{DOWNLOAD_PATH}\\{extension}")
                folders_created.append(extension)
                shutil.move(f"{DOWNLOAD_PATH}\\{file_}", f"{DOWNLOAD_PATH}\\{extension}")
            except FileExistsError as err:
                print(f"Couldn't create a file to locate this file: {file_}")