# The aim of this script is to prepare a folder to be organized by another script called clean (Oh wait, may be I should merge them or make one call another)
# This scripts goes into all subfolders and subfolders of subfolders etc. and moves all files back to the main directory

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
