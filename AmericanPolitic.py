import random



amb_act=["whispered to","shouted to","texted","wrote a letter to",
         "cried to","incoherently mumbled to","morsed to",
         "reassured","gossiped with","screamed at","telegraphed to",
        "emailed to","lectured","convinced"]

ext_person=["the Queen","Charlie Sheen","Bill Gates",
            "Bill Clinton","Kim Jong Un","Edward Snowden",
            "Angela Merkel","my friend","Ozzy Osbourne",
            "this hobo I met on the street","my dentist",
           "Leonardo DiCaprio","Jake Gyllenhaal","Seth Rogen",
           "Jesus","Will Smith","god","the pope",
            "the artist formerly known as Prince","Keanu Reeves"]

prefix=["healthy","tired","adorable","silly","dangerous",
        "aggrevated","hyped","drunken","intelligent",
        "sick","weird","sad","addicted","abducted","silent","educated"]

animals=["wolves","turtles","bisons","snakes","sharks",
         "monkeys","spiders","birds","ants","horses",
         "hyenas","antelopes","anteaters","polar bears","cats",
        "alligators","leeches"]

enemy=["on Moon separatists","\nagainst a local theater group",
        "against a nightclub owner","\nagainst the rest of the world",
        "\non the western hemisphere","\nagainst the eastern hemisphere",
        "\non a small town in Europe","on taxes",
        "\non unsafe eating behavior","against South America",
        "\nwith all that is at his disposal","against Africa",
        "against Australia"]

city=["Wyoming","Chicago","Detroit","Washington DC",
      "Tallahassee","Austin","Moskau","Berlin",
      "Ottawa","London","Sao Paulo","Sydney","New Orleans",
      "Amsterdam","Rome","Paris","Prague","Peking","Pyongyang",
      "New Dheli"]

location_spec=["national parks","malls","gyms","skate parks",
               "shady back alleys","gun ranges",
               "garbage dumps","air ports","nightclubs",
               "hospitals","factories","bank vaults","zoos",
              "carnevals","the streets","our homes","rocket silos",
              "interrogation camps"]


interest=["doesn't give much about the fact ","totally wants to make sure ",
          "kinda can agree with the fact ",
          "is extremely shaken ","just won't understand "]

season=["Winter","Spring","Summer","Autumn"]

forum_nat=["Columbian","Peruvian","Mongolian",
           "Mayan","Indian","Vietnamese",
           "Venezuelan","Pakistani","Somali","Ukrainian",
          "Chilenian","Egyptian","Portuguese",
          "Cuban","Aztec","Hawaiian","Bolivian","Namibian",
          "Argentinian","Mauritanian","Chinese","Latvian",
          "Belarusian","North Korean","Spanish","Algerian",
          "Ethiopian","Bangladeshi","Cambodian",
          "Japanese","Greek","Armenian","Ecuadorian","Estonian",
          "Syrian","Finnish","Danish","Swedish","Dutch","Ethiopian",
          "Nepalese","Croatian"]
             
weaponry=["crossbows","sharpened sticks","Exosuits",
          "knives","slingshots","C4 packets","hatchets","battle axes",
          "BB guns","knowledge","dry baguettes","RPGs",
          "nano bots","assault rifles","broken bottles",
          "rusty nails","chainsaws","machetes","dull katanas",
          "flails","tanks","nukes","baseball bats",
         "flamethrowers"]

dessert=["salt","Soylent Green","frozen beer","pizza","cigarettes",
         "mystery meat","vegetables","maple syrup","opium","caviar",
         "free market","freedom","Nootropics","raisins with pepper",
         "dry cornflakes","fingernails","frozen Whiskey","oysters",
         "tuna melts","dry oats","frozen vanilla-scorpion ice cream",
        "really greasy stuff","way too healthy stuff","Twinkies"]

