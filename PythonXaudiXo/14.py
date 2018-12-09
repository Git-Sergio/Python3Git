try:

  # eval('+-')

  print( 7 / 2 )
  # a


# except:
#   print('Pijmano shos')

# except (ZeroDivisionError, NameError, TypeError, ValueError, SyntaxError):

#   print('Pijmano odne z tsyh: ZeroDivisionError, NameError, TypeError, ValueError, SyntaxError ')

except ZeroDivisionError:
  print('Pijmano ZeroDivisionError')
except SyntaxError:
  print('Pijmano SyntaxError несущесвующа перемінна')
except NameError:
  print('Pijmano NameError несущесвующа перемінна')
except TypeError:
  print('Pijmano TypeError')
except ValueError:
  print('Pijmano ValueError')

finally:
  print('kinets poimki')

print('Kinets programy')
