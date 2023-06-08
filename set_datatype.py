#SET DATATYPE

course={'java','c','c++','java','python','c'}
print(course)
print(type(course))
course.add('javascript')
print(course)
course.add('Javascript')
print(course)
course.add('java')
print(course)
print('c+' in course)


'''course.remove('java')
print(course)
course.clear()
print(course)

del course
print(course)'''

# Empty SET
data1 = {}
print(type(data1))
data1 = set()
print(type(data1))

#frozenset

data = frozenset([10,20,10,30,20,40,30,50,10])

print(data)
print(type(data))
#print(data.add(60))
#print(data.remove(10))
