#!/usr/bin/python3
"""
script that changes the name
of a State object from the
database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
import sqlalchemy
import sqlalchemy.orm


def main():

    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker(engine)
    # HERE: no SQL query, only objects!
    session = Session()

    query = session.query(State).filter(State.id == 2).first()

    if query is None:
        print('Not found')
    else:
        query.name = "New Mexico"
        session.add(query)
        session.commit()

    session.close()


if __name__ == '__main__':
    main()
