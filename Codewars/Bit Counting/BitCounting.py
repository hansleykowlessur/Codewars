def count_bits(n):
    binaryNumber = bin(n).replace("0b","")
    # Convert to string
    binaryNumberToString = str(binaryNumber)
    # Count number of 1s from string
    numberOfOne = binaryNumberToString.count("1")
    return numberOfOne