def decodeRekvizitaiIP(encodedIP):
    decoded_decimal = ("00000000" + str(int(encodedIP, 32)))[-12:]
    chunks = [str(int(decoded_decimal[i:i+3])) for i in range(0, len(decoded_decimal), 3)]
    return '.'.join(chunks)


while True:
    print(decodeRekvizitaiIP(input("Enter Encoded IP: ")) + "\n")