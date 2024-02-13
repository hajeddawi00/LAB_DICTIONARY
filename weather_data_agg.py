weather_data:dict = {}

def input_data (city):
    '''this function for getting inputs from user and store it in nested dictionary'''
    date:str = input('Please enter a date ( DD - MM - YYYY): ')
    temperature:int = int(input('Please enter the temperature (°C): '))
    humidity:str = int(input('Please enter the humidity (%): '))
    weather_condition:str = input('Please enter the weather condition (e.g., sunny, rainy): ')

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city] [date]= {
        'temperature':temperature,
        'humidity':humidity,
        'weather_condition':weather_condition
    }
    input('')

def query_weather_data(city:str):
    
    if city in weather_data:
        city_data = weather_data[city]
        for date in city_data:
            print(f"weather for {city} on {date}: ")
            print(f"Temperature: {city_data[date]['temperature']} °C")
            print(f"Humdity: {city_data[date]['humidity']} %")
            print(f"Condition: {city_data[date]['weather_condition']}")
            input("")

    else:
        print("No weather data for this city!")

while True:
    try:
        while True:
            print("\n1. Input Weather Data\n2. Query by City\n3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                city = input('Please Enter The City Name: ')
                input_data(city)
            elif choice == 2:
                city = input('Please Enter The City Name: ')
                query_weather_data(city)
            elif choice == 3:
                print('Exiting from the program...')
                break
            else:
                print('Enter a valid number: ')
    except ValueError:
        print('You enter a wrong inputs. Try again')
        
