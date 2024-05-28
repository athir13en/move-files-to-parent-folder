import os
import shutil

def loopFolder(folderPath):
    # print(folderPath)
    for subdir, dirs, files in os.walk(folderPath):
        for file in files:
            # print(os.path.join(subdir, file))
            shutil.move(os.path.join(subdir, file), folderPath)
    print('done!')
loopFolder("D:\\toTest")