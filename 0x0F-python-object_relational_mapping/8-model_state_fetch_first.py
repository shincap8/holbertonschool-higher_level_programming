#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""
if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    x = session.query(State.id, State.name).first()
    if x is None:
        print("Nothing")
    else:
        print("{}: {}".format(x.id, x.name))
    session.close()
