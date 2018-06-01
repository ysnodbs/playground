# A program that prints all the odd number in the range of value that user entered except those divisible by 5
def main():
    number = int(input("Enter the number: "))
    if isinstance(number,int):
      for i in range (1,number+1):
         if(i%2!=0 and i%5 !=0):
            print(i)
main()        