product=["opium","mold","cocaine","lead powder",
         "crushed beetles","spider candy","alien figurines",
         "pastry","LSD","peyote","silver nitrate",
         "chemtrails","coffee","hamster milk",
         "bamboo flutes","DMT","methamphetamine","hover boards",
         "steroids","cough syrup","research chemicals","PCP",
        "vitamine supplements","Dr. Pepper","probiotic energy water",
        "spider-cookies","cigarettes","weed","snake oil","nano bots",
        "spray paint","asbestos","plutonium"]

catastrophe=["famine","nuclear annihilation","earthquake",
             "uprising of the working class",
             "meteor hit","zombie invasion","%s invasion"%(random.choice(forum_nat)),
             "water pipe damage","propaganda campaign",
             "%s shortage"%(random.choice(dessert)),"boozing","alien message",
             "Tsunami","\nglobal stock market crash","volcano eruption",
             "tornado","hurricane"]

booktheme=["knitting","naval combat","%s monks"%(random.choice(forum_nat)),
           "investment banking","burglary","merrymaking",
           "funny jokes","programming","hydroponics",
           "beer flavors","online banking","exotic cooking",
           "subtle propaganda","circuits and such","opening of the third eye",
           "%s sit-ups"%(random.choice(forum_nat)),"tuna melts","Red Bull connoisseurs",
           "travelling birdwatchers","%s bathroom etiquette"%(random.choice(forum_nat)),
           "Zen Buddhism","Martial Arts","going berserk","informative painting",
           "the recent %s"%(random.choice(catastrophe)),
           "organic drug syntheses","mining efficiently",
           "not messing it up","carefully consuming water",
           "%s %s"%(random.choice(prefix),random.choice(animals)),"%s pop stars"%(random.choice(prefix)),
           "%s cineasts"%(random.choice(prefix)),
           "conspiracy theories","total surveillance","Scientology",
          "woodworking","insurance fraud","prostitution"]

shop=["a cat-barbershop","a lobster fast-food chain",
      "a liquor store","a laundry","a lottery store",
      "a %s textile delivery"%(random.choice(forum_nat)),"a Hollywood catering agency",
      "a gaming arcade \ncatering to nostalgics","the same Starbucks as always",
     "a shop selling %s %s"%(random.choice(forum_nat),random.choice(weaponry)),
     "a local %s den"%(random.choice(product)),
     "a diving school","a pet store","a circus","a brothel",
     "a toy store","a fish market"]

forum_act=["dry-washing","investment","kite-flying",
           "gardening","programming","management","basket-weaving",
           "cat-petting","worm-counting","kitten-taming",
          "snailhouse-enthusiast","bacon-rating","TV host-review",
          "acapella-freelance","glass-blowing","stamp-collecting",
           "designer-cloth","camel-breeding","solar panel",
           "IT class","astronomy","meteorology","sheep-teaching",
          "wall-building","notch-carving","finger-painting",
          "geode-watching","coin-throwing","blowgunning",
          "forensic-enthusiasts","Anime-voicing","shed-building"]

president=["Vladimir Putin","Joseph Stalin","Mao Zedong",
           "Adolf Hitler","Dick Cheney","George W. Bush",
           "Pol Pot","Francisco Franco","Benito Mussolini","Caesar"]

concert_band=["Linking Park","AC/DC","P!nk","Kanye West",
               "Metallica","Weird Al","Eminem","Rise Against",
               "Lady Gaga","Arctic Monkeys","Macklemore",
             "Cypress Hill","Beyonce"]

concert_item=["bracelets","buttons","guitars","shirts",
              "furniture","chocolate bars","cars","jeans",
              "posters","glasses","backpacks","%s"%(random.choice(weaponry))]

org=["cult","church","living commune","underground facility",
     "artist collective","NGO","library","mercenary squad",
    "organisation","hivemind"]

consume=["ate","smoked","injected","consumed",
         "absorbed","snorted","took"]

dump=["lakes","warehouses","somebody's living room",
      "foreign nations","the unknown depths of space",
      "a government warehouse"]

