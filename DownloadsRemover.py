import os

directory = '/home/jakub/Downloads'
files = []


def display(folder):
    num = 0
    for f in os.listdir(folder):
        files.append(f)
        num += 1
    return num


move = True

num_of_files = display(directory)

while move:
    if num_of_files == 0: 
        print("There is no files.")
        move = False
    else:
        for filename in files:
            file = '/home/jakub/Downloads/' + filename
            print(file)
            # os.remove(file)
            num_of_files -= 1

print(num_of_files)
