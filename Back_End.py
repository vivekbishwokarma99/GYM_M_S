import sqlite3


def connect():
    conn = sqlite3.connect("client.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY, name text, address text, mobile_no integer, \
     email_address text, date_of_birth integer, gender text)")

    conn.commit()
    conn.close()

def insert(name=" ", address=" ", mobile_no=" ", email_address=" ", date_of_birth=" ", gender=" "):
    conn = sqlite3.connect("client.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO client VALUES (NULL,?,?,?,?,?,?)",
                (name, address, mobile_no, email_address, date_of_birth, gender))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("client.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM client")
    rows = cur.fetchall()
    return rows

    conn.close()


def delete(id):
    conn = sqlite3.connect("client.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM client WHERE id  = ?", (id,))

    conn.commit()
    conn.close()


def update(id, name=" ", address=" ", mobile_no=" ", email_address=" ", date_of_birth=" ", gender=" "):
    conn = sqlite3.connect("client.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE client SET name = ? OR address = ? OR mobile_no = ? OR email_address = ? OR date_of_birth = ? OR gender = ?",
        (name, address, mobile_no, email_address, date_of_birth, gender))

    conn.commit()
    conn.close()

connect()
