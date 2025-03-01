def write_list_file(file_path, data_path):
    try:
        with open(file_path, 'w') as lol:
            for item in data_path:
                lol.write(str(item)+"\n")
        print("List written !")
    except:
        print("Error")

data=["Apple", "Banana", "Cherry", "12345", "loool"]
file="C:\\destination\\Rauan_Tuken_PP2\\lab6\\lol.txt"
write_list_file(file, data)