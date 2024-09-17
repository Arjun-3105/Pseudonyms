'''printing side kick name by combining some funky first and last names'''
import random

print("Welcome to side kick name picker\n\n")

first_names = (
    'Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
    "Bob Stinkbug", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
    'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
    'Chewy', 'Chigger', "Cinnabuns", 'Cleet', 'Cornbread', 'Crab Meat',
    'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
    'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
    'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
    'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
    'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
    'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
    'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
    "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
    'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
    'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
    "Winston 'Jazz Hands'", 'Worms'
)

last_names = (
    'Applegate', 'Auger', 'Biffle', 'Bigmeat', 'Bloominshine',
    'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof',
    'Clutterbuck', 'Cocktoasten', 'Endicott', 'Featherbottom', 'Guster',
    'Hooperbag', 'Jefferson', 'Jenkins', 'Liverbottom', 'McFadden', 
    'Muckinfutch', 'Nettles', 'Noseworthy', 'Oglethorpe', 'Outerbridge', 
    'Overpeck', 'Pennywhistle', 'Pinkerton', 'Porkins', 'Putney', 
    'Raggles', 'Ramsbottom', 'Scratcher', 'Silversmith', 'Snuggleshine', 
    'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins', 
    'Turnipseed', 'Vanderlay', 'Wafflestomp', 'Whipkey', 'Wigglesworth', 
    'Wimplesnatch', 'Winterkorn', 'Woolysocks', 'Zamboni', 'Zippydingle'
)

i = 'y'
while i == 'y':
    RED =  "\033[91m"
    RESET = "\033[0m"
    f_n = random.choice(first_names)
    l_n = random.choice(last_names)
    final_name = f_n + " " + l_n
    # Only the final_name is red
    print("Your side-kick name is: " + RED + final_name + RESET, end='\n\n')

    i = input("Try again? (Press Enter else n to quit)\n")
