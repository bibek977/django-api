low = 100
high = 205

list_prime = []

for i in range(low,high+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                x = None
                break
            x = i
    if x:
        list_prime.append(x)

print(list_prime)