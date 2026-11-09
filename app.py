"""A股短期趋势监控（本地网页）。启动：streamlit run app.py
两个页面：「指数分析」(views/dashboard.py) 与「数据」(views/data.py，所有下载/上传/自动更新都在这里)。"""
import streamlit as st

st.set_page_config(page_title="A股短期趋势监控", layout="wide")
st.session_state.setdefault("rev", 0)

import common  # noqa: E402  (必须在 set_page_config 之后导入)

pg = st.navigation([
    st.Page("views/dashboard.py", title="指数分析", icon="📈", default=True),
    st.Page("views/data.py", title="数据", icon="🗄️"),
])
common.auto_update_watcher()      # 页面开着时每 5 分钟检查；交易日收盘后核心数据落后就自动更新
pg.run()
