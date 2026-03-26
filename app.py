
import streamlit as st
import pandas as pd

st.title("SkillSync AI Dashboard")

df = pd.read_csv("data.csv")

st.sidebar.header("Filter")
exp = st.sidebar.slider("Experience", int(df.Experience.min()), int(df.Experience.max()), (0,10))

filtered = df[(df["Experience"] >= exp[0]) & (df["Experience"] <= exp[1])]

st.write("### Data Preview")
st.dataframe(filtered)

st.write("### Salary Distribution")
st.bar_chart(filtered["Salary"])

st.write("### Employability Count")
st.bar_chart(filtered["Employable"].value_counts())
