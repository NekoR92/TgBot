import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import python_weather

bot = Bot(token="token")
dp = Dispatcher()
router = Router()

@router.message(Command(commands=["start", "help"]))
async def sendwelcome(message: Message):
    await message.answer("Привет этот бот показывает /weather за пиво.")

@router.message(Command(commands=["weather"]))
async def get_weather(message: Message):

        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get("Sevastopol")
            print(weather)  # Debugging: Print the entire weather object to see its structure

            # Attempt to print out attributes for better understanding
            print(dir(weather))  # Print all attributes of the weather object
            if hasattr(weather, 'current'):
                current_temp = weather.current.temperature

            elif hasattr(weather, 'temperature'):  # Check if temperature is directly available
                current_temp = weather.temperature

            else:
                raise AttributeError("Unable to find current weather attributes")

            response = f"Температура сегодня в севасике: {current_temp}°C , можно пить пивандопас\n"


            await message.answer(response)


@router.message()
async def echo(message: Message):
    await message.answer(message.text)

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


