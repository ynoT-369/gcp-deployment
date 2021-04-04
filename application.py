import os
# import sys
from app import create_app

os.environ["FLASK_CONFIG"] = "production" # "development"

print("os.getenv(FLASK_CONFIG): ", os.getenv("FLASK_CONFIG"))
app = create_app(os.getenv("FLASK_CONFIG") or "default")
print(f"application: {__name__}")
print("application:", __name__ == "__main__")

if __name__ == "__main__":
    app.run()
