def shortcut( s ):
    newstr = s
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in s.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")
    return newstr
