"""
Move the first letter of each word to the end of it,
then add 'ay' to the end of the word.
- pig_it('Pig latin is cool') # igPay atinlay siay oolcay

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
"""

def pig_it(text):
    """
    move 1st letter of each word to the back and add 'ay'
    """
    ret_val = ""
    tmp = text.split()
    for word in tmp:
        ret_val += word[1:]+word[0]
        if word.isalpha():
            ret_val += "ay "
        else:
            ret_val += " "
    return ret_val.rstrip()

def main():
    """
    testing
    """
    print(pig_it("Pig latin is cool"))
    print(pig_it("This is my string !"))

if __name__ == '__main__':
    main()
