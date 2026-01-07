# 以下を「app.py」に書き込み
import streamlit as st
import pandas as pd
import time

# ---------- st.progress() ----------
pro_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    pro_bar.progress(i)  # ←ここにコードを追記

st.balloons()

# ---------- st.progress() ----------
st.  # ←ここにコードを追記
