from gpiozero import OutputDevice

relay = OutputDevice(14, active_high=False, initial_value=False)

def open_shelf():
    print("on")
    relay.on()
    return True

def close_shelf():
    print("off")
    relay.off()
    return True
