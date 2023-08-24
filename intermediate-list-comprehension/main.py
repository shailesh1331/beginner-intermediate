# new_list=[x*2 for x in range(1,5)]
# print(new_list)


# numbers=[1,1,2,3,5,8,13,23,34,45]
# squared_numbers=[num*num for num in numbers]
#
# print(squared_numbers)

numbers=[1,1,2,3,5,8,13,23,34,45]
result=[num for num in numbers if num%2==0]
print(result)