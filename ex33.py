# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


#     print("The numbers: ")

#     for num in numbers:
#         print(num)

print('Drills:')
numbers2 = []


# drill 1
# def while_func(lim, incr):
#     i = 0
#     while i < lim:
#         numbers2.append(i)
#         i += incr


# drill 5: for-loop and range
def loop_n_range_func(lim, incr):
    for i in range(0, lim, incr):
        numbers2.append(i)
test_run = loop_n_range_func(6, 2)
print(numbers2)

