import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv("SkillSync_AI_Candidates.csv")

# -----------------------
# AUTO DETECT COLUMNS
# -----------------------
columns = df.columns

salary_col = [col for col in columns if "salary" in col.lower()][0]
skills_col = [col for col in columns if "skill" in col.lower()][0]
exp_col = [col for col in columns if "exp" in col.lower()][0]
emp_col = [col for col in columns if "employ" in col.lower()][0]

# -----------------------
# FIX EMPLOYABILITY COLUMN
# -----------------------
emp_numeric = pd.to_numeric(df[emp_col], errors='coerce')

if emp_numeric.isnull().all():
    emp_numeric = df[emp_col].map({
        "Yes": 1, "No": 0,
        "High": 1, "Low": 0,
        "Employable": 1, "Not Employable": 0
    })

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("SkillSync AI")
page = st.sidebar.radio("Navigate", [
    "Overview",
    "Descriptive Analytics",
    "Diagnostic Analytics",
    "Predictive Analytics",
    "Prescriptive Analytics"
])

# -----------------------
# OVERVIEW
# -----------------------
if page == "Overview":
    st.title("⚡ SkillSync AI Dashboard")

    st.markdown("### Business Objective")
    st.write("Analyze skills, predict employability, and recommend career improvements.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Salary", int(df[salary_col].mean()))
    col2.metric("Avg Skills", round(df[skills_col].mean(), 1))
    col3.metric("Employability %", round(emp_numeric.mean()*100, 1))


# -----------------------
# DESCRIPTIVE
# -----------------------
elif page == "Descriptive Analytics":
    st.title("📊 Descriptive Analytics")

    st.subheader("Salary Distribution")
    fig = px.histogram(df, x=salary_col, nbins=20)
    st.plotly_chart(fig)

    st.subheader("Skills Distribution")
    fig2 = px.histogram(df, x=skills_col)
    st.plotly_chart(fig2)

    st.subheader("Employability Count")
    fig3 = px.bar(emp_numeric.value_counts())
    st.plotly_chart(fig3)


# -----------------------
# DIAGNOSTIC
# -----------------------
elif page == "Diagnostic Analytics":
    st.title("🔍 Diagnostic Analytics")

    st.subheader("Salary vs Experience")
    fig = px.scatter(df, x=exp_col, y=salary_col)
    st.plotly_chart(fig)

    st.subheader("Skills vs Salary")
    fig2 = px.scatter(df, x=skills_col, y=salary_col)
    st.plotly_chart(fig2)

    st.info("Insight: Higher skills and experience → higher salary.")


# -----------------------
# PREDICTIVE
# -----------------------
elif page == "Predictive Analytics":
File "/mount/src/starter/app.py", line 129
      X_train, X_test, y_train_c, y_test_c = train_test_split(X, y_class, test_size=0.2, random_state=42)
     ^
IndentationError: unexpected indent


# -----------------------
# PRESCRIPTIVE
# -----------------------
elif page == "Prescriptive Analytics":
    st.title("🎯 Prescriptive Analytics")

    skills = st.slider("Your Current Skills", 1, 10, 3)

    if skills < 4:
        st.warning("Recommendation: Learn Python, SQL")
    elif skills < 7:
        st.info("Recommendation: Learn Machine Learning, APIs")
    else:
        st.success("You are highly skilled! Focus on specialization.")

    add_skill = st.checkbox("Add 1 Skill")

    base_salary = int(df[salary_col].mean() + skills * 2000)

    if add_skill:
        new_salary = base_salary + 3000
        st.write(f"New Salary: ₹{new_salary}")
    else:
        st.write(f"Current Salary: ₹{base_salary}")
