
# def print_even():
#     for i in range(1,11):
#         if i %2 == 0:
#             print(i)

# print_even()


# def sum_numbers():
#     total = 0
#     for i in range(1,11):
#         total += i
#     print(total)
# sum_numbers()



# def sum_numbers(n):
#     total = 0
#     for i in range(1,n+1):
#         total += i
#     print(total)

# sum_numbers(5)


# def sum_even(n):
#     total = 0
#     for i in range(1,n+1):
#         if i %2 == 0:
#             total +=i
#     print(total)

# sum_even(6)


# def sum_even(n):
#         total = 0
#         for i in range(1,n+1):
#              if i %2 == 0:
#                 total +=i
#         return(total)


# print(sum_even(6))


# def find_largest(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return(largest)

# numbers = [12, 45, 7, 23, 89, 34]

# print(find_largest(numbers))


# def get_even_numbers(numbers):
#     result = []
#     for number in numbers:
#         if number%2 == 0:
#             result.append(number) 
#     return(result)

# numbers = [3, 8, 11, 14, 20, 7, 6]

# print(get_even_numbers(numbers))


# def count_greater(numbers,x):
#     count = 0
#     for number in numbers:
#         if number > x:
#             count+= 1
#     return count

# numbers = [4, 12, 7, 20, 3, 15]

# print(count_greater(numbers,10))


# def find_even_sum(numbers):
#     sum = 0
#     for number in numbers:
#         if number%2 == 0:
#             sum +=number
#     return(sum)

# numbers = [3, 8, 11, 14, 20, 7, 6]

# print(find_even_sum(numbers))


# def square(a):
#     return a*a

# def calculate(number):
#     return square(number)

# print(calculate(5))


# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number%2 == 0:
#             count +=1
#     return count

# numbers = [4, 7, 2, 9, 6, 3, 8]
# print(count_even(numbers))



# def find_smallest(numbers):
#     smallest = numbers[0]
#     for number in numbers:
#         if number < smallest:
#             smallest = number
#     return smallest
# numbers = [12, 5, 27, 3, 19, 8]

# print(find_smallest(numbers))


# def count_odd(numbers):
#     count = 0
#     for number in numbers:
#         if number%2 != 0:
#             count+=1
#     return count

# numbers =[3,1,3,56,7,4,9,8,7]

# print(count_odd(numbers))



# def sum_greater(numbers, target):
#     total = 0
#     for number in numbers:
#         if number > target:
#             total += number
#     return total

# numbers = [4, 12, 7, 20, 3, 15]
# print(sum_greater(numbers,10))


# def find_largest_even(numbers):
#     largest = 
#     for number in numbers:
#         if number%2 ==0: 
#             if number> largest:
#                 largest = number
#     return largest
# numbers = [301, 12, 7, 20, 9, 14, 5]
# print(find_largest_even(numbers))



# def find_largest_even(numbers):
#     largest = None

#     for number in numbers:
#         if number % 2 == 0:
#             if largest is None or number > largest:
#                 largest = number

#     return largest


# numbers = [301, 12, 7, 20, 9, 14, 5]

# print(find_largest_even(numbers))


# largest = None

# numbers = [301, 12, 7, 20]

# for number in numbers:
#     if number % 2 == 0:
#         largest = number
# print(largest)


# def find_largest_even(numbers):

#     largest = None

#     for number in numbers:

#         if number % 2 == 0:

#             if largest is None or number> largest:
#                 largest = number

#     return largest

# numbers = [301, 12, 7, 20, 9, 14, 5]

# print(find_largest_even(numbers))

