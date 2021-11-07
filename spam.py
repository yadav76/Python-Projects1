text = input("Enter the text : ")
spam = False

if ("buy this to make money" in text):
    spam = True
elif ("subscribe these" in text):
    spam = True
else:
    spam = False

if (spam):
    print("This is spam")
else:
    print("This is not spam")
    