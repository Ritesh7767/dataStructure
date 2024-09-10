def evenlyDivide(number):

    num = str(number)
    count = 0

    for i in num:
        if number % int(i) == 0:
            count += 1
    return count

# print(evenlyDivide(34))

# name = "ritesh"

# for i in name:
#     print(i)

# print(2/0)
# print('ritesh'.split())
# print(list('ritesh'))
# arr = list("ritesh")
# print(str(arr))
# print("".join(arr))
# arr = list(12344)
# print(arr)

def reverseString(number):

    isNegative = False
    if number < 0:
        isNegative = True
        print(number)
        number *= -1
        print(number)
    arr = list(str(number))

    left = 0
    right = len(arr) -1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    number = int("".join(arr))
    if isNegative: number *= -1

    return number

# print(reverseString(-234))

# def gcd(a,b):

#     while a % b > 0:
#         a, b = b,a%b
#     return b

# print(gcd(4,8))

# def func1():
#     print("ritesh")
#     def func2():
#         print("gupta")
#     print("laxman")

# func1()


def gcdAndLcm(a, b):

    def gcd(a, b):

        while b:
            a, b = b, a%b
        return a
    
    return (a*b)//gcd(a, b)

def fullname():
    return "ritesh", "laxman"

# print(fullname())


def isArmstrong(number):

    arr = list(str(number))
    sum = 0
    size = len(arr)
    for i in arr:
        sum += int(i) ** size
    return sum == number

# print(isArmstrong(9474))

def divisors(number):

    if number == 1:
        return 1
    sum = 1
    for i in range(2, number+1):
        if number % i == 0:
            sum += i

    return sum

# print(divisors(6))
def sumOfDivisors(Num):

    result = 0

    for i in range(1, Num+1):
        result += divisors(i)

    return result

# print(sumOfDivisors(4))

def isPrime(dividend, divisor=2):

    if dividend == 1:
        return "1 is neither prime nor composite"

    if divisor == dividend:
        return True
    
    if dividend % divisor == 0:
        return False
    return isPrime(dividend, divisor + 1)

def printN(number):

    if number == 1:
        print(1)
        return 
    printN(number-1)
    print(number)

printN(64)
print(65, end=" ")
print("ritesh")

