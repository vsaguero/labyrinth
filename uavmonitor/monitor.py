import os
import time
import subprocess
import socket

uav_id = "UAV2"
id_devices = ["GCS", "UAV1"]
ip_wifi_list = ["10.0.0.1","10.0.0.2"]
ip_cellular_list = ["10.0.1.1","10.0.1.2"]
interface_list = ["enp3s0", "enp4s0"]
controller_ip = "127.0.0.1"
#Integer value is required for controller port
controller_port = 5005

#Check connectivity
def check_connectivity (ip_list):
    connectivity = ['0' for i in range(len(ip_list))] 
    for ip in ip_list:    
        if ip == 'none':
            connectivity[ip_list.index(ip)] = 'none'
        else:
            response = os.system('ping -c 1 -i 0.2 -w 1 '+ ip + ' > /dev/null')
            if response == 0:
                connectivity[ip_list.index(ip)] = '1'
            else:
                connectivity[ip_list.index(ip)] = '0'
    
    return connectivity

#Check RTT
def check_rtt (ip_list):
    rtt = ['0' for i in range(len(ip_list))] 
    for ip in ip_list:    
        if ip == 'none':
            rtt[ip_list.index(ip)] = 'none'
        else:
            response = os.system('ping -c 1 -i 0.2 -w 1 '+ ip + ' > /dev/null')
            if response == 0:
                value = subprocess.check_output("ping -c 1 " + ip +" | grep ttl | awk -F= '{print $4}'", shell=True).split(" ")
                rtt[ip_list.index(ip)] = value[0]
            else:
                rtt[ip_list.index(ip)] = 'null'
    return rtt

#Check Power
def check_power():
    a = "Coming soon"
    return a

#Check load RX
def check_load_RX (interface_list):
    load = ['0' for i in range(len(interface_list))] 
    for interface in interface_list:
        if interface == 'none':
            load[interface_list.index(interface)] = 'none'
        else:
            value = subprocess.check_output("ifconfig " + interface + " | grep 'Bytes RX'", shell=True).split(":")
            value = value[1].split(" ")
            load[interface_list.index(interface)] = value[1]

    return load

#Check load TX
def check_load_TX (interface_list):
    load = ['0' for i in range(len(interface_list))] 
    for interface in interface_list:
        if interface == 'none':
            load[interface_list.index(interface)] = 'none'
        else:
            value = subprocess.check_output("ifconfig " + interface + " | grep 'Bytes RX'", shell=True).split(":")
            value = value[2].split(" ")
            load[interface_list.index(interface)] = value[1]

    return load

def send_data_UDP (data, ip, port):
    byte_message = bytes(data)
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    opened_socket.sendto(byte_message, (ip, port))


while True:
    print ("-------------------")
    print ("Network parameters:")
    connectivity_wifi = check_connectivity(ip_wifi_list)
    print ("WiFi connectivity: ", connectivity_wifi)
    connectivity_cellular = check_connectivity(ip_cellular_list)
    print ("Cellular connectivity: ", connectivity_cellular)
    rtt_wifi = check_rtt(ip_wifi_list)
    print ("WiFi RTT: ", rtt_wifi)
    rtt_cellular = check_rtt(ip_cellular_list)
    print ("Cellular RTT:  ", rtt_cellular)
    print ("-------------------")
    print ("Host parameters:")
    power = check_power()
    print ("Power: ",power)
    interface_load_RX = check_load_RX(interface_list)
    print ("Interface Load RX: ",interface_load_RX)
    interface_load_TX = check_load_TX(interface_list)
    print ("Interface Load TX: ",interface_load_TX)
    print ("************************************************")

    data = str(uav_id) + "/" + str(id_devices) + "/" + str(connectivity_wifi) + "/" + str(connectivity_cellular) + "/" + str(rtt_wifi) + "/" + str(rtt_cellular)
    send_data_UDP(data,controller_ip,controller_port)
   
    #byte_message = bytes(data)
    #opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #opened_socket.sendto(byte_message, ("127.0.0.1", 5005))

    time.sleep(3)
