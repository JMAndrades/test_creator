import sys, re
# file_name = sys.argv[1]
file_name = r'DDL.sql'
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
for x in range(1,6):
    cont2 = 0
    example_data += "("
    for line in file_content:
        words = line.split(" ")
        if len(words) > 1:
            if  'CONSTRAINT' in line.upper() or 'IDENTITY' in line.upper():
                pass
            elif 'int' in words[1] or 'bigint' in words[1] or 'smallint' in words[1] or 'tinyint' in words[1]:
                example_data += f"{words[0]}={x}, "
                cont2 += 1
            elif 'date' in words[1] or 'datetime' in words[1] or 'date2' in words[1] or 'datetime2' in words[1] or 'time' in words[1] or 'time2' in words[1] or 'datetimeoffset' in words[1]:
                example_data += f"{words[0]}='2022-08-0{x}', "
                cont2 += 1
            elif 'decimal' in words[1] or 'float' in words[1]:
                example_data += f"{words[0]}={x}.{x-1}, "
                cont2 += 1
            elif 'varchar' in words[1] or 'nvarchar' in words[1] or 'char' in words[1] or 'nchar' in words[1] or 'varbinary' in words[1] or 'binary' in words[1]:
                longitud = int(re.sub("\).*$","",(re.sub(".*?\(","",words[1]))))
                # longitud = re.sub("\).*$","",(re.sub(".*?\(","",words[1])))
                print(longitud)
                test = "test"[:longitud-1]
                example_data += f"{words[0]}='{test}{x}', "
                cont2 += 1
            elif 'bit' in words[1]:
                if x % 2 == 0:
                    example_data += f"{words[0]}=1, "
                else:
                    example_data += f"{words[0]}=0, "
                cont2 += 1
    if x < 5:
        example_data = example_data[:-2] +"),\n"
    else:
        example_data = example_data[:-2] +");"
example_data = re.sub("\[|\]","",example_data)
print(example_data)
if cont1 != cont2:
    print("There is something wrong!")
    print(f"{cont1} rows read")
    print(f"{cont2} rows written")