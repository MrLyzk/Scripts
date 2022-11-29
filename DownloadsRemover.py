import os

directory = '/home/jakub/Downloads'
files = []
files_to_spare = []


def counter(folder):
    num = 0
    for f in os.listdir(folder):
        files.append(f)
        num += 1
    return num


def ask():
    for i in files:
        print(i)

    decision = input("Do you want to remove all the given files? (y/n):\n")

    if decision == "n":
        files_to_spare.append(input("Write the exact name of the file to be spared, "
                                    "otherwise it'll be deleted permanently: "))


move = True

num_of_files = counter(directory)

while move:
    ask()
    if num_of_files == 0: 
        print("There is no files.")
        move = False
    else:
        for filename in files:
            if filename not in files_to_spare:
                file = '/home/jakub/Downloads/' + filename
                print(file)
            # os.remove(file)
            num_of_files -= 1

print(num_of_files)
