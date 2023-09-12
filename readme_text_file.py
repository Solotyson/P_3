import os

folder_path = r"D:\Sem 3\Prog_3\prac_2"
file_name = "readme.txt"

file_path = os.path.join(folder_path, file_name)


file_obj = open(file_path, 'r')

# print(file_obj.read())

# print(file_obj.readline())

# print(file_obj.readlines())

lines = file_obj.readlines()

count = 1
for line in lines:
    print("{} - {}".format(count, line))
    count = count + 1
