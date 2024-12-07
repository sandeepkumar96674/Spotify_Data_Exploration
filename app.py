import streamlit as st
import pandas as pd
import numpy as np

# Configuration of the Page
st.set_page_config(
    page_title="Spotify Data Insight",
    page_icon="🔍"
)

st.title(":green[Spotify]")
st.subheader("Exploring the Spotify Data using SQL")

st.caption("Created by :red[Sandeep] ✨")

tab1,tab2,tab3,tab4,tab5=st.tabs(['Summary','Top and Bottom Rows','Data Types','Columns','Null Values'])
