import socket
import json

#UAV 1
UDP_IP_uav_1 = "127.0.0.1"
UDP_PORT_uav_2 = 5006

sock_uav_1 = socket.socket


#UAV 2
UDP_IP_uav_2 = "127.0.0.1"
UDP_PORT_uav_2 = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP_uav_2, UDP_PORT_uav_2))

while True:
    uav_2, addr = sock.recvfrom(1024)
    print ("received message: %s" % uav_2)
    data = uav_2.split("/")
    uav_id = data[0]
    id_devices = data[1]
    connectivity_wifi = data[2]
    connectivity_cellular = data[3]
    rtt_wifi = data[4]
    rtt_cellular = data[5]

    print ("-------------------")
    print ("Network parameters: ")
    print ("UAV ID: ", uav_id)
    print ("WiFi connectivity: ", connectivity_wifi)
    print ("Cellular connectivity: ", connectivity_cellular)
    print ("WiFi RTT: ", rtt_wifi)
    print ("Cellular RTT:" , rtt_cellular)
    
    #data1 = json.dumps(uav_2)
    #data2 = '{"id":["123456789","2"],"name":"John Doe","first_name":"John","last_name":"Doe"}'
    #print(uav_2)
    #print(data)
    #data = json.loads(data2)
    #print (data['id'])
    #print ('*********')
    #print (data[2])
    #print (connectivity_wifi)
    #print (data2) 
