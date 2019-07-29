```
Python script to take data returned from Ansible and extract
relevant data and combine into two var files for ansible
```
import subprocess as sp

cert_file = []
pem_file = []
cert_output_file = open("./cert_parse.txt", 'w')
pem_output_file = open("./pem_parse.txt", 'w')

# Generate list based on directory names
def generate_file_list(path):
  hostname_list = []
  cmd = "ls " + path
  p = sp.Popen(cmd,shell=True, stdout=sp.PIPE)

  for line in p.stdout:
    line = line.decode("utf-8")
    hostname_list.append(line.strip())
  return hostname_list

hostnames = generate_file_list("/opt/ansible/wildcard_find/certs")

# Generate Ansible vars file
for i in hostnames:
  cert_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_cert.txt"
  read_file = open(cert_file, 'r')
  cert_output_file.write(f"{i}: \n")
  for line in read_file:
    if "wildcard" in line:
      cert_output_file.writelines(f"  - {line}")

for i in hostnames:
  pem_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_pem.txt"
  read_file = open(pem_file, 'r')
  pem_output_file.write(f"{i}: \n")
  for line in read_file:
    if "wildcard" in line:
      pem_output_file.writelines(f"  - {line}")
