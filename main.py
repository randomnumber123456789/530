num=int(input("give me random number: "))
numbers = [45,67,3,4,85,2,6,9]
def is_even():
    print(bool(num%2==0))
def list_sum():
    final_num = 0
    for number in numbers:

        final_num += number

    print("sum from this number is",final_num)

is_even()
list_sum()
