import json
from pathlib import Path


from os.path import exists


def create_json_file(path_to_json  = Path("importantFiles","data.json")) -> bool:#Return True if the file create, or False
    if not exists(path_to_json):
        with open(path_to_json, "w", encoding="utf-8") as write_file:
            json.dump({
    "users": {
        
            }
                        }, write_file, indent=4)
        return True
    
    return False


def check_user_in_database(user_id : str, path_to_json  = Path("importantFiles","data.json")) -> bool:#True if user in database, false if not
    with open(path_to_json, "r", encoding="utf-8") as read_file:
        read_json = json.load(read_file)

    if str(user_id) in read_json["users"]:
        return True
        
    return False


def add_user_to_database(user_id : int, path_to_json = Path("importantFiles","data.json")) -> bool: #True if user added, false if not
    result = check_user_in_database(user_id)

    if result:
        return False
    
    with open(path_to_json, "r", encoding="utf-8") as read_file:
        read_json = json.load(read_file)

    
    read_json["users"][str(user_id)] = {
        "contact_data" : None,
        "get_sample" : False
    }

    with open(path_to_json, "w", encoding="utf-8") as write_file:
        json.dump(read_json, write_file, indent=4)

    return True


def edit_contact_data(user_id : int, contact_data : str, path_to_json = Path("importantFiles","data.json")) -> bool: #True if successful edit, false if not
    result = check_user_in_database(user_id)

    if not result:
        return False

    with open(path_to_json, "r", encoding="utf-8") as read_file:
        read_json = json.load(read_file)

    read_json["users"][str(user_id)]["contact_data"] = contact_data

    with open(path_to_json, "w", encoding="utf-8") as write_file:
        json.dump(read_json, write_file, indent=4)

    return True



def change_get_sample(user_id : int, path_to_json = Path("importantFiles","data.json"))-> bool:
    result = check_user_in_database(user_id)

    if not result:
        return False
    

    with open(path_to_json, "r", encoding="utf-8") as read_file:
        read_json = json.load(read_file)

    read_json["users"][str(user_id)]["get_sample"] = True

    with open(path_to_json, "w", encoding="utf-8") as write_file:
        json.dump(read_json, write_file, indent=4)

    return True


def check_get_sample(user_id : int, path_to_json = Path("importantFiles","data.json"))-> bool:
    result = check_user_in_database(user_id)

    if not result:
        return False
    
    with open(path_to_json, "r", encoding="UTF-8") as read_file:
        read_json = json.load(read_file)

    return read_json["users"][str(user_id)]["get_sample"]


def get_contact_data(user_id : int, path_to_json = Path("importantFiles","data.json")) -> str:
    result = check_user_in_database(user_id)
    
    if not result:
        return None
    
    with open(path_to_json, "r", encoding="UTF-8") as read_file:
        read_json = json.load(read_file)
    
    return read_json["users"][str(user_id)]["contact_data"]

    




