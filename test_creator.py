import sys

file_name = sys.argv[1]
# file_name = r'D:\proyectos\test_creator\1.sql'
file = open(file_name, 'r')
file_content = file.read()
file_content_list = file_content.split('\n')
file_content = file_content.replace('\t', '').replace('\n', '')
example_data = "("
for x in range(5):
    for row in file_content_list:
        if 'CREATE' in row:
            pass
        elif 'int' in row:
            # get first word of the string 
            example_data += row.split(' ')[0] + ' 1' + ", "
        elif  'float' in row or 'double' in row or 'decimal' in row:
            example_data += row.split(' ')[0] + ' 1.1' + ", "
        elif 'varchar' in row:
            example_data += row.split(' ')[0] + " 'test1'" + ", "
        elif 'date' in row or 'datetime' in row or 'timestamp' in row:
            example_data += row.split(' ')[0] + " 01-01-2022" + ", "
        elif 'char' in row:
            example_data += row.split(' ')[0] + " 't'" + ", "
    if x < 4:
        example_data = example_data[:-2] + "),\n("
    else:
        example_data = example_data[:-2] + ");"

print(example_data)