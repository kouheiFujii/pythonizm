import os
import pathlib
import shutil
import glob

# ファイルの作成
pathlib.Path('file/test.txt').touch()

# ファイルか確認
print(os.path.isfile('file/test.txt'))
# ディレクトリか確認
print(os.path.isdir('file/test.txt'))
# ファイルが存在するか確認
print(os.path.exists('file/test.txt'))
# ファイルの拡張子を取得
print(os.path.splitext('file/test.txt'))
# ファイルの名前を取得
print(os.path.basename('file/test.txt'))
# ファイルの名前を変更
os.rename('file/test.txt', 'file/test2.txt')
# symlinkを作成
os.symlink('file/test2.txt', 'file/test3.txt')
# ディレクトリの作成
os.mkdir('file/test_dir')
# ディレクトリの削除
os.rmdir('file/test_dir')

# ネストしたディレクトリを作成して中身を表示する
os.makedirs('file/test_dir/test_dir2')
pathlib.Path('file/test_dir/test_dir2/test.txt').touch()
# ファイルをコピー
shutil.copy('file/test_dir/test_dir2/test.txt', 'file/test_dir/test_dir2/test2.txt')
print(glob.glob('file/test_dir/test_dir2/*'))

# ディレクトリを強制削除
shutil.rmtree('file/test_dir')
