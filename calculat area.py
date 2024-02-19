#Create a Class
class Room:
    length = 0.0
    breadth = 0.0

    #Method to Calculate Area
    def calculate_area(self):
        print("Area Of Room", self.length * self.breadth)
study_room = Room()
study_room.length = 42.5
study_room.breadth = 30.8
study_room.calculate_area()
