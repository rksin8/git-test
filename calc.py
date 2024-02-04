# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
print("1. To add\n2. To substract\n3. To Multiply\n4. To divide")
choice = input("Select operation (1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
            num0 = float(input("Enter first number: "))
            num1 = float(input("Enter second number: "))
            
            if choice == '1':
                print( num0 + num1)
            elif choice == '2':
                print( num0 - num1)
            elif choice == '3':
                print( num0 * num1)
            elif choice == '4':
                print( num0 / num1)
else:
    print('unknown operator!')
    print(None)


# this project has been finished!
# this calculator workds for +, -, *.,/
# git push origin master
