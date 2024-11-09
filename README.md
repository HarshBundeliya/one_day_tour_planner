One-Day Tour Planner 🌍
A FastAPI-based application to plan customized, optimized one-day tours based on user preferences, budget, and weather conditions.

🚀 Features
Personalized Itinerary Generation: Create an itinerary based on location, number of people, interests, and budget.
Weather-Based Adjustments: Automatically adjusts itinerary stops based on weather forecasts.
Budget Optimization: Ensures the tour fits within the specified budget by selecting stops that meet cost constraints.
Interactive Map Link: Provides a link to view the optimized itinerary on an interactive map.
🏗️ Project Structure
app.py: The main application with FastAPI routes for the tour planning process.
Agents:
MemoryAgent: Stores user preferences.
ItineraryAgent: Generates a basic itinerary based on user input.
WeatherAgent: Fetches or simulates weather information.
OptimizationAgent: Optimizes the itinerary based on budget and weather.
🛠️ Setup
Prerequisites
Python 3.8+
FastAPI
Uvicorn (ASGI server)
Installation
Clone the repository:

bash
git clone https://github.com/your-username/one_day_tour_planner.git
cd one_day_tour_planner
Install dependencies:

bash
pip install -r requirements.txt
Start the FastAPI server:

bash
uvicorn app:app --reload
Access the application at http://127.0.0.1:8000 in your web browser.

💻 Usage
Open http://127.0.0.1:8000 in your browser.
Fill out the form with your tour preferences, including location, start and end dates, number of people, interests, and budget.
Submit the form to generate an optimized itinerary.
The response page will display:
Tour details: Location, dates, number of people, interests, and budget.
Weather forecast for the location.
An optimized itinerary with adjustments based on the budget and weather.
A link to view the itinerary on an interactive map.
🧩 Agents
MemoryAgent: Saves user preferences for future reference.
ItineraryAgent: Creates an itinerary based on the user’s preferences and interests.
WeatherAgent: Provides weather information, allowing adjustments to the itinerary.
OptimizationAgent: Ensures the itinerary fits within the user’s budget, adjusting stops as necessary.
📄 Example Workflow
Input:
Location: Paris
Start Date: 2024-11-12
End Date: 2024-11-12
People: 2
Interests: Museums, Outdoor, Historic Sites
Budget: €100
Output:
Itinerary:
Museum of Art: Indoor, Entry Fee: €20
Botanical Garden: Outdoor, Entry Fee: €15 (adjusted if rainy)
City Tour: Outdoor, Entry Fee: €30
🔗 Interactive Map
A generated itinerary includes a link to view the tour route on an interactive map for easier navigation.
