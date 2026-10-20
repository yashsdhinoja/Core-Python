class Mercedes:
    item = "Luxuary Automotive"

    def __init__(self,model):
        self.model = model

    def drive(self):
        txt = f"{self.model} ({self.item}) glides silently with supreme luxury."
        print(txt)

class FordMustarg:
    item = "American Muscle"

    def __init__(self,model):
        self.model = model

    def drive(self):
        xtx = f"The {self.model} ({self.category}) roars down the track with V8 power!"
        print(xtx)

caer1 = Mercedes("S-Class")
caer2 = FordMustarg("GT450")

shree_ram_garage = [caer1,caer2]

for d in shree_ram_garage:
    print(d.drive())