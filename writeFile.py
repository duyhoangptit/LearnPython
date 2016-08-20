# truncate: xoa het noi dung của file
# write : ghi noi dung gi do vao file

fileName = input("Nhập tên file: ")

file = open(fileName,'a+')
# w mở file để ghi thay thế, r là mở file để đọc, a thì sẽ cho phép ghi đè
# nếu dừng w+,r+, a+ có nghĩa cho phép dùng vừa đọc vừa ghi

print("Xóa nội dung của file: ", fileName)
# Xóa trắng file
# file.truncate()

print("Ghi noi dung của file\n")

line1 = input("Line 1:" )
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file")

file.write(line1 + "\n")
file.write(line2 + "\n")
file.write(line3 + "\n")

print("Ghi thành công")
file.close()