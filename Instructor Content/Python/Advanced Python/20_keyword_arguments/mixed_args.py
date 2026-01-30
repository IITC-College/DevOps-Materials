#!/usr/bin/env python3
# Mixing positional and keyword arguments

def book_flight(passenger, destination, flight_class, meal_pref):
    print(f"Passenger: {passenger}")
    print(f"Destination: {destination}")
    print(f"Class: {flight_class}")
    print(f"Meal: {meal_pref}")
    print("---")

# First two positional, rest keyword
book_flight("Alice", "London", flight_class="Business", meal_pref="Vegetarian")

# Only first positional, rest keyword
book_flight("Bob", destination="Paris", flight_class="Economy", meal_pref="None")

# Positional arguments must come before keyword arguments
