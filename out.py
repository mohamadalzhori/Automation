import os
import shutil
import sys

def extract_files(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            shutil.move(file_path, directory)
            

folder = sys.argv[1]
# Replace argument by actual path
if folder == "test":
    folder = "C:\\Users\\Mohamad Alzhori\\Desktop\\test"

extract_files(folder)

#os.system("pause")