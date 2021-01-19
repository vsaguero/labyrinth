# Labyrinth

This repository contains essential information to configure a testbed developed in the context of the H2020 Labyrinth European project.

UAV -> Raspberry Pi 4
UAV controller -> miniITX

## How to install pyparrot in the UAV

Install the pyparrot in the UAV following the documentation:

[pyparrot’s documentation](https://pyparrot.readthedocs.io/en/latest/)

## How to install ansible in the UAV controller

Installation:
''' bash
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible
'''

Include the IP of the UAV you want to manage using ansible in:

/etc/ansible/hosts

Passwordless SSH access from UAV controller to UAV:

[Passwordless SSH access](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)


