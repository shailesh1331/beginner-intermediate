# with open('file.txt') as file:
#     data=file.read()
#     print(data)
#
# try:
#     file=open('a_file.txt')
# except:
#     file=open('a_file.txt',mode='w')
#     file.write('hello')
# else:
#     data=file.read()
#     print(data)


fruits=['Apple','Pear','Orange']

def make_pie(index):
    fruit=fruits[index]
    print(fruit + "pie")

user=int(input("enter index"))
try:
    make_pie(user)
except IndexError:
    print("Fruit Pie")
