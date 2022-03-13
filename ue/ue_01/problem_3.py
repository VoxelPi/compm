def replace_word(s_in, s_find, s_replace):
    words = s_in.split()
    s_out = ""
    for word in words:
        if word == s_find:
            s_out += " " + s_replace
        else:
            s_out += " " + word
    return s_out.strip()

def f(s: str, capitalize = False):
    words = s.split()
    if capitalize:
        out = []
        for word in words:
            out.append(word.capitalize())
        return out
    else:
        return words

print(replace_word("this test is a test", "test", "word"))
print(f("this test is a test"))
print(f("this test is a test", True))