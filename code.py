import sys
import time

D_file = open("D's.txt","w")
global byte_count
byte_count = 0

def stop_program():
    print("\n", byte_count, "characters in file", "\n")
    D_file.close()
    sys.exit()


def create_characters(num_lines):
    global byte_count
    repeat = num_lines
    while byte_count < repeat:
        D_file.write("D")
        byte_count += 1
        if byte_count % 100 == 0:
            D_file.write("\n")
            time.sleep(0.00001)    
    stop_program()

print("Previous Characters have been eraced")
num_Ds = int(input("How many characters do you want -- >"))
create_characters(num_Ds)