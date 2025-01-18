# # from operator import length_hint
# # from collections import Counter
# #
# # # # # Python program to interchange first and last elements in a list
# # # # size = int(input('Enter the size for list: '))
# # # # l1 = [input('Enter element: ') for _ in range(size)]
# # # # l1[0], l1[len(l1)-1] = l1[len(l1)-1], l1[0]
# # # # print(l1)
# # #
# # # # Python program to swap two elements in a list
# # # size = int(input('Enter the size for list: '))
# # # l1 = [input('Enter element: ') for _ in range(size)]
# # # print('original list = ', l1)
# # # i1 = int(input('Enter index to swap: '))
# # # i2 = int(input('Enter index to swap: '))
# # # l1[i1], l1[i2] = l1[i2], l1[i1]
# #
# # # Python | Ways to find length of list
# #
# #
# # def length(new_list):
# #     if not new_list:
# #         return 0
# #     return 1 + length(new_list[1:])
# #
# #
# # # using len, length_hint, counter, recursion, sum, enumerate, list comprehension
# # size = int(input('Enter the size for list: '))
# # l1 = [input('Enter element: ') for _ in range(size)]
# # print('length of list using len: ', len(l1))
# # print('length using length hint', length_hint(l1))
# # print('length using sum: ', sum(1 for _ in l1))
# # print('length using recursion: ', length(l1))
# # print('length using list comprehension: ', sum([1 for _ in l1]))
# # counter = 0
# # for _ in l1:
# #     counter += 1
# # print('length using counter variable: ', counter)
# # s = 0
# # for i, a in enumerate(l1):
# #     s += 1
# # print('length using enumerate: ', s)
# # print('length using Counter from collection: ', sum(Counter(l1).values()))
#
# # Maximum of two numbers in Python
#
# num1 = int(input('enter a number: '))
# num2 = int(input('enter a number: '))
# print(max(num1, num2), '>=', min(num1, num2))
# print(num1 if num1 >= num2 else num2)
# maximum = lambda a, b: a if a >= b else b
# print(maximum(num1, num2))

# Python program to check whether the string is Symmetrical or Palindrome
word = input('enter a word: ')
print('palindrome' if word == word[::-1] else 'not palindrome')
print('symmetrical' if word[:len(word)//2] == word[-(len(word)//2):] else 'not symmetrical')

