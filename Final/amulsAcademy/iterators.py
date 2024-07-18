# def print_each(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             item = next(iterator)
#         except StopIteration:
#             break
#         else:
#             print(item)
#
# print_each([1,2,3,4,5,6])


list = [1,2,3,4]
for a in list:
    list.append(a)
print(list)