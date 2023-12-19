# Code for converting folder structure to uml

import os

base_path = "/Users/snathani/PycharmProjects/data-structures/arrays_list/array_questions_geeksforgeeks"
# base_path = "/Users/snathani/PycharmProjects/data-structures/arrays_list"
base_path = "/Users/snathani/PycharmProjects/data-structures/stack"
def convert_folder_to_mindmap1(base_path, count):
    # print("Count = " + str(count))
    count = count + 1

    for root, dirs, files in os.walk(base_path):
        # print("base path: " + base_path)
        # print("dirs: " + str(dirs))
        # print("files: " + str(files))
        # import sys; sys.exit()
        if dirs:
            dirs = sorted(dirs)
            # print("dirs: " + str(dirs))
            for d in dirs:
                str_star = "*" * count
                print(str_star + " " + str(d))
                convert_folder_to_mindmap1(base_path + "/" + d, count)
        # else:
        #     print("No more folders")
        # else:
            # print( files)
        # print("base_path2: " + base_path)
        files = sorted(files)
        for f in files:
            str_star = "*" * count
            print(str_star + " " + str(f))

            # print(root + "/" + f)
            with open(root + "/" + f, 'rb') as fopen:
                line = fopen.readlines()
                if line:
                    # print(line)
                    first_line = line[0]
                    if "TODO" in str(first_line):
                        print(str_star + "* " + str(first_line.decode("utf-8").strip()))
        # print("End of a loop")
        break

def convert_folder_to_mindmap2(base_path, count):
    for root, dirs, files in os.walk(base_path):
        if dirs:
            dirs = sorted(dirs)
            print("dirs: " + str(dirs))
            for d in dirs:
                base_path = base_path + "/" + d
                convert_folder_to_mindmap2(base_path)
        else:
            print("*** " + str(files))
            files = sorted(files)
            for f in files:
                print("*** " + f)


if __name__ == '__main__':
    convert_folder_to_mindmap1(base_path, 1)