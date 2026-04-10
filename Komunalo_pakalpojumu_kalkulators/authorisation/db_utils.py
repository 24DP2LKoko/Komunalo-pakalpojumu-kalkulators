import mysql.connector

def pievienoties_db():
    mydb = mysql.connector.connect(
        host="sql.freedb.tech",
        user="freedb_dominiks",
        password="wDCZqbM3v2D!3Er",
        database="freedb_dzivokli"
    )
    mycursor = mydb.cursor()
    return mydb, mycursor