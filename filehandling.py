'''
obj = open("file1.txt",'w')

obj.write("Welcome to TGC ")
print('All ok')
obj.close()
'''
'''
obj = open('file1.txt','r')

result=obj.read()
print(result)
obj.close()
'''
'''
obj = open('file1.txt','a')

obj.write("\nAddress: C 57, 2nd floor Metro Station, opposite Metro Pillar Number 81, near Preet Vihar, Preet Vihar, Delhi, 110092 \n Phone: 095827 86406")
print('All ok')
obj.close()
'''
'''
obj = open('file1.txt','r+')
result=obj.readline()
print(result)
obj.close()
'''
'''
obj = open('file1.txt','r+')
print(obj.readlines())
obj.close()
'''


