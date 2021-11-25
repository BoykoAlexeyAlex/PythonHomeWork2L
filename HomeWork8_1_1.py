grossbukh1 = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

def order_summ(grossbukh1):
    for j in grossbukh1:
        j[3] = round(j[3]*j[2]) if j[3]*j[2]>=100 else round(j[2]*j[3]+10)
    l1= list(map(lambda x: tuple(x[::3]),grossbukh1))
    return l1

print(order_summ(grossbukh1))

