image = [[224, 13, 98], [155, 2, 50], [99, 50, 14], [15, 55, 22],
[155, 61, 87], [63, 30, 17], [1, 54, 19], [99, 81, 66],
[219, 77, 91], [69, 39, 50], [18, 200, 33], [25, 54, 3]]

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