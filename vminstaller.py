import subprocess, shlex
from sys import argv

Type = [] 

def distro():
    name = raw_input("New VM's name: ")
    ram = raw_input("RAM to assign: ")
    vcpus = raw_input("Number of CPUs: ")
    cdrom = raw_input("Location of CDROM: ")
    disk = raw_input("Path to create disk: ")
    size = raw_input("Size of HDD: ")
    
    Type = (name,ram,vcpus,cdrom,disk,size)
    return(Type)

def installer(distro):
    distro = distro.lower()
    if distro == "ubuntu":
        Type = distro()
        command = "virt-install --name {0} --ram {1} " \
                  "--vcpus {2} --cdrom {3} --os-type linux " \
                  " --os-variant ubuntu16.04 --graphics " \
                  "vnc,listen=192.168.1.10 --hvm --virt-type kvm " \
                  "--disk path={4},size={5} --noautoconsole --livecd " \
                  " --network network=ovs-vmbr3,model=e1000".format(*Type)
        command = shlex.split(command)
        p = subprocess.Popen(command)
    else:
        print("Please define a distro")
        exit()
argv
installer(argv[1])
