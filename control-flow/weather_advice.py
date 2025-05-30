weather_day = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather_day == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_day == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_day == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
