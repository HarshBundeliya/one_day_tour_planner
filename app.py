import streamlit as st
import requests

st.title("One-Day Tour Planner")

# Collect user preferences via Streamlit form
city = st.text_input("City")
date = st.date_input("Date")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
budget = st.number_input("Budget", min_value=0)
interests = st.multiselect("Interests", ["culture", "adventure", "food", "shopping"])
starting_point = st.text_input("Starting Point (Hotel or Location)")

if st.button("Plan Tour"):
    user_preferences = {
        "city": city,
        "date": str(date),
        "start_time": str(start_time),
        "end_time": str(end_time),
        "budget": budget,
        "interests": interests,
        "starting_point": starting_point,
    }

    response = requests.post("http://127.0.0.1:8000/plan_tour/", json=user_preferences)
    itinerary = response.json()["itinerary"]
    weather = response.json()["weather"]

    # Display the itinerary and weather
    st.write("Weather Forecast:", weather)
    st.write("Your Itinerary:")
    for stop in itinerary:
        st.write(f"{stop['name']} ({stop['time']}), Entry Fee: ${stop['entry_fee']}")
