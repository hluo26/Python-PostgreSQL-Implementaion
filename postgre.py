import psycopg2
import sys



def main():
    #change the dbname, username and password as you have set
    try:
        conn = psycopg2.connect(host="localhost", dbname="testdb", user="haoluo", password='0826')
    except:
        print("unable to connect database")
        sys.exit()
    cur = conn.cursor()
    cur.execute("select table_name from information_schema.tables where table_schema='testdb';")
    print(cur.fetchone())


if __name__ == '__main__':
    main()
