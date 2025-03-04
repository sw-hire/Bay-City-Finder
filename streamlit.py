from os import access

import streamlit as st
from filternew import findcity

st.title("Bay Area City Finder 🌉")

st.markdown("Welcome to the Bay Area City Finder!"
            " Picking the right place to live in the Bay Area is tough—prices are high, commutes are long, and every city is different. This tool makes it easier!"
            " Just enter your budget, commute preferences, and what matters most to you. "
            "We’ll match you with a city that fits your needs.")

st.text("Alright, let's get started!")

meetsCondition = True

budget = st.number_input("What is your budget for a home ($)?")
if budget < 453000.00 and budget > 0:
    meetsCondition = False
    st.error("Sorry! Median house prices as of 2021 start at 453000."
            " Please enter a value at or above 453000.")

mode = st.selectbox("How do you prefer to commute?",
             ("", "Transit", "Carpool", "Drive Alone", "Bicycle", "Walk", "Work From Home"))

time = st.number_input("What is your ideal commute time?")
if time < 17.34 and time > 0:
    meetsCondition = False
    st.error("Sorry! Average commute times as of 2018 start at 17.34 minutes. Please enter a value at or above 17.34.")
st.text("In order of importance, please rank your top 2 among your budget, mode of commute, and ideal commute time.")
pref1 = st.selectbox("First Ranking:",
                    ("", "Budget", "Mode", "Commute Time"))
pref2 = st.selectbox("Second Ranking:",
                    ("", "Budget", "Mode", "Commute Time"))
if pref1 == "" or pref2 == "":
    meetsCondition = False
    st.error("Please select a Budget, Mode, or Commute Time.")

if pref1 == pref2:
    meetsCondition = False
    st.error("Please select a different second ranking from your first choice.")

if st.button("Find My Cities") and meetsCondition:
    result = findcity(budget, mode, time, pref1, pref2)

    if result.empty:
        st.error("Sorry! Looks like very few cities found that match your criteria. Try adjusting your mode!")
    else:
        st.dataframe(result, use_container_width=True)