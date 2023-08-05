from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import datetime

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

d = st.date_input("Select the date to display the report", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
