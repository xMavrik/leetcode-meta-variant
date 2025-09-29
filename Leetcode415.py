
a = "91.564"
b = "524.6"


def calcString(num1, num2):


    num1_int, num1_dec = num1.split(".")

    num2_int, num2_dec = num2.split(".")


    if len(num1_dec) < len(num2_dec):
        num1_dec = num1_dec + "0" * (len(num2_dec) - len(num1_dec))
    else:
        num2_dec =  num2_dec + "0" * (len(num1_dec) - len(num2_dec))

    if len(num1_int) < len(num2_int):
        num1_int = "0" * (len(num2_int) - len(num1_int)) + num1_int
    else:
        num2_int = "0" * (len(num1_int) - len(num2_int)) + num2_int

    response = ""

    carry = 0

    for x in range(len(num1_dec) - 1, -1, -1):

        curr_sum = int(num1_dec[x]) + int(num2_dec[x]) + carry

        carry = curr_sum // 10

        response += str(curr_sum % 10)

    response += "."

    for y in range(len(num1_int) - 1, -1, -1):

        curr_sum = int(num1_int[y]) + int(num2_int[y]) + carry

        carry = curr_sum // 10

        response += str(curr_sum % 10)


    if carry > 0:
        response += "1"

    return response[::-1]


print(calcString(a, b))
    

