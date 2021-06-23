"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DATABASE HELPER
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pandas as PD
import sqlalchemy as SQL


def openConnection(dbPath):

    connectTx = f"sqlite:///{dbPath}"
    print(connectTx)

    engine = SQL.create_engine(connectTx, echo=False)
    meta = SQL.MetaData(bind=engine)
    meta.reflect()

    return meta, engine   # engine.connect()


