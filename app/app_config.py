from dotenv import load_dotenv, dotenv_values

load_dotenv()
env = {**dotenv_values(".env")}