jobs=["cartel lord","poacher","brain surgeon",
      "weatherman","cruise ship captain","sniper","investment banker",
      "rich person","lizard person","car mechanic","rocket scientist",
      "dog breeder","wolf tamer","lion healer","tourist",
      "%s producer"%(random.choice(product)),"astronaut",
      "%s salesman"%(random.choice(product)),"plumber",
     "expressive dancer","gourmet cook","food critic",
     "rebel leader","nuclear engineer","performance activist",
     "weekend warrior","augmented soldier","citizen","beggar",
     "voodoo priest","bear jockey","golfer","paraglider"]

tourist_act=["gathered intelligenge that","filmed how",
             "randomly saw how","met this minister who swears that",
             "sat in a coffeehouse and observed that",
             "but my vacation was cut short because"]

v1=["In the current political climate, \n",
    "During this time of crisis, \n",
    "The fact that I'm wearing a tin foil hat doesn't contradict that \n",
    "Last week I visited %s and %s\n"%(random.choice(city),random.choice(tourist_act)),
    "Barely within the limits of our national pride, \n",
    "In the name of our conservative standards, \n",
    "While the enemy reforms his means of production, \n",
    "As the sun crossed the middle of our American skies, \n",
    "The moment the lasers hit our country, \n",
    "Just when the lizard people saw their chance, \n",
    "As the future reveals itself to us, \n",
    "For real now, %s %sthat \n"%(random.choice(ext_person),random.choice(interest)),
    "Word on the street is \n",
    "The communist party predicts that \n",
    "The world lies in shambles, \nand ",
    "%s %d was the time when \n"%(random.choice(season),random.randint(2016,2024)),
    "Anarchy crawls back into the hole it came from precisely when \n",
    "Total Anarchy is on the brink of happening because \n",
    "The radical right-wing ran a simulation. The results? \n",
    "TV just convinced me that \n",
    "Throwing out every last ounce of dignity, \n",
    "Going above and beyond the call of duty, \n",
    "In a sharp regress to medieval values, \n",
    "Full of idealistic spirit, \n",
    "Troop movement at the border forced a response: \n",
    "The riots stopped for exactly two minutes when it became apparent that \n",
    "Surprisingly enough, the recent %s doesn't change anything: \n"%(random.choice(catastrophe)),
    "I read on that %s %s forum that \n"%(random.choice(forum_nat),random.choice(forum_act)),
    "My sources handed me intel that states that \n",
    "All red lights are flashing as soon as \n",
    "A well-known radical leftist think tank wants me to tell you that \n",
    "With blatant disregard for \nthe health of any voter out there, \n",
    "During the second Kremlin robot revolution, \n",
    "A while ago I %s some %s and vividly observed how \n"%(random.choice(consume),random.choice(product)),
    "Wasted and totally devoid of rational thought, \n",
    "The public outrage reaches a critical plateau as \n",
    "Civilization as we know it is going to collapse because \n",
    "As DEFCON hits the negative numbers, \n",
    "Radio told me that \n",
    "The %s ambassador %s me that \n"%(random.choice(forum_nat),random.choice(amb_act)),
    "In a blatant attempt to secure absolute power, \n",
    "I had a vision in which %s\n%s me that \n"%(random.choice(ext_person),random.choice(amb_act))]
    
v2=["Hillary Clinton ",
    "Bernie Sanders ",
    "Donald Trump ",
    "Ben Carson ",
    "Jeb Bush ",
    "President Robot ",
    "Barack Obama "]

body_part=["forehead","thigh","wrist","biceps","forearm",
           "neck","calf","lower back","upper back","belly",
           "cheek","ankle","chest","knee"]

