
    def check_username(us):
        maulers = mydb.cursor()

        Fender = "SELECT * FROM users WHERE username  =" + us

        maulers.execute(Fender)

        result = mycursor.fetchall()

        if not result:
            # the user doesnt exist
            return false
        else:
            # the user exists
            return true

#def check_password(username, password):
    #TODO: function logic


def authenticate_user(username, password):
    if check_username(username):
        if check_password(username, password):
            return true
        else:
            # TODO: flash a message about incorrect password
            return false
        # TODO: flash a message about incorrent username
    return false
