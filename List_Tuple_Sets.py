courses= ['math','physics','chemestry']
print((courses))
print(len(courses))
print(courses[1])

print((courses[2]))
print((courses[-1]))
print(courses[1:-1])

courses.append('marathi')
print(courses)
courses.insert(0,'Art')
print(courses)

courses1=['English', 'History']
#courses.insert(0,courses1)

#courses.append(courses1)

courses.extend(courses1)

print(courses)

courses.remove('English')
print(courses)
print(courses.pop())
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

a=[5,7,3,54,98,74,56,85,258,45,789]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(sorted(a))
print(sorted(courses))
print(sum(a))




for item in courses:
    print(item)

for index,courses in enumerate(courses,start=1):
    print(index,courses)

str=' , '.join(courses1)
print(str)

newlist=str.split(' - ')
print(newlist)



#Tuples

print(courses1)
b=courses1
print(b)

courses1[0]='Art'
print(courses1)
print(b)


tuple1=('History','Math','English','Physics')
tuple2=tuple1

print(tuple1)
print(tuple2)

#tuple1[0]='Art'

print(tuple1)
print(tuple2)



#sets

sets1={'History','Math','English','Physics'}
sets2={'History','Math','Art','Geography'}
print(sets1)

print(sets1.intersection(sets2))

print(sets1.difference(sets2))

print(sets1.union(sets2))