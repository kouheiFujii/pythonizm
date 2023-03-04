# 辞書内包表記
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
drinks = ['coffee', 'tea', 'beer', 'wine', 'water', 'juice', 'soda']
menu = {}
for day, drink in zip(days, drinks):
    menu[day] = drink
print(menu) # {'Mon': 'coffee', 'Tue': 'tea', 'Wed': 'beer', 'Thu': 'wine', 'Fri': 'water', 'Sat': 'juice', 'Sun': 'soda'}
# ワンライナーで書ける
menu = {day: drink for day, drink in zip(days, drinks)}
print(menu) # {'Mon': 'coffee', 'Tue': 'tea', 'Wed': 'beer', 'Thu': 'wine', 'Fri': 'water', 'Sat': 'juice', 'Sun': 'soda'}
