import os
import shutil

def loopFolder(folderPath):
    # print(folderPath)
    for subdir, dirs, files in os.walk(folderPath):
        for file in files:
            # print(os.path.join(subdir, file))
            if not os.path.exists(os.path.join(folderPath, file)):
                shutil.move(os.path.join(subdir, file), folderPath)
            else:
                print("The file destination_file already exists.")            
    print('done!')
loopFolder("D:\\toTest")