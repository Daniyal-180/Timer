import time

def count_down(number):
    print(f"!__Count_down Timer Starts Now__!")

    while number>0:
        print(f"\t The remaining time is {number}")
        time.sleep(1)
        number -= 1

number = int(input("Enter a count down second:"))
count_down(number)