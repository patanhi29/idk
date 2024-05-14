def encode(message):
    m = len(message)
    r = 1
    while 2 ** r < m + r + 1:
        r += 1

    encoded_message = ['0'] * (m + r)
    parity_positions = [2 ** i for i in range(r)]

    j = 0
    for i in range(1, m + r + 1):
        if i not in parity_positions:
            encoded_message[i - 1] = message[j]
            j += 1

    for i in range(r):
        parity = 0
        for j in range(1, m + r + 1):
            if j & (2 ** i):
                parity ^= int(encoded_message[j - 1])
        encoded_message[2 ** i - 1] = str(parity)

    return ''.join(encoded_message)

def decode(received_codeword):
    r = 1
    while 2 ** r < len(received_codeword):
        r += 1

    error_position = 0
    syndrome = 0

    for i in range(r):
        parity = 0
        for j in range(1, len(received_codeword) + 1):
            if j & (2 ** i):
                parity ^= int(received_codeword[j - 1])
        syndrome += parity * (2 ** i)

    if syndrome != 0:
        error_position = syndrome

    if error_position != 0:
        # Correct the error
        received_codeword = list(received_codeword)
        received_codeword[error_position - 1] = str(int(received_codeword[error_position - 1]) ^ 1)
        received_codeword = ''.join(received_codeword)

    decoded_message = ''
    j = 0
    for i in range(1, len(received_codeword) + 1):
        if i & (i - 1) != 0:
            decoded_message += received_codeword[j]
            j += 1

    return decoded_message

def main():
    data = input("Enter 7/8 bits data to be transmitted: ")
    encoded_message = encode(data)
    print("Transmitted codeword:", encoded_message)

    received_codeword = input("Enter received codeword: ")

    decoded_message = decode(received_codeword)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()
