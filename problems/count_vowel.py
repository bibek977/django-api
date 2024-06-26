vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

y = 0
for i in vowels:
    for j in ip_str:
        if i == j:
            y += 1

print(y)