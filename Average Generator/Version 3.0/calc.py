print("Welcome to Python Average Calculator Developed --  By Jay")
print("\nEnter how many numbers do you want the average of: ")
def avg(num_n):
    """
    This is a Function to Calculate the Average of Unlimited Numbers
    """
    global Sum
    Sum = 0
    nums = 0
    n = None
    for i in range(num_n):
        i += 1
        try:
            n = (input(f"\nEnter number {i}: "))
            nums = int(n)
            print(f"{nums}")
        except ValueError:
            nums = len(n)
            print(f"{nums}")
        Sum = Sum + i
        pass
    average = Sum / nums
    print(f"\nAverage == {average}")
num_nu = 0
num = None
try:
    num = input()
    num_nu = int(num)
    avg(num_nu)
except ValueError as ve:
    num_nu = len(num)
    avg(num_nu)