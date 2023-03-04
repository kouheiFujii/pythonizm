import time

def measure_time(func):
    print(f"測定対象の関数: {func.__name__}")
    def wrapper(*args, **kwargs):
        print("wrapper関数を実行します")
        print("引数に渡された値: ", args, kwargs)
        print("測定を開始します")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("測定を終了します")
        print(f"実行時間: {end_time - start_time}秒")
        return result
    return wrapper # wrapper関数を返す

# @measure_timeの関数を呼び出す
# 直下にある関数を引数に渡す
# measure_time(long_running_function)と同じ
@measure_time
def long_running_function():
    print("long_running_functionを実行します")
    time.sleep(2)

long_running_function()

print("-----")

@measure_time
def short_running_function():
    print("short_running_functionを実行します")
    time.sleep(0.5)

short_running_function()

print("-----")

@measure_time
def add(a, b):
    print("addを実行します")
    return a + b

add(1, 2)
