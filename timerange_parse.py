import re

file_path_01 = "./files/10.1.1."
file_name = "/var/log/httpd/access.log-20190307"
server_list = [95, 96, 97, 98, 102, 103, 104, 105]
output_file = open("./parsed_out.txt", 'w')

for i in range(len(server_list)):
    read_file = open(file_path_01 + str(server_list[i]) + file_name, 'r')
    for line in read_file:
        if re.match("^(.*?06/Mar/2019:(0[6-9]))", line) and re.match("^(.*?ts=pd)", line):
                output_file.writelines(line)

output_file.close()
