grossbukh1 = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def order_summ(grossbukh):
	res = list(dict(zip(list(map(lambda x: x[0], grossbukh)), list(
		map(lambda x: round(x[2] * x[3]) if x[2] * x[3] >= 100 else round(x[2] * x[3] + 10), grossbukh)))).items())
	return res


print(order_summ(grossbukh1))



