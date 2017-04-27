def mux_letters(inputstring, numberoftimes):
    xtra= ""
    for letter in inputstring:
        for count in range(numberoftimes):
            xtra= xtra + letter 
    return xtra
mux_letters("hi",3)
print(mux_letters("hi",3))
	



