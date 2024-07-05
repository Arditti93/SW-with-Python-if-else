capital_cites = {
    "England" : "London",
    "France" : "Paris",
    "Spain" : "Madrid"
}
print(capital_cites)
print(capital_cites["France"])

capital_cites["England"] = "Manchester"
print(capital_cites)
print(capital_cites.keys())
capital_cites.setdefault("England","Manchester")
print(capital_cites)


users = {
    1 : {
         "username" : "test",
         "password" : "password123",
         "bio" : "wrgwrwrgrgwrgw"
     },
    2 : {
        "username" : "test2"
    }
}
print(users[1]["username"])
print(users[2]["username"])
print(users)