from functools import wraps

def requires_registration(users):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not users:
                print("No users registered yet. Please register first.")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator
