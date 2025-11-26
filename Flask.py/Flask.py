# 1
# n = int(input())
# frost = 0
# cool = 0
# normal = 0
# hot = 0

# for _ in range(n):
#     temp = float(input())
#     if temp < 0:
#         frost += 1
#     elif 0 <= temp <= 15:
#         cool += 1
#     elif 15 < temp <= 25:
#         normal += 1
#     else:
#         hot += 1

# print(f"мороз: {frost}")
# print(f"прохладно: {cool}")
# print(f"нормально: {normal}")
# print(f"жарко: {hot}")


# 2
# password = input()

# has_digit = False
# has_letter = False

# if len(password) >= 8:
#     for char in password:
#         if char.isdigit():
#             has_digit = True
#         elif char.isalpha():
#             has_letter = True
    
#     if has_digit and has_letter:
#         print("OK")
#     else:
#         print("WEAK")
# else:
#     print("WEAK")



# 3
# numbers = []
# while True:
#     user_input = input()
#     if user_input == "stop":
#         break
#     numbers.append(int(user_input))

# if numbers: =======
#     total = 0
#     minimum = numbers[0]
#     maximum = numbers[0]
    
#     for num in numbers:
#         total += num
#         if num < minimum:
#             minimum = num
#         if num > maximum:
#             maximum = num
    
#     print(f"сумма: {total}")
#     print(f"минимум: {minimum}")
#     print(f"максимум: {maximum}")
# else:
#     print("Нет введённых чисел")



# 4
# a = int(input())
# b = int(input())
# n = int(input())

# for i in range(1, n + 1):
#     if i % a == 0 and i % b == 0:
#         print("FizzBuzz")
#     elif i % a == 0:
#         print("Fizz")
#     elif i % b == 0:
#         print("Buzz")
#     else:
#         print(i)

# 5
# w = int(input())
# h = int(input())

# for row in range(h):
#     for col in range(w):
#         if row == 0 or row == h - 1 or col == 0 or col == w - 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()  



# B
# 2.
# prices = {"apple": 50, "banana": 30, "cherry": 120, "milk": 90}
# cart = ["apple", "banana", "banana", "milk", "potato", "apple"]

# cart_count = {}
# for item in cart:
#     cart_count[item] = cart_count.get(item, 0) + 1
# print(cart_count)
# sum = 0
# for item, count in cart_count.items():
#     if item in prices:
#         sum += prices[item] * count
# print(sum)

# m = [item for item in cart_count.keys() if item not in prices]
# print(m)
