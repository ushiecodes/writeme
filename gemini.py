import os
from google import genai
from dotenv import load_dotenv

# Load variables from .env.local
load_dotenv(dotenv_path=".env.local")

# Access API KEY
API_KEY = os.getenv("API_KEY")

# Parse the API KEY
client = genai.Client(api_key=API_KEY)

# establish a connection with the model and test if it is working
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="say hello, turtell!"
)

print(response.text)
