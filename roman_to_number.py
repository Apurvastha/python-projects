numbers_input = input("Enter a Roman numeral: ").upper()

def roman_to_int(numeral):
    final_answer = 0
    # Check for the special cases(IV, IX, XL, XC, CD, CM)
    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV", "")
        
    for i in numeral:
        if i == 'I':
            final_answer += 1
        elif i == 'V':
            final_answer += 5
        elif i == 'X':
            final_answer += 10
        elif i == 'L':
            final_answer += 50
        elif i == 'C':
            final_answer += 100
        elif i == 'D':
            final_answer += 500
        elif i == 'M':
            final_answer += 1000
        
    print(f"The Roman numeral {numeral} is equal to {final_answer}.")

roman_to_int(numbers_input)