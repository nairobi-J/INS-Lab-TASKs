import sys

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

def count_same_bits(hex1, hex2):
    bin1 = hex_to_bin(hex1)
    bin2 = hex_to_bin(hex2)
    
    same_bits = 0
    total_bits = len(bin1)
    
    for i in range(total_bits):
        if bin1[i] == bin2[i]:
            same_bits += 1
    
    return same_bits, total_bits

if __name__ == "__main__":
    hex1 = "dd7c4d7a31247c7fe0caac9754f3c291"
    hex2 = "9a4bd1491aa41e5402cc88c1b97eb32b"
    
    same, total = count_same_bits(hex1, hex2)
    percentage = (same / total) * 100
    
    print(f"MD5 - Same bits: {same}/{total} ({percentage:.2f}%)")
    
    hex3 = "ab30888291c4da9c09c111c2c55c3907543e05435935d0e7c18480f06a9e05ea"
    hex4 = "ce3720702c0d8a31a7b9b5013dbf79fe9a0b4e823ae4a135120adc4a9a40012e"
    
    same2, total2 = count_same_bits(hex3, hex4)
    percentage2 = (same2 / total2) * 100
    
    print(f"SHA256 - Same bits: {same2}/{total2} ({percentage2:.2f}%)")
