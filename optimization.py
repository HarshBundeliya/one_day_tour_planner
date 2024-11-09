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
