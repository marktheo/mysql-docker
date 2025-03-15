import mysql.connector as mysql

def main():
    mysqlconn = mysql.connect(
        user='...', 
        password='...', 
        database='...',
        host='127.0.0.1', 
        port=3306
    )
    cursor = mysqlconn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER(16) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(64))")

    cursor.execute("INSERT INTO test VALUES (name) ('Marcos')")

    cursor.execute("SELECT * FROM test")
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    mysqlconn.close()

if __name__ == "__main__":
    main()
