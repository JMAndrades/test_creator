import sys, re
# file_name = sys.argv[1]
file_name = r'1.sql'
file = open(file_name, 'r')
file_content = file.readlines()
example_data = "INSERT INTO "
cont1 = 0
for line in file_content:
    if line == ')' or line == ");" or 'CONSTRAINT' in line.upper() or 'IDENTITY' in line.upper():
            pass
    elif 'CREATE' in line:
        table_name = re.sub("\(","",line.split(" ")[2])
        example_data += f"{table_name} ("
    else:
        nombre = re.sub("\\\\t","",line.split(" ")[0]).strip()
        example_data += f"{nombre}, "
        cont1 += 1
example_data = example_data[:-2] + ") VALUES\n"
for x in range(1,5):
    cont2 = 0
    example_data += "("
    for line in file_content:
        if 'CONSTRAINT' in line.upper():
            pass
        if 'IDENTITY' in line.upper():
            pass
        elif ' int ' in line or ' bigint ' in line or ' smallint ' in line or ' tinyint ' in line:
            example_data += f"{x}, "
            cont2 += 1
        elif ' date ' in line or ' datetime ' in line or ' date2 ' in line or ' datetime2' in line or ' time ' in line or ' time2 ' in line or ' datetimeoffset ' in line:
            example_data += f"'2022-08-0{x}', "
            cont2 += 1
        elif ' decimal(' in line or ' float(' in line:
            example_data += f"{x}.{x-1}, "
            cont2 += 1
        elif ' varchar ' in line or ' nvarchar ' in line or ' char' in line or ' nchar' in line or ' varbinary' in line or ' binary' in line:
            # longitud = int(re.sub("\).*$","",(re.sub(".*?\(","",line))))
            longitud = re.sub("\).*$","",(re.sub(".*?\(","",line)))
            print(longitud)
            test = "test"[:longitud-1]
            example_data += f"'{test}{x}', "
            cont2 += 1
        elif ' bit ' in line:
            if x % 2 == 0:
                example_data += f"1, "
            else:
                example_data += f"0, "
            cont2 += 1
    if x < 4:
        example_data = example_data[:-2] +"),\n"
    else:
        example_data = example_data[:-2] +");"
example_data = re.sub("\[|\]","",example_data)
print(example_data)
if cont1 != cont2:
    print("There is something wrong!")
    print(f"{cont1} rows read")
    print(f"{cont2} rows written")