# # # # # # # 

# # # # # # user_input=input('Enter a sentence: ')
# # # # # # print(user_input)
# # # # # # step1=user_input[0]
# # # # # # print(step1)
# # # # # # step2=user_input[-1]
# # # # # # print(step2)
# # # # # # step3=len(user_input)-2
# # # # # # print(step3)
# # # # # # step4='*'*step3
# # # # # # print(''.join([step1,step4,step2]))



# # # # # user_input=input('Enter a sentence: ').replace('-','').replace(' ','')
# # # # # print('*'*30)
# # # # # step1=user_input[:4]
# # # # # step2=user_input[-4:]
# # # # # step3=len(user_input)-8
# # # # # step4='*'*step3
# # # # # print(''.join([step1,step4,step2]))
# # # # # print('*'*35)


# # # # userinput='aeiou'
# # # # step1=userinput.replace('a','✈️').replace('e','🐘').replace('i','🍧').replace('o','🍊').replace('u','☂️')
# # # # print(step1)

# # # userinput='HTTPS://www.PTYHON.org/abc'
# # # step1=userinput.lower()
# # # print(step1)
# # # step2=step1.split('/')
# # # print(step2)
# # # step3=step2[2]
# # # print(step3)
# # # step4=step3.replace('www.','')
# # # print(step4)



# # def login():
# #     '''this function will display'''
# #     print('hello world')
# #     login()
# #     print(login.__doc__)


# #     student_name = ['sita', 'rita', 'hari']
# # name = input('Enter the name: ')

# # if name in student_name:
# #     print(f'{name} is present')
# # else:
# #     print(f'{name} is absent')

# # # Second condition
# # if name not in student_name:
# #     print('true')
# # else:
# #     print('false')


# #to locte memory 
# name='ram'
# name2='shyam'
# print(id(name))
# print(id(name2))
# print(name is name2)



# name=[1,2,3,4]
# name2=[1,2,3,4]
# print(id(name))
# print(id(name2))
# print(name is name2)

# num1=12
# num2=15
# print(num1&num2)
# print(bin(num1) )


# list1=[1,2,3,4]
# list2=list1
# list1=list1+list2
# print(list1)
# print(list2)

# # # # # #num1=15
# # # # # #num2=17
# # # # # #if num1>num2:
# # # # # #    print('num1 is greater than num2')
# # # # # #else:
# # # # # #    print ('num2 is greater than num1')

# # # # # #num1=17
# # # # # #num2=15
# # # # # #if num1!=num2 and num1%2==0:
# # # # #   #  print ('True')
# # # # # #else:
# # # # #     print('False')

# # # # #     num1=17
# # # # # num2=15
# # # # # if num1!=num2 or num1%2==0:
# # # # #     print ('True')
# # # # # else:
# # # # #     print('False')

# # # # #Membership operator
# # # # student_name=['laxman,heera,sita']
# # # # name=input('enter the student name: ')
# # # # if name in student_name:
# # # #     print(f'{name} is present')
# # # # else:
# # # #     print(f'{name} not available')

# # # student_name=['laxman,heera,sita']
# # # name=input('enter the student name: ')
# # # if name in student_name:
# # #     print(f'{name} is present')
# # # else:
# # #     print(f'{name} not available')

# # #     # ----------------
    
# # #     if name not in student_name:
# # #         print('True')
# # #     else:
# # #         print('False')

# # #is is not
# # name='ram'
# # name2='shyam'
# # print(id(name))
# # print(id(name2))
# # print(name is name2)

# name=[1,2,3,4]
# name2=[1,2,3,4]
# print(id(name))
# print(id(name2))
# print(name is name2)

#bitwise opertaor
#& | * - << >>







# data=input('enter a name: ')
# print(data)
# step1=data.lower()
# print(step1)
# step2=step1.strip()
# step3=step2.replace(' ','_')
# print(step3)



# year=2025
# month=11
# day=24
# print(year,month,day,sep='/')


# for i in range(5):
#     print(i)

# for i in range(5):
#     print(i,end=' ')


# num1=12
# num2=15.09
# result=num1+num2
# print(type(result))



