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
        temp = [item for item in input("Write the exact names (with blank spaces as separators)"
                                       " of the files to be spared, "
                                       "otherwise they'll be deleted permanently: ").split()]


move = True

num_of_files = counter(directory)

while move:
    ask()
    if num_of_files == 0:
        print("There is no files to be removed.")
        move = False
    else:
        for filename in files:
            if filename not in files_to_spare:
                file = '/home/jakub/Downloads/' + filename
                print(file)
            # os.remove(file)
            num_of_files -= 1

print(num_of_files)
