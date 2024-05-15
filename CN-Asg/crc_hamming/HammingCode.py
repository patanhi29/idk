def main():
    data = [0] * 8
    data_at_rec = [0] * 8

    print("Enter 4 bits of data one by one:")
    data[7] = int(input("Enter bit 1: "))
    data[6] = int(input("Enter bit 2: "))
    data[5] = int(input("Enter bit 3: "))
    data[3] = int(input("Enter bit 4: "))

    # Calculation of even parity bits
    data[4] = data[5] ^ data[6] ^ data[7]
    data[2] = data[3] ^ data[6] ^ data[7]
    data[1] = data[3] ^ data[5] ^ data[7]

    print("\nEncoded data is:")
    for i in range(1, 8):
        print(data[i], end="")
    print()

    print("\nEnter received data bits one by one:")
    for i in range(1, 8):
        data_at_rec[i] = int(input(f"Enter bit {i}: "))

    # Calculation of parity check bits at receiver's end
    c1 = data_at_rec[1] ^ data_at_rec[3] ^ data_at_rec[5] ^ data_at_rec[7]
    c2 = data_at_rec[2] ^ data_at_rec[3] ^ data_at_rec[6] ^ data_at_rec[7]
    c3 = data_at_rec[4] ^ data_at_rec[5] ^ data_at_rec[6] ^ data_at_rec[7]
    c = c3 * 4 + c2 * 2 + c1

    if c == 0:
        print("\nCongratulations, there is no error.")
    elif c > 7 or c < 1:
        print(f"\nError detected but position {c} is invalid.")
    else:
        print(f"\nError at position: {c}")
        print("Corrected message is:")
        data_at_rec[c] = 1 if data_at_rec[c] == 0 else 0
        for i in range(1, 8):
            print(data_at_rec[i], end="")
    print()

if __name__ == "__main__":
    main()
