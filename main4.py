print("Numbers form 10 to 20")
for num in range(10,21):
    print(num , end="")
    print()

print("Numbers from 10 to 2 in steps of 2")
for num in range(10, 21, 2):
    print(num , end=" ")
print()
print("finish")




gap = int(input("What is the gap?"))
print(f"numbers in steps of {gap}:")
for num in range(10, 21, gap):
    print(num, end=" ")
    print()
print("finish")

start = int(input("what is the starting point?"))
end = int(input("what is the ending point?"))
gap = int(input("what is the gap?"))
print(f"numbers from {start} to {end} in steps of {gap}")
for num in range(start , end , gap):
    print(num ,end="")
    print()
print("finish")