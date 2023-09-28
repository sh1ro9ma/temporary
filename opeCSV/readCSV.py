import pandas as pd

FILE_PATH = "./sample.csv"

print(pd.__version__)

# CSVファイル読み込み
df = pd.read_csv(FILE_PATH)
print(df)

# 単純出力
print(df.columns)

# 情報出力
df.info()

# サイズ出力
print(df.shape)

row, col = df.shape
print(f"{row=},{col=}")

# ヘッダー行を追加して出力
df = pd.read_csv(FILE_PATH, names=['A', 'B', 'C', 'D'])
print(df)

# ヘッダー行を置き換えて出力
df = pd.read_csv(FILE_PATH, header=0, names=['A', 'B', 'C', 'D'])
print(df)

# 列名を出力
df = pd.read_csv(FILE_PATH, na_filter=False)
for colName in df.columns:
    print(colName)

# 列名を削除
skiprows_a = ["Test", "AAA"]

print(df.drop(skiprows_a, axis=1))
