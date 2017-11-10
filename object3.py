from vehicle import Vehicle
cars=[]
def show_list():
    for car in cars:
        print car
def edit_cars():
    show_list()
    index=int(raw_input("enter car number:..."))
    km=int(raw_input("enter km:..."))
    cars[index].km=km
def add_new_car():
    brand=raw_input("car brand:...")
    model=raw_input("car model:...")
    km=raw_input("current km:...")
    service=raw_input("service date: dd/mm/yyyy...")
    new_car=Vehicle(brand,model,km,service)
    cars.append(new_car)

print "Welcome to Carpark Catalogue"
while True:
    print "1 Show list"
    print "2 Edit existing cars"
    print "3 Add new vehicle"
    print "4 Exit"
    task=int(raw_input("What would you like to do? (1/2/3/4):"))
    if task==1:
      show_list()
    elif task==2:
      edit_cars()
    elif task==3:
      add_new_car()
    elif task==4:
      print "bye"
      break
    else:
      print "I don not know what you want"

