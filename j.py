import streamlit as st
import pandas as pd
import random

a,b,c,d = st.columns(4)
k1 = a.text_input("keyword (optional)")
k2 = b.text_input("keyword  (optional)")
r = c.selectbox("Round",["Normal","Final","Either"])

def newQuestion(k1,k2,r):
    questions = pd.read_csv("JEOPARDY_CSV.csv")
    questions = questions[(questions["Category"].str.lower().str.contains(k1.lower())) | (questions["Question"].str.lower().str.contains(k1.lower()))]
    questions = questions[(questions["Category"].str.lower().str.contains(k2.lower())) | (questions["Question"].str.lower().str.contains(k2.lower()))]

    if r == "Normal":
        questions = questions[questions["Round"]!="Final Jeopardy!"]
    if r == "Final":
        questions = questions[questions["Round"]=="Final Jeopardy!"]
    l = len(questions)
    ra = random.randint(0,l-1)
    st.title(questions.iloc[ra]["Category"] + " | $" + questions.iloc[ra]["Value"])
    st.subheader(questions.iloc[ra]["Question"])
    try:
        st.session_state["last"] = st.session_state["current"]
    except:
        pass
    st.session_state["current"] = questions.iloc[ra]
    try:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.caption("Last Prompt: " + st.session_state["last"]["Category"] + " | " + st.session_state["last"]["Question"])
        st.write("Correct Response: " + st.session_state["last"]["Answer"])
    except:
        pass

if d.button("Run / Re-run"):
    newQuestion(k1,k2,r)