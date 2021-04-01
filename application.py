import os
# import sys
from app import create_app

print(os.getenv("FLASK_CONFIG"))
app = create_app(os.getenv("FLASK_CONFIG") or "default")
print(f"application: {__name__}")
print("application:", __name__ == "__main__")
