def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for j in range(1, number+1):
        print(str(j).rjust(width) + " " + oct(j)[2:].rjust(width)+ " " + hex(j)[2:].rjust(width)+ " " + bin(j)[2:].rjust(width))
        
        

if __name__ == '__main__':
    n = 17
    print_formatted(n)      