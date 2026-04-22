class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.is_lit = False  

    def toggle_lights(self):
        self.is_lit = not self.is_lit
        if self.is_lit:
            print(f"The lights in {self.room_name} are now ON.")
        else:
            print(f"The lights in {self.room_name} are now OFF.")

    def perform_maintenance(self):
        print(f"General maintenance performed in {self.room_name}.")


class Laboratory(Room):
    def __init__(self, room_name, equipment_count):
        super().__init__(room_name)   
        self.equipment_count = equipment_count


    def perform_maintenance(self):
        print(f"Safety check complete. All {self.equipment_count} pieces of equipment "
              f"in {self.room_name} have been calibrated.")


storage = Room("Storage Closet")

lab = Laboratory("Bio-Chem Lab", 15)

lab.toggle_lights() 

storage.perform_maintenance()
lab.perform_maintenance()



