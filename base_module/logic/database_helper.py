
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DATABASE HELPER
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pandas as PD
import sqlalchemy as SQL


def ConnectSqlite(dbPath):

    connectTx = f"sqlite:///{dbPath}"
    print(connectTx)

    engine = SQL.create_engine(connectTx, echo=False)
    meta = SQL.MetaData(bind=engine)
    meta.reflect()

    return meta, engine   # engine.connect()

def ConnectPostgreSql():

    hostUrl = ''
    database = ''
    user = ''
    password = ''
    connectTx = f"postgresql+psycopg2://{user}:{password}@{hostUrl}/{database}"
    print(connectTx)

    engine = SQL.create_engine(connectTx, echo=False, pool_size=20, max_overflow=0)
    meta = SQL.MetaData(bind=engine)
    meta.reflect()

    return meta, engine

