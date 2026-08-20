With SQLAlchemy:

from sqlalchemy import create_engine
engine = create_engine("sqlite:///company.db")

The engine becomes the main connection point between your Python application and the database.

Your Python Code
       ↓
   SQLAlchemy
       ↓
     SQLite
       ↓
   company.db