import math
def isPrime(n): #判断素数
    max = math.floor(math.sqrt(n)) + 1
    for i in range(2,max):
        if n % i == 0:  #factor found
            return 0
    return 1

def isDigitPrime(n):    #判断每位和素数
    nlist = []
    sum = 0

    while n >= 10:
        # print(n%10)
        nlist.append(n%10)
        sum += n%10

        n = int(n/10)

    # print(n)
    nlist.append(n) #get digit  取每一位

    sum += n
    print(sum, end = " ")
    print(nlist, end = ' ')
    print(isPrime(sum))

    return isPrime(sum)



count = 0
sum = 0
# print(isDigitPrime(123))


# nlist = list(map(int,str(123)))

# for i in nlist:
#     sum = sum + i
# print(sum)

start = 1000001
result = ''

while count < 2:
    if isPrime(start) and isDigitPrime(start):
        count = count + 1
        print(start)
        result += str(start)
    start =  start + 1
print(result)