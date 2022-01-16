from flask import session, redirect
from functools import wraps 

#creating a custom decorator 
def login_required(func):
    @wraps(func) #preserves the original name when creating the wrapped function
    def wrapped_function(*args, **kwargs):#*args and **kwargs ensures that all arguments are captured

        if session.get('loggedIn') == True:
            return func(*args, **kwargs)

        return redirect('/login')
    
    return wrapped_function