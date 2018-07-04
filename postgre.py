import psycopg2
import sys



def main():
    #change the dbname, username and password as you have set
    conn = psycopg2.connect(dbname="testdb", user="person", password='123')
    cur = conn.cursor()
    #if there is a duplicated table exists, drop it
    cur.execute("DROP TABLE IF EXISTS users;")
    #create new table
    cur.execute("""
    CREATE TABLE users(
        id integer PRIMARY KEY,
        email text,
        name text,
        address text
        )
    """)
    #insert some values into columns
    insert_query = "INSERT INTO users VALUES {}".format("(10, 'hello@dataquest.io', 'Some Name', '123 Fake St.')")
    cur.execute(insert_query)
    #fetch all the columns from table
    cur.execute("SELECT * FROM users;")
    one = cur.fetchone()
    print(one)
    conn.close()

if __name__ == '__main__':
    main()
