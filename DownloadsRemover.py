import os

folder = '/home/jakub/Downloads'
files = 0
for filename in os.listdir(folder):
    files += 1
    print(filename)

# os.remove('/home/jakub/Downloads/steam_latest.deb')
print(files)
