# first function
def hello():
    print("Hello there, human.")


hello()


# second function
def pack(a, b, c):
    return [a, b, c]


print(pack("foo", "bar", "zap"))


# third function
def eat_lunch(food_list):
    if len(food_list) > 0:
        print(f"First, I eat {food_list[0]}.")
    if len(food_list) > 1:
        count = 1
        for i in food_list[1:]:
            print(f"Next, I eat {food_list[count]}.")
            count += 1
    if len(food_list) == 0:
        print("My lunchbox is empty!")


my_lunch = ["apple", "orange", "chocolate"]
eat_lunch(my_lunch)