v4=["should totally ",
    "needs to publicly defend the urge to \n",
    "is going to ",
    "will ",
    "told everyone the adamant view \nabout wanting to ",
    "has sworn to ",
    "told everyone about \nwanting to ",
    "took an oath to ",
    "vowed to ",
    "appealed to everyone to ",
    "wants you to ",
    "said the model citizen is supposed to \n",
    "lied to a priest about the desire to \n",
    "is strongly opposed to ",
    "was instructed by foreign forces to \n",
    "spent several years in the mountains, \npreparing to ",
    "hired a professional to ",
    "tried unsuccesfully to ",
    "always waited for the right moment to \n",
    "was getting annoyed not being able to \n",
    "started building a strange contraption that will \n",
    "finally found \nthe courage to ",
    "at last decided to go through \nwith the idea to ",
    "blackmails the entire population to \n",
    "visited Russia, discussing the plan to \n",
    "realised the life long dream to \n",
    "is probably not going to actually \n",
    "never ever will ",
    "rather lets the sentient military drones \n",
    "dared the opposition to \n",
    "encouraged the listeners to \n",
    "was seen spraying graffiti \nthat encourages people to \n",
    "made shady deals with cloaked and daggered figures to \n",
    "presents a new %s tattoo, \nindicating an inclination to \n"%(random.choice(body_part)),
    "recently admitted to secretly enjoy to \n",
    "clearly fantasizes \nabout every %s %s being able to \n"%(random.choice(forum_nat),random.choice(jobs)),
    "was sentenced by the high court to \n",
    "opened a press conference \nto state that if needed, every citizen could \n", 
    "only needs to raise an eyebrow \nand the army would immediately \n",
    "composes a fine piece of propaganda, telling everyone to \n",
    "recently asked %s for help to \n"%(random.choice(ext_person)),
    "challenges every citizen, \nthe adversaries in particular, to \n",
    "is giving a passionate speech about how \nthe average %s should \n"%(random.choice(jobs))]
    
v5=["a degree in minimum-waging","birth on Mars",
    "birth on Jupiter","birth on Earth","serving time in the %s infantry"%(random.choice(forum_nat)),
    "winning a hot dog eating contest","winning a home decoration contest",
    "being a good person","being good at having pets",
    "being older than three years","not being a villain",
    "being a villain","understanding the internet",
   "birth at the feet of a holy mountain","having been at Coachella"]

timespan_add=(random.randint(2,12))
timespan=["for the next few months",
          "for the next %d months"%(timespan_add),
          "for the next %d years"%(timespan_add),
         "for a good laugh and a story"]
     
extremists=["a stern talk and a ride home",
            "cheaply manufactured %s"%(random.choice(weaponry)),
            "a kickpunch into the %s"%(random.choice(body_part)),
            "a raise","a retirement fond","an Oscar","more %s"%(random.choice(product))]

cat_act=["shoot mud at a %s"%(random.choice(jobs)),"help out NASA",
         "hunt the whales","get rid of rubble",
         "make Americans fly, once in their lives",
         "simulate darker times","be closer to god",
         "strenghten the trans-Atlantic partnership",
         "launch a counter-attack"]

action_spec=["disguised as Big Foot","trying to push an agenda",
             "stealing from pockets","making people smile","pretending to belong",
             "trying to sabotage the electronics","pretending not to be sad",
             "selling some %s"%(random.choice(product)),
             "advertising a website","waiting for a call",
             "meeting with some %s %s"%(random.choice(forum_nat),random.choice(jobs))]

combined=[random.choice(product),random.choice(dessert),
          random.choice(weaponry)]

industry=["private security sector","music industry",
          "gun economy","food business sector","animal breeding sector",
          "agrarian sector","banking sector","building business",
          "way our government works","mass of unspeakable problems in our country"]

become_the=["only","best","worst","most well adjusted",
           "most gracious","nicest","most intrigant",
           "most treacherous"]

status=["illegal","legal","are mandatory in every household",
        "are to be burned on sight","are too big to fail"]

object1=["the constitution","community centers","welfare checks",
        "food stamps","tax documents","whistle blowers",
        "security cameras","evil forces","colleges","evolution textbooks",
        "bibles"]

status2=["famous","well-known","powerful","criminal","legal",
         "controversial","highly praised","unconstitutional",
        "corrupt","critical","fundamental","crucial"]

econ_act=["water-tight embargo of","increased import prices of",
          "governmental support for smugglers of",
          "subsidizing abroad production of",
          "higher quality control of","prohibition of"]

hair=["A blue dyed mohawk","Long braided hair",
      "A bald shaven head","Pig tails","Neatly combed white dyed hair",
      "Star shaped sideburns","An army helmet",
     "A fedora","A hockey mask","A gas mask","Sunglasses"]# hanging ','

