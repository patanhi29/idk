def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword

def crc_encode(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def crc_decode(received_codeword, key):
    l_key = len(key)
    remainder = mod2div(received_codeword, key)
    if '1' in remainder:
        return False
    else:
        return True

def main():
    data = input("Enter data to be transmitted (ASCII): ")
    key = input("Enter CRC key (ASCII): ")

    transmitted_codeword = crc_encode(data, key)
    print("Transmitted codeword:", transmitted_codeword)

    received_codeword = input("Enter received codeword (ASCII): ")

    if crc_decode(received_codeword, key):
        print("No error detected. Data is correct.")
    else:
        print("Error detected. Data is corrupt.")

if __name__ == "__main__":
    main()
