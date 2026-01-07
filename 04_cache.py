import streamlit as st
import pandas as pd
import time

# ---------- キャッシュによる時間短縮 ----------
st.title("@st.cache")

@st.cache  # ←この表記の下の関数がキャッシュされる
def my_heavy_func(a, b):
    c = 0
    for i in range(10000000):  # 意味の無い重い処理
        c = c + a - b
        c = c - a + b
    return c

if st.button("時間を計測"):
    start_time = time.time()  # 開始時刻
    my_heavy_func(1, 1)
    st.write("所要時間: " + str(time.time() - start_time))
