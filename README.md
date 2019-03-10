IT NEEDS docker-py on the host that you are running ansible* commands from

1. pip install docker-py.
2. Will only work on containers that does have python installed.

USAGE
######
Tested with the official centos docker image, as it does have python and I am lazy enough to put python in any other image, for example, the official httpd image.

Not tried, but can use an alpine image with having python installed in it, and it might just work.

ansible -i dynamic_inventory.py all -m command -a hostname -c docker
