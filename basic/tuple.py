import datetime

def get_today():
  today = datetime.datetime.today()
  value = (today.year, today.month, today.day) # () がタプル宣言
  return value

test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])
# print(test_tuple[3])
# IndexError: tuple index out of range
