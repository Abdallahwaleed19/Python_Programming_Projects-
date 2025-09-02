class Weather_Station : 
    def __init__ (self):
        self.__observers = []
        self.__temperature = 0
    def register_observer(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)
            print(f"{observer.name} registered to Weather Station")
    def update_tempperature(self, temperature):
        self.__temperature = temperature
        print(f"Weather Station: Temperature updated to {self.__temperature}°C")
    
    
class PhoneApp :
    def __init__(self, name):
        self.name = name
    def update(self, temperature):
        print(f"{self.name} received temperature update: {temperature}°C")
        
if __name__ == "__main__":
    print("Egyption Weather Station")
    
    weather_station = Weather_Station()
    
    phone_app1 = PhoneApp("Phone App 1")
    phone_app2 = PhoneApp("Phone App 2")
    
    weather_station.register_observer(phone_app1)
    weather_station.register_observer(phone_app2)
    
    weather_station.update_tempperature(25)  
    weather_station.update_tempperature(30)  
    