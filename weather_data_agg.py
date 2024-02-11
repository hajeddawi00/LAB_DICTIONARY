weather_data:dict = {}

def input_data ():
    '''this function for getting inputs from user and store it in nested dictionary'''
    city:str = input('Please enter the city name: ')
    date:str = input('Please enter a date ( DD - MM - YYYY): ')
    temperature:int = int(input('Please enter the temperature (°C): '))
    humidity:str = int(input('Please enter the humidity (%): '))
    weather_condition:str = input('Please enter the weather condition (e.g., sunny, rainy): ')

    weather_data[city] = {
        'date':date,
        'temperature':temperature,
        'humidity':humidity,
        'weather_condition':weather_condition
    }

def query_by_city():
    city_name = input('Please enter city name: ')
    if city_name in weather_data:
        for key, value in weather_data[city_name].items():
            print(f"{key}: {value}")
    else:
        print("City not found in the data.")
        


while True:
    print("\n1. Input Weather Data\n2. Query by City\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        input_data()
    elif choice == 2:
        query_by_city()
    elif choice == 3:
        print('Exiting from the program...')
        break
    else:
        print('Enter a valid number: ')

        
