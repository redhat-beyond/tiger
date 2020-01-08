def check_username(us):
    maulers = connection.cursor()
    Fender = "SELECT * FROM users WHERE username  =" + us
    maulers.execute(Fender)
    result = maulers.fetchall()
    if not result:
        # the user doesnt exist
        return False
    else:
        # the user exists
        return True
