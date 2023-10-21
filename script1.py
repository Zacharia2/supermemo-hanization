import re
import csv
# 使用正则表达式匹配id和值

e_dic = {}
c_dic = {}

e_file = "sm18cs_3.txt"
c_file = "sm18cs_1.txt"


def has_chinese_character(string):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    match = pattern.search(string)
    if match:
        return True
    else:
        return False
    

with open(e_file, "r") as file:
    lines = file.read()
    # print(lines)
    matches = re.findall(r'@(\d+)\s+.*\n(.*)', lines)
    for match in matches:
        e_dic[match[0]] = match[1]
print(e_dic)


with open(c_file, "r") as file:
    lines = file.read()
    # print(lines)
    matches = re.findall(r'@(\d+)\s+.*\n(.*)', lines)
    for match in matches:
        c_dic[match[0]] = match[1]
print(c_dic)


def convert_dict_to_list(d1,d2):
    result = []
    for key1, value1 in d1.items():
        if key1 in d2:
            if has_chinese_character(d2[key1]):
                result.append([value1, d2[key1]])
    return result

list = convert_dict_to_list(e_dic,c_dic)

print(list)
#python2可以用file替代open
with open("test.csv","w") as csvfile: 
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(["a_name","b_name"])
    #写入多行用writerows
    writer.writerows(list)