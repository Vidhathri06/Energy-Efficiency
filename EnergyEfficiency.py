import random
class SmartHomeAgent:
    def __init__(self):
        self.devices = {
            "lights":False,
            "thermostat":22,  
            "appliances":False
        }
        self.occupancy=False  
        self.outside_temp=25 
    def environment(self):
        self.occupancy=input("Is the house occupied? (yes/no): ").strip().lower()=="yes"
        self.outside_temp=int(input("Enter the outside temperature (°C): "))
    def action(self):
        self.devices["lights"]=self.occupancy
        if self.occupancy:
            if self.outside_temp<18:
                self.devices["thermostat"]=24  
            elif self.outside_temp>28:
                self.devices["thermostat"]=20  
            else:
                self.devices["thermostat"]=22 
        else:
            self.devices["thermostat"]=18 
        self.devices["appliances"]=self.occupancy    
    def actions(self):
        print("\nSmart Home Status:")
        for device,state in self.devices.items():
            print(f"{device.capitalize()}:{state}")
        print(f"Occupancy:{self.occupancy},Outside Temp:{self.outside_temp}°C")   
    def run(self):
        self.environment()
        self.action()
        self.actions()
if __name__=="__main__":
    agent=SmartHomeAgent()
    while True:
        agent.run()
        if input("Run again? (yes/no): ").strip().lower()!="yes":
            break
