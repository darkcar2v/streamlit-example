from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import datetime

""" # CLASSIC FITNESS CENTER ANALYTICS BOARD """

d = st.date_input("Select the date to display the report", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
