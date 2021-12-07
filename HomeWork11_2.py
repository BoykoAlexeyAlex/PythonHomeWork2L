from pprint import pprint

dict1 = dict([tuple([_,chr(_)]) for _ in range(32,128)])

pprint(dict1)