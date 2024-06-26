def prime_numbers(num:int)->bool:
    if num == 1:
        return True
    elif num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(f"\n {num} is divisible by {i}")
                return False
                break
        print(f"\n {num} is not divisible")
        return True
    return False

print(prime_numbers(300))
print(prime_numbers(143))
print(prime_numbers(19))
print(prime_numbers(35))
print(prime_numbers(25))
print(prime_numbers(9))