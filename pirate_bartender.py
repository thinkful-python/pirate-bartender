import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
answers = {}

def smart_bartender():
  """ loop through each of the preferences in drinks with a yes or no answer """
  print "Don't know what you like? {} is here to help! Just answer 'y' or 'n' and we can figure it out!".format("Smart Bartender")
  for key, value in questions.items():
  #for flavor in questions: 
    answer = raw_input(value)
    if (answer == "y") or (answer == "Y"):
      answers[key] = True
      print answers; print "Yar a wise one"
    else: 
      answers[key] = False 
      print answers; print "Scallywag"
  return answers

def create_drink(answers):
  """ Use the answers to combine with ingredients to create drink """
  #drink = []
  print "\n Great, now let's add a little flavor to the mix"
  for key, value in ingredients.items():
   if answers[key]:
      #drink.append(random.choice(value))
      print "I got your back, Jack. Here's a {0} for something {1}".format(ingredients.values(), ingredients.keys())


  # for key, value in ingredients.items():
  #   if value is True:
  #     print "{0}".format(ingredients[answers])
  # return

if __name__ == '__main__':
  smart_bartender()
  create_drink(answers)
  