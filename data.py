import pandas as pd

df = pd.read_csv("data.csv")

# Xuất bảng HTML có class để dễ style
html_table = df.to_html(index=False, classes="my-table", border=0)

# Ghi ra file riêng nếu muốn copy
with open("table.html", "w", encoding="utf-8") as f:
    f.write(html_table)
