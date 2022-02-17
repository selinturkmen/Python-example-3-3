import string
import math


def phone_converter(a):
 
    print('phone_alpha:', a)
    numerical_phone_num = ''
    if len(a)!= 12:
     print(-2)
    elif a[0] == '0':
      print(-1)   
    else:
     for char in a:
         if char == 'A' or char == 'B' or char == 'C' or char == 'a' or char == 'b' or char == 'c':
             char = '2'
         elif char == 'D' or char == 'E' or char == 'F'or char == 'd' or char == 'e' or char == 'f':
             char = '3'
         elif char == 'G' or char == 'H' or char == 'I' or char == 'g' or char == 'h' or char == 'i':
             char = '4'
         elif char == 'J' or char == 'K' or char == 'L' or char == 'j' or char == 'k' or char == 'l':
             char = '5'
         elif char == 'M' or char == 'N' or char == 'O' or char == 'm' or char == 'n' or char == 'o':
             char = '6'
         elif char == 'P' or char == 'Q' or char == 'R' or char == 'S' or char == 'p' or char == 'q' or char == 'r' or char == 's':
             char = '7'
         elif char == 'T' or char == 'U' or char == 'V' or char == 't' or char == 'u' or char == 'v':
             char = '8'
         elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z'or char == 'w' or char == 'x' or char == 'y' or char == 'z':
             char = '9'
         numerical_phone_num = numerical_phone_num + char
    return numerical_phone_num





def main():

    print(phone_converter("555-GET-FOOD"))
    print(phone_converter("310-EaT-MeaT"))
    print(phone_converter("12E-456-789T"))
    print(phone_converter("444-EAT-CHICKEN"))
    print(phone_converter("444EATMEAT"))
    print(phone_converter("090-EAT-MEAT"))   
    

    
################################################################ 

if __name__ == '__main__':
    main()
