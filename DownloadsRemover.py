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


def delete(num, to_spare, decision, move):
    message = True
    while move:
        if num == 0:
            if message:
                print("There is no files to be removed.")
            move = False
        else:
            message = False
            for filename in files:
                if filename not in to_spare:
                    file = '/home/jakub/Downloads/' + filename
                    os.remove(file)
                num -= 1

            print("removed.")

    print(files)


def main():
    num_of_files = counter(directory)
    decision = ask()
    while decision != "y" and decision != "n":
        decision = input("y/n")
    if decision == "n":
        files_to_spare = changes()
        delete(num_of_files, files_to_spare, decision, move=True)
    else:
        delete(num_of_files, None, decision, move=True)


main()
