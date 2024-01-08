letter = input("Nhập chữ cái: ")
if letter in ('u', 'e', 'o', 'a', 'i'):
    print("%s là nguyên âm" % letter)
elif letter == 'y':
    print("Y có thể là nguyên âm hoặc phụ âm")
else:
    print("%s là phụ âm" % letter)