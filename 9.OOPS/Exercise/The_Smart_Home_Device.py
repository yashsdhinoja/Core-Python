class SmartDevice: # deine class
    software_version = "v2.4" # attribute class

    # Constructor
    def __init__(self,device_name, room_location, security_token):
        self.device_name = device_name
        self.room_location = room_location
        self.__security_token = security_token

    #instance Method
    def instace_mtd(self, change_securely):
        self.__security_token = change_securely
        print(f"Device Name : {self.device_name} \n Room Location : {self.room_location} \n Security_token : {self.__security_token}")
        print(f"I allow you to change the security token securely New: {self.__security_token}")

    @staticmethod
    def deivce_status():
        print("occurs when your computer or security software no longer recognizes your printer's network signature, IP address, or security certificate")

SD1 = SmartDevice("Lenovo ideapad GAMING","smart object is inside when GPS cannot reach it",54392971)

print("="*30)
print(SmartDevice.software_version)
SD1.instace_mtd(212833)
SD1.deivce_status()
print("="*30)