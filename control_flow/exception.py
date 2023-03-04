# 例外処理
l = [1, 2, 3, 4, 5]
try:
    l[10] # IndexError: list index out of range
except IndexError as e:
    print('IndexError: {}'.format(e)) # IndexError: list index out of range

print('--------')

# NameError
try:
  a
except NameError as e:
  print('NameError: {}'.format(e)) # NameError: name 'a' is not defined

print('--------')

# multiple exceptions
try:
  # l[10]
  a
except (IndexError, NameError) as e:
  print('Error: {}'.format(e))

print('--------')

# else
try:
  l[0]
except IndexError as e:
  print('IndexError: {}'.format(e))
except NameError as e:
  print('NameError: {}'.format(e))
else:
  # tryの中でエラーがなかった場合に実行される
  print('No errors')

print('--------')

# finally
try:
  l[0]
except IndexError as e:
  print('IndexError: {}'.format(e))
finally:
  # 例外が発生してもしなくても実行される
  print('Finally')
