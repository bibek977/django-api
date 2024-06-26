def number(num):

    num_str = str(num)
    num_len = len(num_str)

    num_total = sum(int(x)**num_len for x in num_str)

    if num == num_total:
        return True

    return False

print(number(153))

sum_natural_numbers = sum([x for x in range(1,16+1)])
print(sum_natural_numbers)

my_list = [1,2,3,4,5,6,7,8,9,10]

# filter_divisible = list(filter(lambda x: x%2==0,my_list))
filter_divisible = list(filter(lambda x: x%2==0,[i for i in range(1,50)]))
print(filter_divisible)