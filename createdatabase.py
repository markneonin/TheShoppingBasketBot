from database.database import engine
from database.tables import Base

Base.metadata.create_all(engine)

