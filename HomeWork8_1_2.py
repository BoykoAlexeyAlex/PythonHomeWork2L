grossbukh1 = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

def order_summ(grossbukh1):
    l1= list(map(lambda x: tuple((str(x[0]) +' '+ str(round(x[2] * x[3])
	    if x[2] * x[3] >= 100 else round(x[2] * x[3] + 10))).split()),grossbukh1))
    return l1

print(order_summ(grossbukh1))