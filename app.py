from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, validator
from typing import List
import datetime

# Assuming agents are correctly defined in their respective modules
from .memory import MemoryAgent
from .itinerary import ItineraryAgent
from .weather import WeatherAgent
from .optimization import OptimizationAgent

app = FastAPI()

# Initialize the agents
memory_agent = MemoryAgent()
itinerary_agent = ItineraryAgent(memory_agent)
weather_agent = WeatherAgent()
optimization_agent = OptimizationAgent()

# Define the user preference input schema
class TourDetails(BaseModel):
    location: str
    start_date: str
    end_date: str
    num_people: int
    interests: List[str] = []  # Historical sites, museums, etc.
    budget: float = 100.0  # Default budget for the tour

    @validator('start_date', 'end_date')
    def validate_date_format(cls, value):
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date format should be YYYY-MM-DD")
        return value

    @validator('num_people')
    def validate_num_people(cls, value):
        if value <= 0:
            raise ValueError("Number of people should be greater than 0")
        return value

    @validator('budget')
    def validate_budget(cls, value):
        if value <= 0:
            raise ValueError("Budget should be greater than 0")
        return value


@app.get("/")
def read_root():
    return HTMLResponse("""
        <html>
            <body>
                <h1>Plan Your Tour</h1>
                <form action="/plan_tour_form/" method="post">
                    Location: <input type="text" name="location"><br>
                    Start Date (YYYY-MM-DD): <input type="text" name="start_date"><br>
                    End Date (YYYY-MM-DD): <input type="text" name="end_date"><br>
                    Number of People: <input type="number" name="num_people"><br>
                    Interests (comma separated): <input type="text" name="interests"><br>
                    Budget: <input type="number" name="budget" value="100.0"><br>
                    <input type="submit" value="Plan Tour">
                </form>
            </body>
        </html>
    """)


@app.post("/plan_tour_form/")
async def plan_tour_form(
    location: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    num_people: int = Form(...),
    interests: str = Form(""),
    budget: float = Form(100.0),
):
    # Print inputs for debugging
    print(f"Received input - Location: {location}, Start Date: {start_date}, End Date: {end_date}, "
          f"Number of People: {num_people}, Interests: {interests}, Budget: {budget}")
    
    # Parse interests into a list
    interests_list = [interest.strip() for interest in interests.split(",")]

    try:
        # Create the TourDetails object with validation
        tour_details = TourDetails(
            location=location,
            start_date=start_date,
            end_date=end_date,
            num_people=num_people,
            interests=interests_list,
            budget=budget
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Step 1: Save the user preferences to memory
    memory_agent.save_user_preferences(tour_details)

    # Step 2: Generate an initial itinerary based on the interests
    itinerary = itinerary_agent.generate_itinerary(tour_details)

    # Step 3: Fetch weather and adjust itinerary if necessary
    try:
        weather = weather_agent.get_weather(tour_details.location, tour_details.start_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Weather service error: {str(e)}")

    itinerary = optimization_agent.adjust_itinerary_based_on_weather(itinerary, weather)

    # Step 4: Optimize travel paths based on the budget
    optimized_itinerary = optimization_agent.optimize_itinerary(itinerary, tour_details.budget)

    # Step 5: Generate an interactive map (this can be an external service like Google Maps API)
    # For now, we'll simulate it with a placeholder
    map_link = "https://www.google.com/maps/d/u/0/viewer?mid=1h_2gkJ7PpNR9vHk_i3xoFqfJsoB8o_cX"

    # Return the optimized itinerary, weather, and other details in an HTML format
    return HTMLResponse(f"""
        <html>
            <body>
                <h1>Tour Planned Successfully!</h1>
                <p><strong>Location:</strong> {tour_details.location}</p>
                <p><strong>Start Date:</strong> {tour_details.start_date}</p>
                <p><strong>End Date:</strong> {tour_details.end_date}</p>
                <p><strong>Number of People:</strong> {tour_details.num_people}</p>
                <p><strong>Interests:</strong> {', '.join(tour_details.interests)}</p>
                <p><strong>Budget:</strong> €{tour_details.budget}</p>
                <h3>Itinerary:</h3>
                <ul>
                    {"".join([f"<li>{item}</li>" for item in itinerary])}
                </ul>
                <h3>Weather Forecast:</h3>
                <p>{weather}</p>
                <h3>Optimized Travel Paths:</h3>
                <p>{optimized_itinerary}</p>
                <h3>Interactive Map:</h3>
                <p><a href="{map_link}" target="_blank">Click here to view your itinerary on the map</a></p>
            </body>
        </html>
    """)

# Classes for agents (as per your previous code)

class OptimizationAgent:
    def adjust_itinerary_based_on_weather(self, itinerary, weather):
        if weather == "rainy":
            for stop in itinerary:
                if stop["type"] == "outdoor":
                    stop["status"] = "indoor"
        return itinerary

    def optimize_itinerary(self, itinerary, budget):
        optimized_itinerary = []
        remaining_budget = budget
        for stop in itinerary:
            if remaining_budget >= stop["entry_fee"]:
                optimized_itinerary.append(stop)
                remaining_budget -= stop["entry_fee"]
        return optimized_itinerary


class MemoryAgent:
    def save_user_preferences(self, tour_details):
        # Code to save the user's preferences (e.g., to a database or file)
        print(f"Saved user preferences: {tour_details.dict()}")

class ItineraryAgent:
    def __init__(self, memory_agent):
        self.memory_agent = memory_agent
    
    def generate_itinerary(self, tour_details):
        # Generate a basic itinerary based on user preferences
        return [
            {"name": "Museum of Art", "type": "indoor", "entry_fee": 20},
            {"name": "Botanical Garden", "type": "outdoor", "entry_fee": 15},
            {"name": "City Tour", "type": "outdoor", "entry_fee": 30}
        ]


class WeatherAgent:
    def get_weather(self, location, date):
        # Mock weather service (you can replace this with actual weather API calls)
        if "rain" in location.lower():
            return "rainy"
        return "sunny"
