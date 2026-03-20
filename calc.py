import time

print("""
 ______     ______     __         ______    
/\  ___\   /\  __ \   /\ \       /\  ___\   
\ \ \____  \ \  __ \  \ \ \____  \ \ \____  
 \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_____/   \/_/\/_/   \/_____/   \/_____/ 
""")
while True:
    print("+")
    time.sleep(1)
    a = int(input("enter number:"))
    b = int(input("enter number"))
    print("Result (+)=")
    print(a + b)
    print("*")
    time.sleep(1)
    c = int(input("enter number:"))
    d = int(input("enter number:"))
    print("Result (*)=")
    print(c * d)
    print("-")
    time.sleep(1)
    e = int(input("Biggest number: "))
    f = int(input("The smaller one: "))
    print(e - f)
    print(":")
    time.sleep(1)
    g = int(input("Enter the bigger number:"))
    h = int(input("enter the smaller number"))
    print(g / h)
end