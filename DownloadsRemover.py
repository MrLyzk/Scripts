import os

directory = '/home/jakub/Downloads'
files = []


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
    return decision


def changes():
    temp = [item for item in input("Write the exact names (with blank spaces as separators)"
                                   " of the files to be spared, "
                                   "otherwise they'll be deleted permanently: ").split()]
    return temp


def delete(num, to_spare):
    while True:
        if num == 0:
            print("There is no files to be removed.")
            break
        else:
            for filename in files:
                if filename not in to_spare:
                    file = '/home/jakub/Downloads/' + filename
                    print(file)
                    # os.remove(file)
                num -= 1

    print(files)


def main():
    num_of_files = counter(directory)
    decision = ask()
    if decision == "n":
        files_to_spare = changes()
        delete(counter(directory), files_to_spare)


main()
