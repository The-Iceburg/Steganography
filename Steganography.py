# this is the original image
image = [[225, 12, 99], [155, 2, 50], [99, 51, 15], [15, 55, 22],
[155, 61, 87], [63, 30, 17], [1, 55, 19], [99, 81, 66],
[219, 77, 91], [69, 39, 50], [18, 200, 33], [25, 54, 190]]

print(image)

# the binary conversion of the image as a list of binary values
binary = []

length = (len(image) * 3 - 1)// 8

# the message to be encoded
message = str(input("Please enter a message to be encoded. With the current image this cannot be longer than " + str(length) + " characters\n"))

while len(message) > length:
    print("Your submitted message is longer than the excepted " + str(length) + " characters. Please enter another which meets our requirements")
    message = str(input("Please enter a message to be encoded. With the current image this cannot be longer than " + str(length) + " characters\n"))

# for all the sets of "RGB" in the image
for i in range(len(image)):

    # for each "R","G" & "B"
    for j in range(3):

        # changes the value into its binary form
        string = format(image[i][j], "b")

        # pads each number out with "0" until it is 8 characters long
        string = str(string).rjust(8, '0')

        # adds this converted value to the list binary
        binary.append(string)

# subroutine which converts strings to binary
def toBinary(string):

    # declares 2 lists
    unicodeval,binaryconv=[],[]
    
    # for index in message
    for i in string:
        
        # adding each unicode value for every character in string to list l
        unicodeval.append(ord(i))

    # for each unicode value
    for i in unicodeval:

        # converts this unicode value to binary
        binaryuni = (int(bin(i)[2:]))

        # pads each number out with "0" until it is 8 characters long
        binaryuni = str(binaryuni).rjust(8, '0')

        # adds this to a list named binary conversion
        binaryconv.append(binaryuni)

    # returns this binary converted list
    return binaryconv

# runs subroutine and curates list
binconperchar = toBinary(message)

# defines new list
binsepperchar = []

# seperates each binary value into an individual entrie in a list
for i in range(len(binconperchar)):
    for j in range(8):
        binsepperchar.append(binconperchar[i][j])

for i in range(len(binsepperchar)):
    if binary[i][7] == "1" and binsepperchar[i] == "0":
        binaryint = int(binary[i])
        binaryint -= 1
        binaryint = str(binaryint).rjust(8, '0')
        binary[i] = binaryint
    elif binary[i][7] == "0" and binsepperchar[i] == "1":
        binaryint = int(binary[i])
        binaryint += 1
        binaryint = str(binaryint).rjust(8, '0')
        binary[i] = binaryint

for i in range(len(binary)):
    dec_number= int(binary[i], 2)
    binary[i] = dec_number

n = 3
binary = [binary[i:i+n] for i in range(0, len(binary), n)]

binary[-1][2] = len(message)

print(binary)
