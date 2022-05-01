import re

f = open("human_c.obj")
fo = open("human_c.smf", "w")

line = f.readline()
while line:
    if line[0] == 'v' and line[1] != 'n':
        print(line)
        fo.write(line)
    elif line[0] == 'f':
        line = line.replace("//", " ")
        line_list = line.split()
        new_line = line_list[0] + " " + line_list[1] + " " + line_list[3] + " " + line_list[5] + "\n"
        print(new_line)
        fo.write(new_line)
    line = f.readline()

f.close()
fo.close()