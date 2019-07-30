import subprocess as sp
from pathlib import Path

cert_file = []
pem_file = []
cert_output_file = open("./cert_parse.txt", 'w')
pem_output_file = open("./pem_parse.txt", 'w')
key_output_file = open("./key_parse.txt", 'w')

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
    if "allstar" in line:
      cert_output_file.writelines(f"  - {line}")

for i in hostnames:
  pem_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_pem.txt"
  read_file = open(pem_file, 'r')
  pem_output_file.write(f"{i}: \n")
  for line in read_file:
    if "allstar" in line:
      pem_output_file.writelines(f"  - {line}")

for i in hostnames:
  key_file_verify =  Path(f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_key.txt")
  key_file = f"/opt/ansible/wildcard_find/certs/{i}/var/tmp/{i}_search_key.txt"
  if key_file_verify.is_file():
    read_file = open(key_file, 'r')
    key_output_file.write(f"{i}: \n")
    for line in read_file:
      if "allstar" in line:
        key_output_file.writelines(f"  - {line}")

