class User:
    def __init__(self,data):
        self.first_name=data['name']['first']
        self.last_name=data['name']['last']
        self.gender = data['gender']
        self.phone = data['phone']

