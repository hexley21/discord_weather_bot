import discord
import requests

appid = "your app id"

def get_weather(city):
    city = city
    api = f'https://api.openweathermap.org/data/2.5/weather?q=" + city + \
          "&units=metric&appid={appid}'
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    temp_min = int(json_data['main']['temp_min'])
    temp_max = int(json_data['main']['temp_max'])
    humidity = int(json_data['main']['humidity'])
    wind = json_data['wind']['speed']
    _city = json_data["name"]

    final_data = f"Weather in {_city}:\n" + \
                 f"Condition : **{condition}**\n" + \
                 f"Temperature : **{temp}°C**\n" + \
                 f"Max Temp : **{temp_max}°C**\n" + \
                 f"Min Temp : **{temp_min}°C**\n" + \
                 f"Humidity : **{humidity}%**\n" + \
                 f"Wind Speed : **{wind}m/sec**\n"

    return final_data


client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} is up".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$weather "):
        try:
            city = message.content.replace("$weather ", "")
            print(get_weather(city))
            await message.reply(get_weather(city))
        except Exception as e:
            print(str(e))
            await message.reply("This city doesn't exist or is entered incorrectly", mention_author=True)


token = "your discord token"
client.run(token)
