# items=[1,2,3,4]
# i=0
# while i<len(items):
#     print(items[i])
#     i+=1    

#     # using rangr
# items=[1,2,3,4]
# i=0
# while i in range(len(items)):
#     print(items[i])
#     i+=1    

#     # using true
# # items=[1,2,3,4]
# # i=0
# # while True:
# #     if i==4:
# #         break
# #     print(items[i])
# #     i+=1    
# # for even num
# items=[1,2,3,4]
# i=0
# while True:
#     if i==4:
#         break
#     if items[i]%2==0:
#         print(items(i))
#         i+=1


print('.............................while loop que..............................')


# 1(wrong)

# program=int(input('enter the  inter:'))
# total=0
# while True:
#   if program>=0:
#      total=total+program
#      program=int(input('enter the  inter:'))

#   print(total)


# 2

# User_input=int(input('enter the  inter:'))
# while User_input>1:
#     print(User_input)
#     User_input=User_input-1
# else:
#     print('limit threshold reached')

# 3
# item=[1,2,3,4,5]
# i=0
# while i<len(item):
#     if item[i]%2==0:
#         i=i+1
#         continue
#     print(item[i])
#     i=i+1

# # 3
# import random
# while True:
#     rn=random.randint(1,100)
#     user_input=int(input('enter a num:'))
#     if rn==user_input:
#         print('congrat')
#         break
#     elif user_input>rn:
#         print('too high')
#     else:
#         print('too low')


# # 4
# while True:
#     password=input('enter password')
#     if len(password)>8:
#         print('thank u')
#     else:
#         print('password must be greater then 8')

# 5
# user_input=int(input('enter the number:'))
# for i in range(1,11):
#     print(user_input,'*',i,'=',user_input*i)


# user_input=int(input('enter the number:'))
# i=1
# while True:
#     if i==11:
#         break
#     print(f'{user_input}x{i}={user_input*i}')
# i=i+1

# p1=input('enter s or p or r:')
# p2=input('enter s or p or r:')
# if p1==p2:
#     print('equal')
# elif p1=='r':
#     if p2=='s':
#       print('player1 won the game')
#     else:
#         print('player2 won the game')
# elif p1=='s':
#     if p2=='p':
#       print('player1 won the game')
#     else:
#         print('player2 won the game')
# elif p1=='p':
#     if p2=='s':
#       print('player1 won the game')
#     else:
#         print('player2 won the game')


print('.....................................................................................')
# items=[1,2,3,4]
# for i in range(len(items)):
#     if items[i]%2!=0:
#       print(items[i])
    

# items=[1,2,3,4]
# i =0
# while i in range(len(items)):
#     if items[i]%2!=0:
#       print(items[i])
#     i+=1

# items=[1,2,3,4]
# i =0
# while True:
#     if i==4:
#        break
#     if items[i]%2!=0:
#       print(items[i])
#     i+=1


print('.....................................................................................')

# items=[1,'a','b',2,3,4]
# str1=[]
# id=[]
# for i in range(len(items)):
#     if isinstance(items[i],int):
#         id.append(items[i])
#     elif isinstance(items[i],str):
#         str1.append(items[i])
# print(id)
# print(str1)



# items=[1,'a','b',2,3,4]
# i=0
# str1=[]
# id=[]
# while i in range(len(items)):
#     if isinstance(items[i],int):
#         id.append(items[i])
#     elif isinstance(items[i],str):
#         str1.append(items[i])
#         i=i+1
# print(id)
# print(str1)


# items=[3,4]
# for i in range(len(items)):
#     for j in range(1,11):
#         print(f'{items[i]}x{j}={items[i]*j}')

# items=[3,4]
# i=0
# while i in range(len(items)):
 
#       j=1
#       while j in range(1,11):
#              print(f'{items[i]}x{j}={items[i]*j}')
#              j=j+1
#       i=i+1     

# que
# sum=0
# i=2
# while i<5:
#     i=i+1
#     sum=sum-2
#     print(i)
# print(sum)    


