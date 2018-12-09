# 1
# 2
# 3
# 4
# 5
# Привіт
# це твої
# перші
# програми

input_str = 'Jessy'
length =24

if( len(input_str) % 2 == 0 and int(length) % 2 == 0):
  print( ('{0:/^'+str(length)+'}').format( input_str))
elif( len(input_str) % 2 == 0 and int(length) % 2 == 1):
  print( ('{0:+^'+str(1+length)+'}').format( input_str))
elif( len(input_str) % 2 == 1 and int(length) % 2 == 0):
  print( ('{0:=^'+str(1+length)+'}').format( input_str))
else:
  print( ('{0:$^'+str(length)+'}').format( input_str))

#
name = 'Julian'
length = 11
#Условие
length_1 = len(name) % 2 ==0 and int(length) % 2 == 0
length_2 = len(name) % 2 ==1 and int(length) % 2 == 1
length_3 = len(name) % 2 ==1 and int(length) % 2 == 0
# length_4 = len(name) % 2 ==0 and int(length) % 2 == 1

if length_1:
  print( ('{0:$^'+str(length)+'}').format( name))
elif length_2:
  print( ('{0:*^'+str(length)+'}').format( name))
elif length_3:
  print( ('{0:+^'+str(1+length)+'}').format( name))

else:
  print( ('{0:=^'+str(1+length)+'}').format( name))

#
name = 'Klara'
length = 14
#Условие name и length
length_1 = len(name) % 2 ==0 and int(length) % 2 == 0
length_2 = len(name) % 2 ==1 and int(length) % 2 == 1
length_3 = len(name) % 2 ==1 and int(length) % 2 == 0
length_4 = len(name) % 2 ==0 and int(length) % 2 == 1

#Условие  print
Print1 = ('{0:$^'+str(length)+'}').format( name)
Print2 = ('{0:*^'+str(length)+'}').format( name)
Print3 = ('{0:+^'+str(1+length)+'}').format( name)
Print4 = ('{0:=^'+str(1+length)+'}').format( name)

if length_1:
  print( Print1 )
elif length_2:
  print( Print2 )
elif length_3:
  print( Print3 )
else:
  print( Print4 )


#
name = 'Razor'
length = 10
#Условие name и length
length_1 = len(name) % 2 ==0 and int(length) % 2 == 0 or len(name) % 2 ==1 and int(length) % 2 == 1
length_2 = len(name) % 2 ==1 and int(length) % 2 == 0 or len(name) % 2 ==0 and int(length) % 2 == 1

#Условие  print
Print1 = ('{0:@^'+str(length)+'}').format( name)
Print2 = ('{0:@^'+str(1+length)+'}').format( name)

if length_1:
  print( Print1 )
else:
  print( Print2 )
