#REMOVE PASS AND FIX THIS FUNCTION
#
def palindrome(word):
    txt_forward = word.replace(' ', '').upper()
    txt_backward = word [::-1].replace(' ', '').upper()
    if txt_forward == txt_backward:
        if txt_forward == '':
            return False
        else:
            return True
    else:
        return False

#user_word = input()
#print(palindrome(user_word))