import math

def house_sqr_ft():
    total_sqr_ft = 0
    num_rooms = int(input("How many rooms are in the house? "))
    counter = 0
    while counter < num_rooms:
        counter+=1
        print(f"For room #{counter}: ")
        room_len = int(input("What is the room length? "))
        room_width = int(input("What is the room width? "))
        room_area = room_len * room_width
        total_sqr_ft+=room_area
        print(f"Adding room area {room_area} to total square feet")
    print("The total square foot is :")
    print(total_sqr_ft)

def circum_of_circle(radius):
    circumference = 2*math.pi*radius
    return circumference