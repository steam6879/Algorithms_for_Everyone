def palindrome(s):   #string s
    qu = []
    st = []
    for x in s:
        if x.isalpha(): #주어진 문자가 알파벳 문자인지 확인
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True

print(palindrome("wow"))
print(palindrome("wke"))
print(palindrome("Madam, I'm Adam."))
