import sqlite3
import subprocess as sp

def create_table():
    conn = sqlite3.connect('score_db.sqlite')

    cursor = conn.cursor()

    # query = '''
    #     CREATE TABLE IF NOT EXISTS score_tbl(
    #         id INTEGER PRIMARY KEY, 
    #         name TEXT,
    #         score INTEGER,
    #     )
    # '''

    cursor.execute(" CREATE TABLE IF NOT EXISTS score_tbl( id INTEGER PRIMARY KEY, name TEXT, score INTEGER) ")

    conn.commit()
    conn.close()



def add_score(name,score):
    conn = sqlite3.connect('score_db.sqlite')

    cursor = conn.cursor()

    query = '''
        INSERT INTO score_tbl(name, score)
                    VALUES ( ?,? )
    '''

    cursor.execute(query,(name,score))

    conn.commit()
    conn.close()



def get_score(name):
    conn = sqlite3.connect('score_db.sqlite')

    cursor = conn.cursor()

    query = '''
        SELECT name, score
        FROM score_tbl
        WHERE name = name
    '''

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows


def delete_score(name):
    conn = sqlite3.connect('score_db.sqlite')

    cursor = conn.cursor()

    query = '''
        DELETE
        FROM score_tbl
        WHERE name = {}
    ''' .format(name)

    cursor.execute(query)
    all_rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return all_rows



def add_data(name,score):
    add_score(name,score)
def get_data(name):
    return get_score(name)

def show_data():
    scores = get_data()
    for score in score_tbl:
            print(score)


create_table()
