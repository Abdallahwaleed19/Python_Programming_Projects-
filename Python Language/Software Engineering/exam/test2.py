class SmartHomecontroller :
    def control_device(self , device_type , action):
        if device_type == "light" and action == "on" :
            return "Light is turned on"
        elif device_type == "light" and action == "off":
            return "Light is turned off"
        elif device_type == "thermostat" and action == "set":
            return "Thermostat is desired temperature"
        else:
            return "Invalid action"

class OldfanController:
    def turn_on_fan(self):
        return "Fan is turned on"
    def turn_off_fan(self):
        return "Fan is turned off"

class Adapter:
    def __init__(self, oldfancontroller):
        self.oldfancontroller = oldfancontroller

    def control_device(self, device_type, action):
        if device_type == "fan" and action == "on":
            return self.oldfancontroller.turn_on_fan()
        elif device_type == "fan" and action == "off":
            return self.oldfancontroller.turn_off_fan()
        else:
            return "Invalid action"

if __name__ == "__main__":
    oldfancontroller = OldfanController()
    adapter = Adapter(oldfancontroller)
    print(adapter.control_device("fan", "on"))
    print(adapter.control_device("fan", "off"))
