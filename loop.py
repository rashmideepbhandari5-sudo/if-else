# # item=[1,2,3,4]
# # for i in range(len(item)):
# #     print(item[i])


# # item=[1,2,3,4]
# # for i in range(len(item)):
# #     print(i,'',item[i])



# # item=[1,2,3,4]
# # count=0
# # for i in item:
# #     count+=1
# #     print(count,'',i)


# # item=[1,2,3,4]
# # for i in enumerate(item):
# #   print(i)



# #   item=[1,2,3,4]
# # for i,j in enumerate(item,start=1):
# #   print(i,'',j)


# # strs='program'
# # vowel=[]
# # cons=[]
# # for i in strs:
# #    if i in 'aeiou':
# #     vowel.append(i)
# # else:
# #     cons.append(i)

# # print(vowel)
# # print(cons)    

# # num=int(input('enter the number:'))

# # if num%2==0:
# #     print('even')
# # else:
# #     print('odd')



# # item=[1,2,3,4,5]
# # odd=[]
# # even=[]
# # for i in item:
# #    if i%2==0:
# #     print('even')
# # else:
# #     print('odd')


# # item=[1,2,3,4,5]
# # total_sum=0
# # for i in item:
# #      if i%2==0:
# #        total_sum=total_sum+i
# # print(total_sum)
    

# # items=[1,'a','b',-2,-3,4,20,-22,5]

# # for i in items:
# #     if isinstance(i,int):
# #         if i%2==0:
# #             if i>0:
# #                 print(i)


# # items=[1,'a','b',-2,-3,4,20,-22,5]
# # odd=[]
# # even=[]
# # strs=[]
# # for i in items:
# #     if type(i)==int:
# #        if i%2==0:
# #            even.append(i)
# #        else:
# #            odd.append(i)
# #     else:
# #      strs.append(i)

# # print(odd)
# # print(even)
# # print(strs)



# # que no 1
# num={1,2,3,4,5}
# for i in num:
#     if i%2==0:
#      print(f'number {i} is even')
#     else:
#        print (f'number {i} is odd')

# # by using len(item)
# num=[1,2,3,4,5]
# for  i in range(len(num)):
#     if num[i]%2==0:
#      print(f'number {num[i]} is even')
#     else:
#        print (f'number {num[i]}is odd')


# # que no 2
# list=[10,20,30 ,40]
# sum=0
# for i in range(len(list)):
#    sum+=list[i]
#    print(f'added {list[i]}.running total is {list[i]}')
# print(f'total sum is {sum}')
   
# #    que 3

# student_name= ['ram','sita','hari']
# for i in student_name:
#    print(f'hi {i},your cource approval ready.')

              
# student_name= ['ram','sita','hari']
# for i in range(len(student_name)):
#    print(f'hi {student_name[i]},your cource approval ready.')
              
# print('..........................................................')

# # que 4
# # pagecount=[ 45,30 ,50,40]
# # chapter=1
# # for i in range(len(pagecount)):
# #    print(f'chapter {chapter[i]} has {pagecount[i]} ')
# #    chapter+=pagecount[i]

# page=[45,48,83,64]
# for i,j in enumerate(page,start=1):
#     print(f'chapter {i} has {j} ')

#     print('..........................................................')

# # que 5

# list=[4,5,3,2]
# count=1
# for i in range(len(list)):

#     count*=list[i]
#     print(f'the product of multiplation is {count}')
 
# print('..........................................................')

# # que 6
# num=11
# for i in range(1,11):
#    print(f'num*{i}={num*i}')

#    print('..........................................................')
   

# #    que 7
# student_name= [{"name":"ram","math_grade":43},{"name":"hari","math_grade":65},{"name":"sita","math_grade":90}]
# for i in student_name:
#   if i['math_grade']>=70:
#      i['status']='approved'
#   else:
#      i['status']='rejected'
# print(student_name)

# print('..........................................................')
   
# # or
# student_name= [{"name":"ram","math_grade":43},{"name":"hari","math_grade":65},{"name":"sita","math_grade":90}]
# for i in range(len(student_name)):
#   if student_name[i]['math_grade']>=70:
#      student_name[i]['status']='approved'
#   else:
#      student_name[i]['status']='rejected'
# print(student_name)

