def hcf_number(x,y):
    if x>y:
        smaller = x
    else:
        smaller = y
    
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            num = i
    return num
    
# print(hcf_number(24,54))

def lcm_number(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    
    while(True):
        if greater%x==0 and greater%y==0:
            num = greater
            break
        greater += 1
    return num

print(lcm_number(24,54))

