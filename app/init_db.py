from sqlalchemy import create_engine
from db import Base

engine = create_engine('postgres://postgres:postgres@database:5432/divide_service_db')

if __name__ == '__main__':
    Base.metadata.create_all(engine)


