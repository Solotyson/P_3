import os

folder_path = r"D:\Sem 3\Prog_3\prac_2\P_3"
file_name = "writeme.txt"

file_path = os.path.join(folder_path, file_name)

# Read only ('r')
# Read and Write ('r+')
# Write only (w)
# Write and Read ('w+')
# Append only ('a')
# Append and Read ('a+')

file_obj = open(file_path, 'w')
input_text = "Puneker na majha namaskar, me Shantanu "

file_obj.write(input_text)
file_obj.close()

print("Process completed")
