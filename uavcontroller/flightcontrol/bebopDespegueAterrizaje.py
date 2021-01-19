from pyparrot.Bebop import Bebop


bebop = Bebop(drone_type="Bebop2", ip_address="192.168.42.1")

print("connecting")
success = bebop.connect(15)
print(success)

if (success):

    bebop.smart_sleep(5)
    bebop.safe_takeoff(5)

    #Inclinaci  n m  xima permitida (5 es el m  nimo)
    bebop.set_max_tilt(5)
    #Velocidad vertical m  xima permitida (0.5 es el m  nimo)
    bebop.set_max_vertical_speed(1)
    #Altitud m  xima permitida (0.5 es el m  nimo)
    bebop.set_max_altitude(0.5)

    bebop.smart_sleep(10)
    bebop.safe_land(10)

    print("DONE - disconnecting")

    bebop.smart_sleep(5)
    bebop.disconnect()
