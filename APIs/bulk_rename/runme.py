import os
import sys

class NotInUse:
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

niu = NotInUse()

class Folder:
    def rename(self, folder_dir, new_name):
        if os.path.exists(folder_dir):
            os.rename(folder_dir, new_name)
        else:
            raise FileNotFoundError("Folder not found, Check the directory is correct")

folder = Folder()