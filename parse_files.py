import subprocess as sp
from pathlib import Path

cert_output_file = open("./cert_parse.txt", 'w')
pem_output_file = open("./pem_parse.txt", 'w')
key_output_file = open("./key_parse.txt", 'w')

class VarsFile:
    def __init__(self):
        self.hostname_list = []
        self.filenames = []
    
    def generate_file_list(self, path):
        self.cmd = "ls " + path
        self.p = sp.Popen(self.cmd,shell=True, stdout=sp.PIPE)

        for line in self.p.stdout:
            line = line.decode("utf-8")
            self.hostname_list.append(line.strip())
        return self.hostname_list

varsfile = VarsFile()
varsfile.generate_file_list("/opt/ansible/wildcard_find/certs")

# Generate Ansible vars file
for i in varsfile.hostname_list:
  cert_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_cert.txt"
  read_file = open(cert_file, 'r')
  cert_output_file.write(f"{i}: \n")
  for line in read_file:
    if "wildcard" in line:
      cert_output_file.writelines(f"  - {line}")

for i in varsfile.hostname_list:
  pem_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_pem.txt"
  read_file = open(pem_file, 'r')
  pem_output_file.write(f"{i}: \n")
  for line in read_file:
    if "wildcard" in line:
      pem_output_file.writelines(f"  - {line}")

for i in varsfile.hostname_list:
  key_file_verify =  Path(f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_key.txt")
  key_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_key.txt"
  if key_file_verify.is_file():
    read_file = open(key_file, 'r')
    key_output_file.write(f"{i}: \n")
    for line in read_file:
      if "wildcard" in line:
        key_output_file.writelines(f"  - {line}")

