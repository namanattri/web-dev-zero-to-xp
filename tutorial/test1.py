# for i in range(5):
#     print(f"Count: {i}")
#     for j in range(5):
#         print(j)
# print()  
# 

# print("===Squre Box===")
# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*', end=' ')
#             # print('*')
#     print()

# print("===left increasing triangle===")
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()

# print("===Right decreasing triangle===")

# n = 5
# for i in range(n):
#     for j in range(i ,n):
#         print('*', end=' ')
#     print()

print("===left increasing triangle===")
n = 5
for i in range(n):
    for j in range(i ,n):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()    

print("===left increasing triangle===")
n = 5
for i in range(n):    
    for j in range(i + 1):
        print(' ', end=' ')  
    for j in range(i ,n):
        print('*', end=' ') 
    print() 