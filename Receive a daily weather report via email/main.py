import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OpenWeatherMap API Key and City
api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
city = 'CITY_NAME,COUNTRY_CODE'  # Example: 'New York,US'

# OpenWeatherMap API URL
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Function to get weather information
def get_weather():
    response = requests.get(api_url)
    data = response.json()
    weather_desc = data['weather'][0]['description']
    temperature = data['main']['temp']
    return f'Today\'s Weather: {weather_desc.capitalize()}\nTemperature: {temperature}°C'

# Function to send email
def send_email(subject, body):
    sender_email = 'YOUR_EMAIL@gmail.com'
    sender_password = 'YOUR_EMAIL_PASSWORD'
    receiver_email = 'RECEIVER_EMAIL@gmail.com'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Get weather information
weather_info = get_weather()

# Send the email
send_email('Daily Weather Report', weather_info)
