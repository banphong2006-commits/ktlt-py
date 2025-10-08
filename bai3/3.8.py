import math

pos = [0, 0]
while True:
    s = input("Nhập lệnh (ví dụ: UP 5, hoặc Enter để dừng): ")
    if not s:          break
    movement = s.split(" ")
    direction = movement[0].upper()   
    steps = int(movement[1])          

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps


distance = int(round(math.sqrt(pos[0]**2 + pos[1]**2)))
print("Khoảng cách là:", distance)
