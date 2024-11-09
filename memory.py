import json

class MemoryAgent:
    def __init__(self):
        self.user_data = {}

    def save_user_preferences(self, preferences):
        user_id = preferences.location + preferences.start_date


        self.user_data[user_id] = preferences.dict()

    def get_user_preferences(self, user_id):
        return self.user_data.get(user_id, {})
