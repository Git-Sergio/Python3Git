key = {
  1 : 5,
  2 : {
    21 : 55,
    22 : 75,
    23 : 99
    },
}

vvid = input('Vvedit kluch:')

if int(vvid) in key:
  print('Takuy kluch je int!  ' + vvid)
# elif int(vvid) in key:
#   print('Takuy kluch je int!  ' + vvid)
else:
  print('Takogo klucha nemaje!  ' + vvid)

