import uuid

def get_random_code():
    code = str(uuid.uuid5())[:8].replace('-',''.lower())
    return code