# Labyrinth

This repository contains essential information to configure a testbed developed in the context of the H2020 Labyrinth European project.

### UAV: 
Required hardware:
* Raspberry Pi 4
* [Raspberry Pi 4G/LTE Cellular Modem Kit](https://sixfab.com/product/raspberry-pi-4g-lte-modem-kit/)

Required OS:
* Ubuntu server 20.04 LTS
### UAV controller:
Required harware:
* Mini ITX

Required OS:
* Ubuntu server 20.04 LTS

## How to install pyparrot in the UAV

Install the pyparrot in the UAV following the documentation:

[pyparrot’s documentation](https://pyparrot.readthedocs.io/en/latest/)

## How to install ansible in the UAV controller

1. Installation:
``` bash
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible
```

2. Include the IP of the UAV you want to manage using ansible in:
```bash
/etc/ansible/hosts
```

3. Passwordless SSH access from UAV controller to UAV:

To manage the UAV using ansible, you should connect using SSH without introducing the password manually:
[Passwordless SSH access](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)

4. Test the connectivity between the UAV controller and the UAV (from UAV controller):

```bash
ansible all -m ping -u uavuser
```

5. Run the ansible playbook (examples in /labyrinth/uavcontroller/ansibleplaybooks/)
```bash
ansible-playbook -vvv despegueaterrizaje.yml
```
