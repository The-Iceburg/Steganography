from PIL import Image
import numpy as np


menuChoice = input("##############################################\nPlease select your option from the list below:\n1. Encode\n2. Decode\n##############################################\n")

if menuChoice == "1":
    imageORIGINAL = "Shiverian.png"
    image = Image.open(imageORIGINAL)

    image_array = np.array(image)
    w, h = image.size

    image_rgb = image.convert("RGB")

    values = []

    for i in range(h):
        for j in range(w):
            listpixel = list(image_rgb.getpixel((j,i)))
            values.append(listpixel)

    # Load all pixels from the image.
    orig_pixel_map = image.load()

    # Create a new image matching the original image's color mode, and size.
    # Load all the pixels from this new image as well.
    new_image = Image.new("RGB", (w, h))
    new_pixel_map = new_image.load()
            
    # the binary conversion of the image as a list of binary values
    binary = []

    length = (len(values) * 3 - 1)// 8

    # the message to be encoded
    message = str(input("Please enter a message to be encoded. With the current image this cannot be longer than " + str(length) + " characters\n"))

    while len(message) > length:
        print("Your submitted message is longer than the excepted " + str(length) + " characters. Please enter another which meets our requirements")
        message = str(input("Please enter a message to be encoded. With the current image this cannot be longer than " + str(length) + " characters\n"))

    # for all the sets of "RGB" in the image
    for i in range(len(values)):

        # for each "R","G" & "B"
        for j in range(3):

            # changes the value into its binary form
            string = format(values[i][j], "b")

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

    x = 0
    y = 0

    for length1 in range(0, len(binary)):
        if (x + 1) == w:
            new_r = binary[length1][0]
            new_g = binary[length1][1]
            new_b = binary[length1][2]
            new_pixel = (new_r, new_g, new_b)
            new_pixel_map[x, y] = new_pixel
            y += 1
            x = 0
        else:
            new_r = binary[length1][0]
            new_g = binary[length1][1]
            new_b = binary[length1][2]
            new_pixel = (new_r, new_g, new_b)
            new_pixel_map[x, y] = new_pixel
            x += 1
        binary[-1][2] = len(message)

    new_image.show()

    new_name = "Steganography " + imageORIGINAL
    new_image.save(new_name)

elif menuChoice == "2":
    
    imageSteg = "Steganography Shiverian.png"
    imageS = Image.open(imageSteg)

    image_array = np.array(imageS)
    w, h = imageS.size

    image_rgb = imageS.convert("RGB")

    image = []
    for i in range(h):
        for j in range(w):
            listpixel = list(image_rgb.getpixel((j,i)))
            image.append(listpixel)

    orig_pixel_map = imageS.load()

    length = image[-1][2] * 8
    binary,values = [],[]

    for i in range(len(image)):
        
        for j in range(3):
            string = format(image[i][j], "b")
            string = str(string).rjust(8, '0')
            binary.append(string)

    for i in range(length):
        values.append(str(binary[i][-1]))

    n = 8
    values = [values[i:i+n] for i in range(0, len(values), n)]

    for i in range(len(values)):
        fullbin = "".join(values[i])
        values[i] = int(fullbin, 2)
        values[i] = str(chr(values[i]))

    message = "".join(values)

    print(message)
