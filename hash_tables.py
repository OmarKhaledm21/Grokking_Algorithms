def check_voter(name):
    if voted.get(name):
        print ("kick them out!")
    else:
        voted[name] = True
        print ("let them vote!")


voted = {}
check_voter("tom")
check_voter("tom")

price_db = dict()

price_db['apple']=0.67
price_db['milk']=1.49

print(price_db['milk'])
