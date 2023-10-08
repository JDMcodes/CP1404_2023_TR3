# names = ['Ada', "Alan", "Bill", "Jon"]
# print(", ".join(names))
# name_to_remove = input("who do you want to remove?")
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print("name not in list")
#     name_to_remove = input("who do you want to remove?")
# print(f"names in the list: " + ", ".join(names))

# things = [True, 1.2, "GOOD", [1, 10]]
# print(things[-2])
# print("%".join([things[2][1:-1]]))
# print([str(t)[0] for t in things])
# print([len(str(t)) for t in things])
# print([t for t in things if type(t) in (float,int)])
# print([t for t in things if isinstance(t, int)])


# values = [[3,4,5,1], [33,6,1,2]]
# v = values[0][0]
# for row in range(0, len(values)):
#     for column in range(0, len(values[row])):
#         if v < values[row][column]:
#             v = values[row][column]
# print(v)

def main():
    numbers = get_numbers()
    squared_numbers = square_numbers(numbers)
    display_numbers(numbers, squared_numbers)

def get_numbers():
    numbers = []
    try:
        number = input('enter a number')
        if number == "":
            return
        number = float(number)
        numbers.append(number)
    except ValueError:
        print("number should be float")
    while numbers[-1] != "":
        try:
            number = input('enter a number')
            if number == "":
                break
            number = float(number)
            numbers.append(number)
        except ValueError:
            print("number should be float")
    return numbers

def square_numbers(numbers: list):
    squared_numbers = []
    for i in range(0, len(numbers)):
        squared_numbers.append(numbers[i]**2)
    return squared_numbers

def display_numbers(numbers, square_numbers):
    for i in range(0, len(numbers)):
        print(f"The square of {numbers[i]} is {square_numbers[i]}")

main()


