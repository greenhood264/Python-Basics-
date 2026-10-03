# functions

# def hello():
#     return "hello how are you"

# print(hello())


# lists

# a = [12, 13, 14, 15, 16, 34.5]

# for i in a:
#     print(i)


# positive and negative elements

# l = [-45, 67, 12, -68, -69, 34]

# for i in l:
#     if i >= 0:
#         print("positive:", i)
#     else:
#         print("negative:", i)


# average of list

# l = [12, 435, 67, 89, 23, 25, 69]

# sum = 0
# for i in l:
#     sum += i

# print(sum / len(l))


# largest element and its index

# l = [12, 567, 43, 235, 347, 568, 45, 7]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"largest number is {largest} at index {index}")


# second largest

# l = [12, 16, 13, 19, 17]

# largest = l[0]
# second = l[0]

# for i in l:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second:
#         second = i

# print(second, largest)


# check sorted list

# a = [12, 13, 18, 15, 16]

# for i in range(len(a) - 1):
#     if a[i] > a[i + 1]:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")


# tuples

# a = (1, 2, 3, 4, 5, 5, 5.5, "hello")

# print(a.count(5))

# a = (1,)
# print(type(a))


# sets

# a = {1, 8, 9, "hello", 2, 3, 4, 5}

# for i in a:
#     print(i)

# a.clear()
# print(a)


# set difference

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(b - a)


# dictionaries

# d = {10: 100, 20: 200, 30: 300}

# d[10] = 150      # update
# d[40] = 400      # create
# del d[30]        # delete

# print(d)


# dictionary items

# d = {10: 100, 20: 200, 30: 300}

# print(d.items())


# merge two dictionaries

# d1 = {10: 100, 20: 200, 40: 300}
# d2 = {40: 400, 50: 500, 60: 600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# sum of dictionary values

# d = {10: 100, 20: 200, 40: 300}

# sum = 0

# for i in d:
#     sum += d[i]

# print(sum)


# count frequency of elements

# a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8]

# d = {}

# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)


# add values of common dictionary keys

# d1 = {10: 100, 20: 200, 40: 300}
# d2 = {40: 400, 50: 500, 60: 600}

# for i in d2:
#     if i in d1:
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)
