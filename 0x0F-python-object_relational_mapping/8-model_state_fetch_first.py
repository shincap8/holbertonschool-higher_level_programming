#!/usr/bin/python3
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

    for sid, name in session.query(State.id, State.name).filter(State.id == 1):
        print("{}: {}".format(sid, name))
