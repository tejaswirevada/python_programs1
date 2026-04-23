class  car:
    def __init__(self,carname,model,cost,colour):
        self.carname=carname
        self.model=model
        self.cost=cost
        self.colour=colour
    def display(self):
        print("Car name is:",self.carname)
        print("Car model is:",self.model)
        print("Car cost in lakhs is:",self.cost)
        print("Car colour is:",self.colour)
c=car("Mahindra Thar","LXT 4WD Diesel AT",17.62,"Shealth Black")
c.display()
