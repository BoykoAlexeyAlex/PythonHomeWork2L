number=int(input('Введите целое трехзначное число '))
lastnumber = number//100
firstnumber = number%10
secondnumber = number%100-firstnumber
print('Перевернутое число :',firstnumber*100+secondnumber+lastnumber)
print('Спасибо')