color=["blue","red","white",""]

shirt=["a %s military jacket"%(random.choice(color)),"Uncle Sam's vest",
       "a %s suit top"%(random.choice(color)),
       "a %s bulletproof vest"%(random.choice(color)),"a Hawaiian shirt",
       "a %s shirt with %s howling at the moon"%(random.choice(color),random.choice(animals)),
       "a long-sleeved hemp jacket","a wifebeater","a %s payama top"%(random.choice(color))]

pants=["%s suit pants"%(random.choice(color)),"cargo pants","a kilt","Uncle Sam's pants",
       "Bahama shorts","armored pants","%s football pants"%(random.choice(color)),
       "%s golf shorts"%(random.choice(color)),"tracking suit pants","jeans",
       "leather pants","satin pants"]

school=["for re-education purposes",
        "for a better understanding of %s"%(random.choice(booktheme)),
        "for old times sake","to improve the reputation with the young crowd",
        "for the free meal in the cantine","for the feeling of being another brick in the wall",
        "to text in the back row"]

v3=["wage war %s."%(random.choice(enemy)),
    "brutally stab Caesar multiple times.",
    "cause a national panic.",
    "eat what little is left of the \n%s."%(random.choice(dessert)),
    "bite %s in %s."%(random.choice(animals),random.choice(location_spec)),
    "get bitten by a bunch of %s."%(random.choice(animals)),
    "play %s on Broadway."%(random.choice(president)),
    "press buttons in the Oval Office.",
    "invite %s spies \ninto our %s."%(random.choice(forum_nat),random.choice(location_spec)),
    "run around in %s \n%s."%(random.choice(location_spec),random.choice(action_spec)),
    "pick up trash at %s \nand store it in \n%s."%(random.choice(location_spec),random.choice(dump)),
    "look at a bunch of %s \na little more closely."%(random.choice(weaponry)),
    "read the newspaper every day.",
    "be kind to the neighbors.",
    "eat healthier food from now on.",
    "eat %s for a \nfew months."%(random.choice(dessert)),
    "sell counterfeit %s at \n%s concerts."%(random.choice(concert_item),random.choice(concert_band)),
    "feed the %s and \nwater the plants while the \nneighbors are gone."%(random.choice(animals)),
    "be a cop on the \nrough streets of %s."%(random.choice(city)),
    "shoplift at %s."%(random.choice(shop)),
    "clandestinely open \n%s."%(random.choice(shop)),
    "find peace in %s."%(random.choice(booktheme)),
    "display advertising \nfor %s."%(random.choice(product)),
    "read a book \nconcerning %s."%(random.choice(booktheme)),
    "eat %s once more."%(random.choice(dessert)),
    "build a catapult \nto %s."%(random.choice(cat_act)),
    "invoke order 66.",
    "go back to school \n%s."%(random.choice(school)),
    "claim that %s might \nnot be so bad afterall."%(random.choice(object1)),
    "proclaim %s %s."%(random.choice(object1),random.choice(status)),
    "force public acceptance \nof eating %s as a dessert."%(random.choice(dessert)),
    "transform into a Cyborg.",
    "rob %s \nfor at least %d days a year."%(random.choice(shop),random.randint(10,300)),
    "forbid apples and oranges \nbecause they are misleading.",
    "show a document which certifies \n%s."%(random.choice(v5)),
    "give local extremists \n%s."%(random.choice(extremists)),
    "sell a container filled with \n%s to gangsters."%(random.choice(weaponry)),
    "make %s more widely available."%(random.choice(dessert)),
    "import incredible amounts \nof %s %s."%(random.choice(forum_nat),random.choice(product)),
    "arm the air force with %s."%(random.choice(weaponry)),
    "discourage people from \npartying after %d PM."%(random.randint(1,11)),
    "start being part \nof some %s %s."%(random.choice(forum_nat),random.choice(org)),
    "party all night on %s."%(random.choice(product)),
    "smuggle copious amounts of \n%s into the White House."%(random.choice(product)),
    "become the %s \n%s %s."%(random.choice(become_the),random.choice(forum_nat),random.choice(jobs)),
    "defend the country \nonly wielding two %s."%(random.choice(weaponry)),
    "prohibit touching \n%s %s."%(random.choice(product),random.choice(timespan)),
    "found a %s %s %s \ncentered around %s."%(random.choice(status2),random.choice(forum_nat),random.choice(org),random.choice(booktheme)),
    "just relax for a bit.",
    "go to jail %s \nand also get %s."%(random.choice(timespan),random.choice(extremists)),
    "go to jail %s, \nwaiting for the heat to cool off."%(random.choice(timespan)),
    "shift the funding towards \nthe countries most important demographic: \nThe %s."%(random.choice(jobs)),
    "strive for alchemic transmutation \nof science funding to %s."%(random.choice(combined)),
    "reform the entire \n%s through \na %s %s %s."%(random.choice(industry),random.choice(econ_act),random.choice(forum_nat),random.choice(combined)),
    "wear the new mandatory American outfit:\n%s combined with \n%s and %s."%(random.choice(hair),random.choice(shirt),random.choice(pants))]

    
    

