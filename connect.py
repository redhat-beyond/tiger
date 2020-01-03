def definedlog(fileHandler):
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)    
    handler = logging.FileHandler(fileHandler)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
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
        print( row )
        logger.debug(row)
    return view


def insertmessageintotable (conn, logger, username, TIMESTAMP, content):
    conn = connect_db ('localhost', 'root', 'LoginPass@@11223344', 'messages')
    try:
            cursor = conn.cursor()
            mysql_insert_query = """INSERT INTO messages (username, TIMESTAMP, content) VALUES (%s, %s, %s, %s) """

            recordmessages = (username, TIMESTAMP, content)
            cursor.execute(mysql_insert_query, recordmessages)
            conn.commit()
            logger.error( 'Record inserted successfully into messages table' )

    except conn.connector.Error as error:
            logger.error( 'Failed to insert into MySQL table {}' .format(error))

    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print ('MySQL connection is closed')


logger = definedlog('log.log')
conn=connect_db ('localhost', 'root', 'LoginPass@@11223344', 'messages')
print (conn)
logger.debug(conn)
messages = readmessages(conn, 'SELECT * FROM messages')

insertmessageintotable(conn, logger, 'morbi', 'TIMESTAMP', 'How u doing?')
messages = readmessages(conn, 'SELECT * FROM messages')
logger.debug( 'finish insert messages' )
