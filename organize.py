import os
import shutil

def getFiles(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def getDirectories(path):
    result = []
    for file in os.listdir(path):
        if not os.path.isfile(os.path.join(path, file)):
            result.append(file)
    return result

def main():
    DOWNLOAD_PATH = os.path.expanduser('~\Downloads')
    files = getFiles(DOWNLOAD_PATH)
    folders_created = getDirectories(DOWNLOAD_PATH)
    
    # For now this code will only work in windows
    if os.name == "nt":
        for file in files:
            name, extension = os.path.splitext(file)
            if extension in folders_created:
                try:
                    shutil.move(f"{DOWNLOAD_PATH}\\{file}", f"{DOWNLOAD_PATH}\\{extension}")
                except:
                    print(f"While moving '{file}' to the folder '{extension}' we encountered a file with the same name.")
            else:
                try:
                    os.mkdir(f"{DOWNLOAD_PATH}\\{extension}")
                    folders_created.append(extension)
                    shutil.move(f"{DOWNLOAD_PATH}\\{file}", f"{DOWNLOAD_PATH}\\{extension}")
                except NameError as err:
                    print(f"Couldn't create a file to locate this file: {file}")


if __name__ == "__main__":
    main()