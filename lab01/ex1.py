def main():
    print("This program illustrates a chaotic function")
    print("This is the change i have made")
    x = float(input("Enter a number between 0 and 1: "))
    z = float(input("Enter the second number between 0 and 1: "))
    y = int(input("Enter the number of values to print: "))
    print("input:",x,"", z,"",1) 
    for i in range(y):
            x = 2.0 * x * (1 - x)
            z = 2.0 * z * (1 - z)
           
            print("    ",x, z)
main()
