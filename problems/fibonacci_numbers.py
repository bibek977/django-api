series_data = []
def fibonacci_number(num:int)->int:
    if num < 0:
        raise ValueError("Please Enter postive number")
    elif num==1 or num==0:
        return num
    return (fibonacci_number(num-1)+fibonacci_number(num-2))

print(fibonacci_number(5))
n = 9
for i in range(n):
    series_data.append(fibonacci_number(i))


print(series_data)