# コードスタイル
# import　の順番
# 1. 標準ライブラリ
# 2. サードパーティライブラリ
# 3. 自作ライブラリ
# 4. ローカルライブラリ
# アルファベット順に並べる
# 各ライブラリ毎に1行空ける
# ライブラリのインポートは1行に1つ



# import lesson_package.utils
from lesson_package import utils

# print(lesson_package.utils.say_hello('Mike')) # hello Mike
r = utils.say_hello('Mike')
print(r) # hello Mike
