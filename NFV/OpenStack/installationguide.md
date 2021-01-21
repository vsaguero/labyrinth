# Installation guide of OpenStack

#### Common for all interfaces in Ubuntu 20.04

+ Modify the "netplan" file, located in "/etc/netplan/00-installer-config.yaml" with the following information (it is mandatory to be superuser):

```
networks:
  ethernets:
    ens3:
      dhcp4: true
    ens4:
      addresses:
        - 10.0.0.11/24						\modify with the corresponding IP of your node
      routes:
          - to: 10.0.0.0/24
            via: 10.0.0.1
            metric: 100
    ens5: {}
  version: 2
```

+ Afterwards, it is mandatory to configure the ens5 interface according to OS. However, after Ubuntu 18.04 it has changed this operation quite a bit (in my opinion, it has worsen a lot but whatever...). Therefore, create the following file in the location "/etc/networkd-dispatcher/degraded.d/interfaceup.bash" and provide execution and ownership permissions to, at leastm the superuser (in this case all users):

```
#!/bin/bash

if [ $IFACE == "ens5" ]; then
	ip link set dev $IFACE up
fi
```
	sudo chmod 777 /etc/networkd-dispatcher/degraded.d/interfaceup.bash

+ Follow the same procedure in the location "/etc/networkd-dispatcher/off.d/interfacedown.bash"

```
#!/bin/bash

if [ $IFACE == "ens5" ]; then
	ip link set dev $IFACE down
fi
```
	sudo chmod 777 /etc/networkd-dispatcher/off.d/interfacedown.bash

## Install OpenStack controller (miniITX A)

## Install OpenStack Compute node (miniITX B)

## Install OpenStack Compute node (RPi)
