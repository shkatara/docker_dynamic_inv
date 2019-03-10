########
IT NEEDS docker-py on the host that you are running ansible* commands from

1. pip install docker-py
2. Will only work on containers that does have python installed


USAGE
######


ansible -i dynamic_inventory.py all -m command -a hostname -c docker
