from sys import argv

script, filename = argv

print(f"Opening file {filename}:")
target = open(filename)
# print(target.readline(0))
# print(target.readline(1))
# print(target.readline(2))

print("Reading the file all at once")
print(target.read())

target.close()