# this is where the main message gets built   
message= random.choice(v1) \
+random.choice(v2) \
+random.choice(v4) \
+random.choice(v3)

print (message) # upgraded to python 3.x AKA easiest port ever.

#input() #TommyHanusa was here

import tkinter
Tkinter = tkinter # this is badd hacks

class MessageUI:

    text = None # this will be the text box element
    button = None# this will be teh buton you click
    
    message = None # this will store the message. 
    
    def __init__(self, master):# master is a reference to the interlink object 
    
        frame = Tkinter.Frame(master)
        frameTop = Tkinter.Frame(master)
        master.title("AmericanPolitic") # this is the program name
        
        self.message = self.get_message()
        
        print(self.message)
        
        self.text = tkinter.Text(frameTop, height= (len(self.message)/75)+1, width = 75, bg='lightgrey', relief = 'flat',wrap=tkinter.WORD)
        self.text.insert(tkinter.END, self.message)
        self.text.config(state= tkinter.DISABLED) # forbid text edition #
        self.text.pack()
        
        self.button = Tkinter.Button(frame, text="New message", command= self.set_text)
        self.button.pack()
        
        frame.pack(padx=10, pady=10)# this puts a padding or 'bleed' on our work in the frame 
        frameTop.pack(padx=10, pady=10)# have a top frame # should allow extra packing
        
        #self.testing()# this is a simple test
        
        pass
    
    def set_text(self):# Sets the message in the text box # should really be called Set Message but whatever
    
        self.message = self.get_message()
        print(self.message)
        
        self.message = self.message.replace("\n","")# remove new ling characters that are screwing with formatting?
        self.message = self.message.replace("  "," ")# replace a bad formating i saw once
        print(self.message)
        
        self.text.config(state= tkinter.NORMAL) 
        self.text.delete(1.0,tkinter.END)
        self.text.insert(1.0, self.message)
        self.text.config(state= tkinter.DISABLED)
        self.text.config(height= (len(self.message)/75)+1)
        
        pass
    def get_message(self):
        temp = random.choice(v1) + random.choice(v2) + random.choice(v4) + random.choice(v3)
        temp = temp.replace("\n","")# remove new ling characters that are screwing with formatting?
        return  temp
        
    def testing(self):
        for  i in range(1000):
            self.button.invoke()
        
    


root = Tkinter.Tk()

ui = MessageUI(root)

frame = Tkinter.Frame(root)
label = Tkinter.Label(root, text='')

def get_message():
    message = random.choice(v1) + random.choice(v2) + random.choice(v4) + random.choice(v3)
    
    print (repr(len(message)) +" = "+repr(len(message)/60))
    
    t = tkinter.Text(root, height= (len(message)/60)+1, width = 60, bg='lightgrey', relief = 'flat')
    t.insert(tkinter.END, message)
    t.config(state= tkinter.DISABLED) # forbid text edition
    t.pack()
    
    label.config(text=message)



root.mainloop()