# print('..........................................................')
   
# # que
# student_record= {'id1':{"name":"ram","math_grade":43},'id2':{"name":"sita","math_grade":90}}
# for i,j in student_record.items():
#    if j['math_grade']>=70:
#       j['status']='approved'
#    else:
#       j['status']='rejected'
#       print(student_record)
     
# # user sanga user name rw password liya .yadi user la pass or usename milyo vanna congract .user la 1 time attem garda mistake aayo vana 2 attem left. anin 3 time garda last timae. aani block garne

# print('..........................................................')
   


# items=[[1,2],[3,4,5],[6,7,8]]
# for i in items:
#    for j in i:
#       print(j,end=' ')
#    print()


   
# items=[[1,2],[3,4,5],[6,7,8]]
# for i in items:
#    for j in i:
#       if j==3:
#        print(j)
#    print()


# items=[[1,2],[3,4,5],[6,7,8]]
# for i in items:
#    for j in i:
#       if j==3:
#          break
#       print(j)
#    print()

# items=[[1,2],[3,4,5],[6,7,8]]
# for i in items:
#    for j in i:
#       if j==3:
#          continue
#       print(j)
#    print()


# items=[[1,2],[3,4,5],[6,7,8]]
# for i in items:
#    for j in i:
#       if j==3:
#        print(j)
#       break
#    print()

# print('..........................................................')
   

# # quue
# items=[4,5,6,7]
# for i in items:
#    for j in range(1,11):
#     print(f'{i}*{j}={i*j}')


# print('..........................................................')
   

# student_name={'ram':{'m':41,'s':43},'shyam':{'m':42,'s':43}}
# for i,j in student_name.items():
#    print(i,'',j)
#    totalmark=j['m']+j['s']
#    averagemark=totalmark/2
#    print(f'totalmark={totalmark}')
#    print(f'averagemark={averagemark}')
  
   
# student_name={'ram':{'m':41,'s':43},'shyam':{'m':42,'s':43}}
# for i in student_name:
#    for j in student_name.values():
#       totalmark=j['m']+j['s']
#       averagemark=totalmark/2
#       print(f'totalmark={totalmark}')
#       print(f'averagemark={averagemark}')
#       print('..........................................................')
   

# student_name={'ram':{'m':41,'s':43},'shyam':{'m':42,'s':43}}
# for i,j in student_name.items():
#    print(i)
#    totalmark=0
#    count=0
#    for k,l in j.items():
#       totalmark=totalmark+l
#       count=count+1
#    averagemark=totalmark/count
#    print(totalmark)
#    print(averagemark)


# dictionary={}
# unique_word=set()
# user_input=int(input('how many words do you want to add:'))
# for i in range(1,user_input+1):
#    choice=int(input('press 1.add 2.display 3.remove 4.exit'))
#    if choice==1:
#       word=input('enter the word:')
#       if word==unique_word:
#          print(f'code already exist')
#       else:
#          meanning=input('enter the meaning of the word:')
#          dictionary[word]=meanning
#          unique_word.add(word)
#    elif choice==2:
#         for i,j in dictionary.items():
#            print(i,' ',j) 
#    elif choice==3:
#       word=input('enter the word want to remove:')
#       if word not in unique_word:
#          print(f'{word} doesnot exists')
#       else:
#          dictionary.pop(word)
#          unique_word.remove(word)
#    else:
#       break
# print(unique_word)          


# distionary={}
# character={}
# word=input('enter the word:')
# for i in word:
#   character[i]=character.get(i,0)+1  
#   character[word]=character
#   print(distionary)

# distionary={}

# word=input('enter the word:')
# for i in word.split(','):
#     character={}
#     for j in i:
#           character[j]=character.get(j,0)+1  
#     distionary[i]=character
# print(distionary)


distionary={}

word=input('enter the word:')
for i in word.split(','):
    character={}
    for j in i:
          if j in 'aeiou':
             character[j]=character.get(j,0)+1  
    distionary[i]=character
print(distionary)


  

  