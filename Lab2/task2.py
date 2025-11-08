import string

# English letter frequencies (more accurate order)
english_freq = "eotainshrdlcufwmpygbkqvjxz"

def frequency_analysis(text):
    """Perform frequency analysis on text"""
    freq = {}
    total_letters = 0
    
    for c in text.lower():
        if c in string.ascii_lowercase:
            freq[c] = freq.get(c, 0) + 1
            total_letters += 1
    
    # Convert to percentages and sort
    freq_percent = {char: (count/total_letters)*100 for char, count in freq.items()}
    sorted_freq = sorted(freq_percent.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_freq

def apply_mapping(text, mapping):
    """Apply character mapping to text"""
    result = []
    for c in text:
        if c.lower() in mapping:
            # Preserve case
            if c.isupper():
                result.append(mapping[c.lower()].upper())
            else:
                result.append(mapping[c.lower()])
        else:
            result.append(c)
    return ''.join(result)

def display_frequency_comparison(cipher_freq):
    """Display comparison between cipher and English frequencies"""
    print("\nFrequency Analysis:")
    print("Cipher | English | Frequency (%)")
    print("-" * 35)
    
    for i, (char, freq) in enumerate(cipher_freq):
        eng_char = english_freq[i] if i < len(english_freq) else '?'
        print(f"  {char}    |    {eng_char}    |   {freq:.2f}")

def main():
    cipher = (
        "af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao"
        "--wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg"
        "du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm"
        "epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc"
        "--pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi"
        "mddg oafg cepc tdvng qdfcafvi cei kiripkqe"
    )
   


    print("Original ciphertext:\n")
    print(cipher)

    # Frequency analysis
    cipher_freq = frequency_analysis(cipher)
   

    # Create initial mapping
    initial_mapping = {}
    for i, (char, _) in enumerate(cipher_freq):
        if i < len(english_freq):
            initial_mapping[char] = english_freq[i]

    
    for k, v in sorted(initial_mapping.items()):
        f"{k} -> {v}"

    # Apply mapping
    initial_decrypt = apply_mapping(cipher, initial_mapping)
    print("\nInitial decryption:\n")
    print(initial_decrypt)


if __name__ == "__main__":
    main()
