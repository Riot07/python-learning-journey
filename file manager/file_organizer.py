import os
import shutil


folder = input("Enter the folder path: ")

images_folder = os.path.join(folder, "Images")
documents_folder = os.path.join(folder, "Documents")
videos_folder = os.path.join(folder, "Videos")
music_folder = os.path.join(folder, "Music")
other_folder = os.path.join(folder, "Others")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(documents_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True)
os.makedirs(music_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

files = os.listdir(folder)


for file in files:

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        file_name, file_extension = os.path.splitext(file)

        file_extension = file_extension.lower()

        if file_extension in [".jpg", ".jpeg", ".png"]:
            destination = images_folder

        elif file_extension in [".pdf", ".docx", ".txt"]:
            destination = documents_folder

        elif file_extension in [".mp4", ".mkv", ".avi"]:
            destination = videos_folder

        elif file_extension in [".mp3", ".wav", ".flac", ".ogg", ".m4a"]:
            destination = music_folder

        else:
            destination = other_folder

        destination_path = os.path.join(destination, file)

        try :
            shutil.move(file_path, destination_path)
            print("Moved:", file)

        except shutil.Error:
            print("Could not move file: " ,file)
        except OSError:
            print("Could not moce file: ",file)
            
