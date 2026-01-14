# to stop the output come from another module
# ######if __name__ == "__main__":#########

# def area_of_rec(l, b):
#     a=l*b
#     print("Area of Rectangle is:",a)

# area_of_rec(5, 10)
# area_of_rec(7, 3)



# def area_of_rec(*a):
#     print("Area of Rectangle is:",a)

# area_of_rec(5, 10,5,6,7,8)

# # output come in tuple form
# def area_of_rec(*a):
#     total=0
#     for i in a:
#         total=total+i
#     print("Area of Rectangle is:",total)
# area_of_rec(5, 10,5,6,7,8)

#     # output come in dictionary form
# def area_of_rec(**a):
#     total=0
#     for i in a:
#         total=total+i
#     print("Area of Rectangle is:",total)
# area_of_rec(a=5, b=10, c=5)# to stop the output come from another module
# # ######if __name__ == "__main





def area_of_rec(**a):
    total=0
    for i in a.values():
        total=total+i
    print("Area of Rectangle is:",total)
area_of_rec(a=5, b=10, c=5)




# ######## scope,namespace ,global and local namespace,buitin,lamdmap filture and reduced a function,