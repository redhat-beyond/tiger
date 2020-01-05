def definedlog(fileHandler):
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(fileHandler)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def connect_db(host, user, password, database):
    import mysql.connector
    connection= mysql.connector.connect(
      user= user, password=password, host=host, database=database)
    return connection

def readmessages(conn, query):
    message = conn.cursor()
    message.execute(query)
    view = message.fetchall()
    for row in view:
        print(row)
        logger.debug(row)
    return view


logger = definedlog('log.log')
conn=connect_db('localhost', 'root', 'LoginPass@@11223344', 'messages')
print(conn)
logger.debug(conn)
messages = readmessages(conn,"SELECT * FROM messages")
