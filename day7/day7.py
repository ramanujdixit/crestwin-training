# from pathlib import Path

# path = Path("f1.txt")
# print(path.exists())
# print(path.name)
# print(path.suffix)

# file = Path("f1.txt")
# print(file.read_text())
# file.write_text("this is done using pathlib")
# print(file.read_text())


# with open("sample.txt", "w") as f:
#     f.write(
#         "my name is ramanuj dixit, my age is 79 years, and residence in Nicobar island"
#     )

# with open("sample.txt", "r") as f:
#     print(f.read())
#     f.seek(0)
#     total_lines = len(f.readlines())
#     print(total_lines)

#     f.seek(0)
#     content = f.read()
#     total_words = len(content.split())
#     print(total_words)


# with open("sample.txt", "a") as f:
#     f.write("\nnew content appended in existing file")

# with open("sample.txt", "r") as f:
#     print(f.read())

# import csv

# with open("customer_segmentation.csv", "r") as f:
#     rows = csv.reader(f)
#     for i in rows:
#         print(i)

# with open("customer_segmentation.csv", "r") as f:
#     dictionary = csv.DictReader(f)
#     for i in dictionary:
#         print(i["Education"], ":", i["Income"])


# import pdb


# def addition(a, b):
#     answer = a + b
#     return answer


# pdb.set_trace()
# x = input("Enter first number : ")
# y = input("Enter second number : ")
# sum = addition(x, y)
# print(sum)
