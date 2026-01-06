import streamlit as st
import numpy as np
import pandas as pd

# ---------- 変数の記述による表示（magic command） ----------
st.title("Magic command")
df = pd.DataFrame({
    "col1": [11, 12, 13, 14],
    "col2": [111, 112, 113, 114]
})
df

# ---------- st.write()　は万能の働き ----------
st.title("st.write()")
st.write("st.write()を使ってみましょう！")
st.write(pd.DataFrame({
    "col1": [11, 12, 13, 14],
    "col2": [111, 112, 113, 114]
}))

# ---------- st.dataframe()　はインタラクティブな表の描画 ----------
st.title("st.dataframe()")
dataframe = pd.DataFrame(
    np.random.randn(8, 8),
    columns=("col"+str(i) for i in range(8)))
st.dataframe(dataframe.style.highlight_max(axis=0))

# ---------- st.table()　は静的な表の描画 ----------
st.title("st.table()")
dataframe = pd.DataFrame(
    np.random.randn(8, 8),
    columns=("col"+str(i) for i in range(8)))
st.table(dataframe)

# ---------- st.line_chart()は折れ線グラフの描画 ----------
st.title("st.line_chart()")
chart = pd.DataFrame(
    np.random.randn(16, 4),
    columns=("line"+str(i) for i in range(4)))
st.line_chart(chart)

# ---------- st.map()は地図の描画 ----------
st.title("st.map()")
map = pd.DataFrame(
    [35.658584, 139.7454316] + np.random.randn(100, 2)/100,  # 東京タワー周辺の緯度、経度
    columns=["lat", "lon"])
st.map(map)

# ---------- st.latex()は数式の描画 ----------
st.title("st.latex()")
st.latex(r"""
E  = \frac{1}{2}\sum_{j=1}^m \Bigl(\sum_{k=0}^n a_kx_j^k - t_j\Bigr)^2
     """)  # 「r」を付けてraw文字列に
