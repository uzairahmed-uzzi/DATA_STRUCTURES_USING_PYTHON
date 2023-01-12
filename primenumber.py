inrange=int(input("TELL US THE RANGE OF PRIME NUMBERS YOU WANT: "));
check=True
for num in range(2,inrange):
    for i in range(2,inrange):
        if num!=i:
            if num%i==0:
                break 
        else:
            print(f"PRIME NUMBER {num}")
                            
                  
        
