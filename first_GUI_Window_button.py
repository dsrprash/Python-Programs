import TKinter
import random
master = TK()

def rollDice() :
	print (random.randint(1,6))
b = Button(master,text="Roll",command=rollDice)
b.pack()

mainloop()
