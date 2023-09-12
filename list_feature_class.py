import arcpy

arcpy.env.workspace = r"D:\Sem 3\Prog_3\Practical_3_ProProject\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"

# Creating a list of feature classes in the current workspace
fc_list = arcpy.ListFeatureClasses()

for fc_name in fc_list:
    print(fc_name)

print("-------------------------------")

# List of field objects for the specific  feature classes in the current workspace

field_list = arcpy.ListFields("Freeways")

for field in field_list:
    print(field.name)
    print(field.type)
    print(field.length)
    print("------------------")