import os
import shutil
import sys

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


def fancyNames(folders_created, extensions_name, path):
    for folder in folders_created: 
        if folder in extensions_name:
            os.rename(f"{path}\\{folder}", f"{path}\\{extensions_name[folder]}")


def main() -> None:

    EXTENSIONS_NAME = {
        ".pptx" : "Powerpoint presentations",
        ".jpg" : "JPG Photos",
        ".png" : "PNG Photos", 
        ".exe" : "Executables",
        ".py"  : "Python Files",
        ".pdf" : "PDFs",
        ".xlsx" : "Excels Files",
        ".cvs" : "Comma Separated Values",
        ".docx" : "Word Documents",
        ".gif" : "GIFs",
        ".mp4" : "MP4 Videos",
        ".zip" : "Compressed Folders",
        ".sql" : "SQL Database Files",
        ".rkt" : "Racket Files"
        }

    DOWNLOAD_PATH = os.path.expanduser('~\Downloads')

    if len(sys.argv) > 1:
        OPTIONS = sys.argv[1::]
    else:
        OPTIONS = []

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

        if "-f" in OPTIONS:
            fancyNames(folders_created, EXTENSIONS_NAME, DOWNLOAD_PATH)

            



if __name__ == "__main__":
    main()