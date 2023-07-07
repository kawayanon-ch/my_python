""" หลักการ จำนวนนั้นต้องไม่เป็นเลขคู่ ยกเว้น '2' 
    ใช้การหารลงตัวโดยเพิ่มจำนวนไปเรื่อยๆ จนถึงตัวเลขก่อนจำนวนที่ต้องการ """

def is_prime(N):
    
    is_prime = True

    if N < 2:
        is_prime = False
    else:
        for i in range(2, N):
            if N % i == 0:
                is_prime = False
                break
            
    if is_prime:
        print("Your input {} is prime number".format(N))
    else:
        print("Your input {} is not prime number".format(N))

N = int(input("Enter the positive integer : "))

is_prime(N)
