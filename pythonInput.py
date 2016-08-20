print("Read file project")
# đọc file python
fileName = input("Nhập tên file: ")

fileIput = open(fileName)

print("note file %r: ", fileName)

print(fileIput.read())

print("Read file c2: ",open(fileName).read())# đọc như này ta sẽ không đóng được file

fileIput.close()