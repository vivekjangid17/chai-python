# if any number is prime then there is no factors other than 1 and itself.
# 2 is the smallest prime number.
# logic for prime number

n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number")
            
