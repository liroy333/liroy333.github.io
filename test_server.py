file_name = './check.txt'
message = 'test OK'

file = open(file_name,'w', encoding='utf-8')
file.write(message)
file.close()

file = open(file_name,'r', encoding='utf-8')
info = file.read()
file.close()

print(info)
input('press any key to continue:')