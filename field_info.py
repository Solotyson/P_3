import arcpy
import os

arcpy.env.workspace = r"D:\Sem 3\Prog_3\Practical_3_ProProject\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

folder_path = r"D:\Sem 3\Prog_3\prac_2\P_3"
output_text_file = "field_information.txt"
output_file_path = os.path.join(folder_path,output_text_file)

file_obj = open(output_file_path, "w")

fc_list = arcpy.ListFeatureClasses()

for name in fc_list:
    print(name)
    file_obj.write(name + "\n")

    field_list = arcpy.ListFields(name)
    for field in field_list:
        print("Name: {}, Type: {}, Length: {}".format(field.name, field.type, field.length))
        file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))

        print("------------------")
        file_obj.write("------------------\n")

file_obj.close()
print("Process completed")
