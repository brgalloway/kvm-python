import subprocess as sp

docker_command = ["docker run --detach -ti --privileged",
                "--hostname chef-server -p 8444:443",
                "-p 8081:80 -p 2222:22", "--name chef-server",
                "-v /opt/chef-server/chef-data/var/opt:/var/opt",
                "--restart always cbuisson/chef-server:latest" ]

sp.call(" ".join(docker_command), shell=True)
