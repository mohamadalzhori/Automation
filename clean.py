# This is my first script, when run it takes one argument either a predefined keyword like "test" or a path to a folder to be cleaned
# Cleaning here means organizing but "clean" is just easier :), files are organized into Documents, Videos, Pictures, Zips, Exe, and Others
import os
import sys

# Define the folder where the files are located
# folder = "C:\\Users\\Mohamad Alzhori\\Desktop\\test"

# To accept parameter of the folder to be organized
folder = sys.argv[1]

# Replace argument by actual path
if folder == "test":
    folder = "C:\\Users\\Mohamad Alzhori\\Desktop\\test"
# Define the folder names for each file type
documents_folder = "Documents"
videos_folder = "Videos"
pictures_folder = "Pictures"
other_folder = "Other"
zips_folder = "Zips"
exe_folder = "Exe"

# Create the full path for each folder
documents_folder_path = os.path.join(folder, documents_folder)
videos_folder_path = os.path.join(folder, videos_folder)
pictures_folder_path = os.path.join(folder, pictures_folder)
other_folder_path = os.path.join(folder, other_folder)
zips_folder_path = os.path.join(folder, zips_folder)
exe_folder_path = os.path.join(folder,exe_folder)

# Iterate through the files in the folder
for item in os.listdir(folder):
    # Get the file path
    file_path = os.path.join(folder, item)

    # Check if the item is a file
    if os.path.isfile(file_path):
        # Get the file extension
        extension = item.split(".")[-1]

        # Determine the folder to move the file to
        if extension == "pdf":
            if not os.path.exists(documents_folder_path):
                os.mkdir(documents_folder_path)
            os.rename(file_path, os.path.join(documents_folder_path, item))
        elif extension in ["mp4", "mkv", "avi"]:
            if not os.path.exists(videos_folder_path):
                os.mkdir(videos_folder_path)
            os.rename(file_path, os.path.join(videos_folder_path, item))
        elif extension in ["jpg", "jpeg", "png", "bmp"]:
            if not os.path.exists(pictures_folder_path):
                os.mkdir(pictures_folder_path)
            os.rename(file_path, os.path.join(pictures_folder_path, item))
        elif extension in ["zip", "rar", "7z"]:
            if not os.path.exists(zips_folder_path):
                os.mkdir(zips_folder_path)
            os.rename(file_path, os.path.join(zips_folder_path, item))
        elif extension in ["exe", "msi"]:
            if not os.path.exists(exe_folder_path):
                os.mkdir(exe_folder_path)
            os.rename(file_path, os.path.join(exe_folder_path, item))
        else:
            if not os.path.exists(other_folder_path):
                os.mkdir(other_folder_path)
            os.rename(file_path, os.path.join(other_folder_path, item))

#os.system("pause")
