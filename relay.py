from gpiozero import OutputDevice

shelf_1_relay = OutputDevice(5, active_high=False, initial_value=False)
shelf_2_relay = OutputDevice(6, active_high=False, initial_value=False)
shelf_3_relay = OutputDevice(13, active_high=False, initial_value=False)


shelves = [shelf_1_relay, shelf_2_relay, shelf_3_relay]
