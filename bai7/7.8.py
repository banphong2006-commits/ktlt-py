
students = ["James", "Nail", "Paul", "Pit"]


with open("students.txt", "w", encoding="utf-8") as f:
    for name in students:
        f.write(name + "\n")

print("Đã ghi danh sách sinh viên vào tệp 'students.txt' thành công!")


print("\nNội dung trong tệp:")
with open("students.txt", "r", encoding="utf-8") as f:
    print(f.read())
