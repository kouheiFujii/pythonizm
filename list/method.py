l = [1, 3, 5, 2, 1, 5, 9, 8]
print(l.index(9)) # 存在する場合インデックスを返す

print(l.count(5)) # 引数に存在する数をカウント

l.sort() # 昇順
print(l)
l.sort(reverse=True) # 降順
print(l)
l.reverse() # 現在の並び順の逆
print(l)

s = "My name is Jon."

to_split = s.split(" ") # 存在する文字を検知する。ここでは空白を指定している
print(to_split)

x = " =========== ".join(to_split) # リストを =========== で結合する
print(x)
