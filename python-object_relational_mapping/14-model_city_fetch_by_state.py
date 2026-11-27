#!/usr/bin/python3
"""Prints all City objects by state."""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    results = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id)
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
