def print_line(char,times):
    print(char*times)
    print("end")

def print_line_muilt(char,times,muilt):
    index=0
    while index<muilt:
        print_line(char,times)
        index+=1

print_line('-',50)
print_line_muilt('-',50,3)