items=[1,2,3,4,5]
f=map(lambda x:x+1,items)
print(list(f))


items=[1,2,3,4,5]
f=filter(lambda x:x%2==0,items)
print(list(f))



name=['ram','rashmi','hari','gita']
f=list(filter(lambda x:x[0].startswith('r'),name))
print(f)
