import sqlite3



PASSWORD= '123'



enter = input("What is your password?\n")

while enter != PASSWORD:
    enter = input("What is your password?\n")
    if enter=="q":
        break

conn = sqlite3.connect('pass_manager.db')
c= conn.cursor()

def get_password(admin_pass):
    global password
    

    print("Enter service name: ")
    service=input()
    c.execute('SELECT * FROM KEYS WHERE SERVICE=?;',[service])
    print(c.fetchone())

    
    
        
                          


def add_password(admin_pass):
    global password
    
    
    print("Enter service name: ")
    service=input()
    #c.execute('INSERT INTO KEYS (SERVICE) VALUES (%s);' %('"' + service +'"'))
    #conn.commit()      
    
    
    print("Enter password: ")
    password= input()
    #c.execute('INSERT INTO KEYS (PASS_KEY) VALUES (%s);' %('"' + password +'"'))
    
    #conn.commit()



    c.execute('INSERT INTO KEYS (SERVICE,PASS_KEY) VALUES (?,?)',(service, password))
    conn.commit()


def update_password(admin_pass):
    global password
    
    print("Enter service name: ")
    service=input()
    print("Enter new password: ")
    password=input()

    c.execute('UPDATE KEYS SET PASS_KEY=? WHERE SERVICE=?',(password, service))
    conn.commit()

    

def show_database():
    with conn:
        c.execute("SELECT * FROM KEYS")
        print(c.fetchall())
    conn.commit()

    

if enter== PASSWORD:
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS KEYS
                    (SERVICE TEXT PRIMARY KEY,
                     PASS_KEY TEXT);''')
        print("Your safe has been created.")

    except:
        print("You have a safe.")

    while True:
        print("**********")
        print("q = quit ")
        print("s = show password")
        print("e = new entry")
        print("u = update password")
        print("sd = show database")
        print("**********")
        input_= input(":")


        if input_ == 'q':
            break
        if input_ == 'e':
            add_password(PASSWORD)
            

        if input_ == 's':
            get_password(PASSWORD)

        if input_ == 'u':
            update_password(PASSWORD)

        if input_ == 'sd':
            show_database()
           

            
        
        
    
          
           
