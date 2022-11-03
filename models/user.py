def create_user(row):
    user = {
        "id" : row[0],
        "username": row[1],
        "password" : row[2],
        "profile_picture" : row[3],
        "user_full_name" : row[4],

        "role" : {
            "id":row[7],
            "name":row[8],
            "description":row[9]
        }
    }

    try:
        user["password"] = user["password"].decode("utf-8")
    except AttributeError:
        pass

    if user["role"]["id"] is None:
        user["role"] = None

    return user
    