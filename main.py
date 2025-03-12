import yr_weather


sitename = 'https://innersource.soprasteria.com/'
# Replace with your own User-Agent. See MET API Terms of Service for correct User-Agents.
headers = {
    "User-Agent": sitename,
}

my_client = yr_weather.Locationforecast(headers=headers)

oslo = 59.91, 10.75
# Get air temperature in Oslo, Norway
oslo_temp = my_client.get_air_temperature(*oslo)

print(oslo_temp)

# Get full forecast for Oslo, Norway
forecast = my_client.get_forecast(*oslo)

# Select the forecast for the time right now (as it's possible to select a time further in the future)
forecast_now = forecast.now()

# You can now select from multiple data points. As an example, we show air pressure and wind speed.
pressure = forecast_now.details.air_pressure_at_sea_level
wind_speed = forecast_now.details.wind_speed

print(f"Air pressure at sea level in Oslo, Norway, is {pressure} hPa and the wind speed is {wind_speed} m/s")
