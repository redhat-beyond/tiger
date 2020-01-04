def authenticate_user(username, password):
    if check_username(username):
        if check_password(username, password):
            return true
        else:
            # TODO: flash a message about incorrect password
            return false
        # TODO: flash a message about incorrent username
    return false

#def check_username(username):
    #TODO: function logic

#def check_password(username, password):
    #TODO: function logic
