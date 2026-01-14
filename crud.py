users=['ram','hari']
while True:
     print('1. add')
     print('2. read')
     print('3. update')
     print('4. delete')
     print('5. exist')

     choice=int(input('enter the number:'))
     if choice==1:
          name=input("enter the name")
          users.append(name)
          print(f'user {name} is added')
     elif choice==2:
          i=0
          while i<len(users):
               print(f'{i}={users[i]}')
     elif choice==3:
        index_no=int(input("enter the name"))
        if index_no>=0 and index_no<len(users):
           name=input("enter the name")
           users[index_no]=name
           print('updates successfully')
        else:
            print('invalid index number')
     elif choice==4:
               name=input("enter the name")
               if name in users:
                    users.remove(name)
               else:
                    print(f'{name} doesnot exists')
     elif choice==5:
          break               
             