class User:
    def __init__(self,data):
        self.first_name=data['name']['first']
        self.last_name=data['name']['last']
        self.gender = data['gender']



user = {
            "gender": "female",
            "name": {
                "title": "Mrs",
                "first": "Clarisse",
                "last": "Gaillard"
            },
            "location": {
                "street": {
                    "number": 8929,
                    "name": "Rue de la Gare"
                },
                "city": "Grenoble",
                "state": "Pas-de-Calais",
                "country": "France",
                "postcode": 91622,
                "coordinates": {
                    "latitude": "77.7305",
                    "longitude": "149.3416"
                },
      
            },      
            "phone": "04-99-09-66-08",

        }


user = User(user)

print(user.first_name)