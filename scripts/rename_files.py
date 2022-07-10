import os
import shutil

path = '../arrays_list/array_questions'
for subdir, dirs, files in os.walk(path):
    for file in files:
        # print(file)
        file_new = file.lower().replace(" ", "_")
        print(os.path.join(path, file))
        print(os.path.join(path, file_new))
        shutil.move(os.path.join(path, file), os.path.join(path, file_new))
