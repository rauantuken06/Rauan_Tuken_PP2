import os
def file_deleter(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.X_OK):
            try:
                os.remove(file_path)
                print(f"{file_path} file deleted !")
            except:
                print("Error")
        else:
            print("You don't have to write access")
    else:
        print("Such file does not exist")

del_path="C:\\destination\\Rauan_Tuken_PP2\\lab6\\lol.py"
file_deleter(del_path)