One-Day Tour Planner
This project is a FastAPI-based backend application designed to help users plan optimized one-day tours based on their location, interests, budget, and the weather. The application generates an itinerary, adjusts stops based on weather conditions, and optimizes the plan to fit within a specified budget.

Features
User Preferences: Users can specify a location, date, number of people, interests, and budget.
Weather-Based Adjustments: Outdoor stops are adjusted to indoor alternatives if the weather forecast is unfavorable.
Budget Optimization: The itinerary is tailored to fit within the user’s budget.
Interactive Map: The itinerary includes a link to an interactive map of the planned tour.
Project Structure
The application includes the following key components:

Agents:
MemoryAgent: Saves user preferences.
ItineraryAgent: Generates a basic itinerary based on user input.
WeatherAgent: Fetches weather information (mocked in this example).
OptimizationAgent: Optimizes the itinerary based on budget and weather.
Setup
Prerequisites
Python 3.8+
FastAPI
Uvicorn
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/one_day_tour_planner.git
cd one_day_tour_planner
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Start the FastAPI server:

bash
Copy code
uvicorn app:app --reload
Access the application at http://127.0.0.1:8000 in your web browser.

Files
app.py: Contains the FastAPI application logic and routes.
agents/: Contains the agent classes (MemoryAgent, ItineraryAgent, WeatherAgent, OptimizationAgent).
Usage
Open http://127.0.0.1:8000 in your browser.
Fill out the form with your tour preferences (location, dates, number of people, interests, and budget).
Submit the form to generate an optimized itinerary.
The response page will display:
Location, date, people, and budget details.
A weather forecast for the location.
An optimized itinerary with cost adjustments.
A link to view the itinerary on an interactive map.
Example Itinerary
Input:
Location: Paris
Date: 2024-11-12
People: 2
Interests: Museums, Outdoor, Historic Sites
Budget: 100
Output:
Itinerary:
Museum of Art: Indoor, Entry Fee: 20
Botanical Garden: Outdoor, Entry Fee: 15 (adjusted based on weather if rainy)
City Tour: Outdoor, Entry Fee: 30
Agents
MemoryAgent
Stores user preferences for future reference.

ItineraryAgent
Generates a list of stops based on the user’s interests.

WeatherAgent
Simulates weather data; you may replace this with a real weather API.

OptimizationAgent
Adjusts and optimizes the itinerary based on weather conditions and available budget.