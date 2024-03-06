def main():
    x = int(input(f"Enter a number: "))
    y = int(input(f"Enter another number: "))
    print(f"1. Addition\n2. Subtract\n3. Multiply\n4. Divide")
    choice = int(input(f"Enter the choice: "))
    
    ans = 0
    flag = 0
    
    try:
        if choice == 1:
            ans = x + y
            flag = 1
        elif choice == 2:
            ans = x - y
            flag = 1
        elif choice == 3:
            ans = x * y
            flag = 1
        else:
            ans = x / y
            flag = 1
    except:
        print("Error while performing Operation")
    
    if flag == 1:
        print(f"\nSolution is: ", ans)
        
main()
    
        