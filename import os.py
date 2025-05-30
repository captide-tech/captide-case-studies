import os
from dotenv import load_dotenv

load_dotenv()
CAPTIDE_API_KEY = os.getenv("CAPTIDE_API_KEY")
print(CAPTIDE_API_KEY)
