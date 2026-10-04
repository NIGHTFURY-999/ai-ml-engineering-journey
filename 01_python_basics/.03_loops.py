# for i in range (5):
#     print(i)

# for i in range(1,11):
#     print(i)


# for i in range(2,21,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)



# total = 0

# for i in range(1,6):
#     total = total +i
# print(total)




# count = 0

# for i in range (1,11):
#     if i%2 == 0:
#         count = count + 1
#     else:
#         continue
# print (count)
 


# word = "python"
# count = 0
# for letter in word:
#     count +=1
# print(count)


# count = 1

# while count <= 5:
#     print(count)
#     count +=1

# count = 10

# while count >= 1:
#     print(count)
#     count += -1



# while count <= 10:
#     if count % 2 == 0:
#         count += 1
#         continue
#     print(count)
#     count += 1


# count = 1

# while True:
#     if count ==6 :
#         break
        
#     print(count)
#     count += 1
    

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(5):
#     for j in range(5-i):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# numbers = [4, 8, 2, 15, 6]
# big = 0
# for number in numbers:
#     if number >= big:
#         big = number
# print(big)

# numbers = [4, 8, 2, 15, 6]
# small = 10
# for number in numbers:
#     if number <= small:
#         small = number
# print(small)

# numbers = [4, 7, 2, 9, 6, 3, 8]
# add = 0
# for number in numbers:
#     if number % 2 == 0:
#         add += number
# print(add)

# numbers = [4, 7, 2, 9, 6, 3, 8]

# for number in range(int(numbers)):
    
#     print(number)


# numbers = [4, 7, 2, 9, 6, 3, 8]
# num = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         num.append(numbers[i])
        
# print(num)


# numbers = [5, 12, 7, 8, 3, 10, 15]

# num = []

# for i in range(len(numbers)):
#     if numbers[i] > 8:
#         num.append(numbers[i])

# print(num)


# numbers = [5, 12, 7, 8, 3, 10, 15]

# num = []

# for number in numbers:
#     if number > 8:
#         num.append(number)

# print(num)


# numbers = [5, 12, 7, 8, 3, 10, 15]

# for i in range(len(numbers)):
#     if numbers[i] > 8:
#         print(i)


# numbers = [14, 3, 8, 21, 6, 11, 4]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         print(i,numbers[i])


# numbers = [14, 3, 8, 21, 6, 11, 4]

# even_numbers = []

# for i in range(len(numbers)):
#     if numbers[i] %2 ==0:
#         even_numbers.append(numbers[i])

# print(even_numbers)


# numbers = [14, 3, 8, 21, 6, 11, 4]

# even_indexes = []

# for i in range(len(numbers)):
#     if numbers[i]% 2 ==0:
#         even_indexes.append(i)

# print(even_indexes)


# numbers = [4, 7, 2, 9, 6, 3, 8]

# target = 6

# for number in range(len(numbers)):
#     if numbers[number] == target:
#         print(target,"found at",number,"index")

# numbers = [4, 7, 2, 9, 6, 3, 8]

# target = 10
# found =False
# for i in range(len(numbers)):
#     if len(numbers):
#         found = False
#         print("not found")
#         continue
#     elif found == True:
#         continue
#     elif numbers[i] == target:
#         found = True
#         print("found")
    

# numbers = [4, 7, 2, 9, 6, 3, 8,]

# target = 10

# found = False

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         found = True

# if found == False:
#     print("not found")
# if found == True:
#     print("found")



# numbers = [4, 7, 2, 9, 6, 3, 8]

# target = 10

# found = False

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         found = True

# if found:
#     print("found")
# else:
#     print("not found")


# numbers = [4, 7, 2, 9, 6, 3, 8]
# target = 6

# for i in range(len(numbers)):
#     if numbers[i] == 6:
#         print(target,"found at index", i)


# numbers = [4, 7, 2, 9, 6, 3, 8]

# target = 6

# found = False
# index = 0
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         found = True
#         index = i

# if found :
#     print(target, "found at index" ,index)

# else:
#     print("not found")

# numbers = [2, 5, 2, 7, 2, 9, 5]

# target = 2

# count =0

# for number in numbers:
#     if number == target:
#         count+=1

# print(count)

# numbers = [3, 8, 5, 12, 7, 6, 9, 10]

# count = 0

# for number in numbers:
#     if number%2 == 0:
#         count+=1

# print(count)

# numbers = [3, 8, 5, 12, 7, 6, 9, 10]

# total = 0

# for number in numbers:
#     if number%2 == 0:
#         total += number

# print(total)


# numbers = [4, 7, 2, 9, 6, 3, 8, 10]

# count = 0
# total = 0

# for number in numbers:
#     if number%2 == 0:
#         count+=1
#         total += number

# print("even numbers :",count)
# print("sum:",total)


# numbers = [4, 17, 2, 9, 25, 6, 8]
# big = 0
# for number in numbers:
#     if number > big:
#         big = number
# print(big)

# numbers = [-4, -17, -2, -9, -25]

# largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         largest = number

# print(largest)

# numbers = [-4, -17, -2, -9, -25]

# smallest = numbers[0]

# for number in numbers:
#     if number < smallest:
#         smallest = number

# print(smallest)

# numbers = [10, 20, 30, 40, 50]
# # for i in range(len(numbers)-1,-1,-1):
# #     print(numbers[i])

# # numbers = [7, 14, 21, 28, 35, 42]

# # for i in range(len(numbers)-1,-1,-1):
# #     print(numbers[i])

# numbers = [7, 14, 21, 28, 35, 42, 49, 56]

# for i in range(len(numbers)-1,-1,-1):
#     if numbers[i] % 2== 0 :
#         print(numbers[i])

# # word = "programming"

# # count = 0

# for letter in word:
#     if letter == "n":
#         count+=1
# print(count)


# word = "programming"

# count = 0

# for letter in word:
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         count+=1

# print(count)

# word = "programming"

# result = ""

# for letter in word:
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         result += letter
# print(result)

# word = "python12345"

# result = ""

# for letter in word:
#     if letter in "qwertyuiopasdfghjklzxcvbnm":
#         result+= letter
# print(result)

# word = "programming"

# count = 0

# for letter in word:
#     if letter in "aeiou":
#         count+= 1
# count =  len(word) - count

# print(count)

# word = "programming"

# count = 0

# for letter in word:
#     if letter not in "aeiuo":
#         count+=1
# print(count)


# numbers = [4, 7, 2, 9, 6, 3, 8]

# target = 9

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print(target,"found at index :", i)
#         break

# numbers = [4, 7, 9, 2, 9, 6, 9]
# target = 9

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print(i)
#         break


# numbers = [4, 7, 2, 9, 6, 3, 8]

# for i in range(len(numbers)):
#     if numbers[i]% 2 == 0 :
#         continue
#     print(numbers[i])


# numbers = [1, 2, 3, 4]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if i != j :
#             print(numbers[i],numbers[j])


# numbers = [4, 7, 2, 9, 6]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if j > i and numbers[i] + numbers[j] == 10:
#             print(numbers[i], numbers[j])
            
# numbers = [4, 7, 2, 9, 6, 3, 8]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if j > i and numbers[i] + numbers[j] == 11:
#             print(numbers[i],numbers[j])


# numbers = [4, 7, 2, 4, 9, 7, 2]

# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#             if numbers[i] == numbers[j]:
#                 print(numbers[i],"found at index :", j)



numbers = [4, 7, 9, 4]

for i, number in enumerate(numbers):

    print(i, number)


