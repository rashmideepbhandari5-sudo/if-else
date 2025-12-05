# list
# item=[]

# # append ko cose ma index same hunxa
# item.append(4)
# item.append((5,4))  
# print((item))

# extend ko case ma index diff hunxa
# item.extend((3,4,9,8))
# print(item)

# item[3]='rashmi'
# item.insert(0,'ram')
# item.insert(2,'ram')

# print(item)



# item=[1,2,3,[5,7]]
# item[3][1]='hari'
# print(item)

# item.remove(1)
# print(item)

# item.pop(1)
# print(item)


# item.pop(item.index(3))
# print(item)
# item.pop()
# print(item)

# item.clear()
# print(item)

# item=[1,2,3,4,5]
# num1=item.copy()
# print(num1)

# item=[1,2,3,4,5]
# num1=item
# item+=num1
# print((item))
# print (num1)
# item=num1+item
# print(item)



# tuple
# item=1,2,3,4,5
# item=[1,2,3,4,5]
# item.insert(0,'ram')
# print(item)
# print(tuple(item))


# item = (1,2,3,3,3,3,4,4,4,4,4,4,4,4)
# result=item.count(3)
# print(result)

# # set
# # items={1,2,3,4,5}
# # result.add(6)
# # print(result)

# item={1,2,3,3,3,4,4,4,5,5}
# print(item)    

# item={1,2,3,4,5}
# item.remove(3)
# print(item)

# item={1,2,3,4,5}
# item.pop()
# print(item)

# item.clear()
# print(item)


item={'shyam','ram','hari'}
item2={1,2,'hari    '}
result=item.union(item2)
print(result)
result=item.intersection(item2) 
print(result)
result=item.difference(item2)   
print(result)
result=item.symmetric_difference(item2) 
print(result)
result=item.isdisjoint(item2)   
print(result)
result=item.issubset(item2)                 
print(result)