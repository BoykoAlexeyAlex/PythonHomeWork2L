s='aafffsssahhhhhrrhhrrrhherrrttt'
s1 = s[:s.find('h')+1]
s2 = s[s.rfind('h'):len(s)]
s3 = s[s.find('h'):s.rfind('h')]
s3= s3.replace('h','H')
s=s1+s3+s2
print(s)