
def reverse(text):
    rev = ''
    for i in range(len(text), 0, -1):
        rev += text[i-1]
    return rev

print reverse("abcd$3@c")
