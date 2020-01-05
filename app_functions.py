def authenticate_user(username, password):
    if check_username(username):
        if check_password(username, password):
            return true
        else:
            # TODO: flash a message about incorrect password
            return false
        # TODO: flash a message about incorrent username
    return false

def check_password(us,password):
    mauser = mydb.cursor()

    Finder = "SELECT * FROM users WHERE username  ="+ us + " and password = " + password

    mauser.execute(Finder)

    result = mycursor.fetchall()

    if not result:
        # the password didn't match
        return false
    else:
        # the password match
        return true

#def check_username(username):
    #TODO: function logic

#def check_password(username, password):
    #TODO: function logic
