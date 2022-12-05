import sys


## All these if & else statements should be within the commands not before. So if len 1 print too little, if len > 2 too many arguments and then if len ==2 then under it with an indent put
#217, invert etc. command.
# command error too much or too little
if len(sys.argv) == 1:
    print("usage: Too little or no arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("usage: Too many arguments")
    sys.exit()
# unknown argument
if sys.argv[1] == "217" or sys.argv[1] == "invert":
    print("executing command")
else:
    print("Unknown Command", sys.argv[1])
    sys.exit()

# pbm file
p1 = input()
width_height = int(input().split())
pbm_list = []

# outputing the 217 file
if sys.argv[1] == "217":
    SENTINEL = "END"
    current_checksum = 0
    Human_text = input()
    Number_of_sections = int(input())
    image_section = input()
    width = int(input())
    height = int(input())
while True:
    #use this try loop
    try:
        #You dont need to convert it to integer.
        zeros_ones_input = int(input())
        s = input()
    except EOFError:
        #Print checksum here
        break

#In total I had 4 inputs. Not sure why you have so many. Your first input is P1, then width,height then for 217 in the while true loop and then one for invert in the while true loop.
