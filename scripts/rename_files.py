import os
import shutil

path = '../arrays_list/array_questions'
for root, dirs, files in os.walk(path):
    for file in files:
        # print(file)
        file_new = file.lower().replace(" ", "_")
        # matches.append(os.path.join(root, filename))

        print(os.path.join(root, file))
        print(os.path.join(root, file_new))
        shutil.move(os.path.join(root, file), os.path.join(root, file_new))
