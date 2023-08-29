import random

names = input("Who is going to buy the bill? ")

names_lists = names.split(", ")

print(names_lists)

names_length = len(names_lists)

print(names_length)

print(f"Today {names_lists[names_length-1]} will pay the bill.")

print(f"Today {random.choice(names_lists)} will pay the bill.")