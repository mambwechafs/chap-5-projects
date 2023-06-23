import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'your_api_key'  # Replace with your OpenWeatherMap API key

def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        messagebox.showinfo('Weather Forecast', f'City: {city}\nTemperature: {temperature} K\nHumidity: {humidity}%\nDescription: {description}')
    except requests.exceptions.RequestException:
        messagebox.showerror('Error', 'An error occurred while fetching weather data.')

# Create the GUI window
window = tk.Tk()
window.title('Weather Forecast')

# Create and pack the widgets
label = tk.Label(window, text='Enter city:')
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text='Get Weather', command=lambda: get_weather(entry.get()))
button.pack()

# Run the GUI event loop
window.mainloop()
