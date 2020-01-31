class sugar_class:
    def __init__(self):
        self.sweeteners_list = ["nectar",
                    "siroop",
                    "ahorncrème",
                    "amazake",
                    "concentraat",
                    "stroop",
                    "aroma",
                    "suiker",
                    "caramel",
                    "karamel",
                    "glucose",
                    "demerara",
                    "dextrose",
                    "diksap",
                    "eindmelasse",
                    "fruitextract",
                    "fructose",
                    "gula" ,
                    "hfcs",
                    "honing",
                    "kandij",
                    "lactose",
                    "maltose",
                    "maple Syrup",
                    "melasse",
                    "molasses",
                    "moutextract",
                    "muscovado",
                    "oerzoet",
                    "panocha",
                    "panela",
                    "piloncillo",
                    "poedersneeuw",
                    "rapadura",
                    "rietsap",
                    "saccharose",
                    "sacharose",
                    "sucanat",
                    "sucrose",
                    "treacle",
                    "trehalose",
                    "turbinado",
                    "vruchtenextract"]

        self.sugar_amount_list = [("karamel", 66),
                             ("honing", 82),
                             ("poedersuiker", 99),
                             ("basterdsuiker", 97),
                             ("kristalsuiker", 100),
                             ("fijnekristalsuiker", 100),
                             ("limonadesiroop frambozen", 0),
                             ("fruitstroop rinse appel", 55.8),
                             ('fijne suiker', 100),
                             ('wittebasterdsuiker', 99),
                             ('vanillesuiker', 98),
                             ("roomboter ministroopwafels", 29),
                             ('roomijs pecankaramel', 29),
                             ("suiker", 100),
                             ("chocoladesuikerparels",),
                             ("fijne tafelsuiker", 100),
                             ('rietsuiker', 100),
                             ('suikerriet', 100),
                             ("donkere basterdsuiker", 99),
                             ('gember', 57.7),
                             ("lichtbruinebasterdsuiker", 99),
                             ("stroopwafel", 31),
                             ("karamelschenkstroop", 80),
                             ('vloeibare honing', 82),
                             ("basterdsuiker", 99),
                             ("appelstroop", 55.8),
                             ('fruitcocktail op siroop', 12),
                             ("schenkstroop", 80),
                             ("melkchocolade", 49),
                             ('suikerwafels', 21),
                             ("zeeuwse keukenstroop", 82),
                             ("keukenstroop", 82),
                             ('geleisuiker', 99),
                             ("bruine kandijsuike", 100),
                             ("bloemenhoning", 80.5),
                             ("appeldiksap", 6),
                             ("kokosbloesemsuiker", 87),
                             ("nectarines", 9.8),
                             ("diksap appel", 6),
                             ("saroma banaan", 73),
                             ("aardbeienlimonadesiroop", 6.8),
                             ("gember op siroop", 70),
                             ("rinse appelstroop", 57),
                             ("stemgember op siroop", 70),
                             ('stroop', 57),
                             ("stroopwafeltje", 31),
                             ("suikerbrood", 33),
                             ("vloeibare", 80.5),
                             ("bosbessen op lichte siroop", 15),
                             ("frambozensiroop", 6.7),
                             ("bosvruchtensiroop", 6),
                             ("perenpartjes op siroop", 13),
                             ("donkerebasterdsuiker", 99),
                             ("donkerbruinebasterdsuiker", 99),
                             ("poedersuikeruitstrooibus", 99),
                             ("fijnesuiker", 100),
                             ("crème brûlée", 18),
                             ("voila rolfondant wit", 85.3),
                             ("bruine suiker", 100)

                                  ]

        self.units = [("vanillesuiker","zakjes", 8),
                      ("suiker", "eetlepels", 11),
                      ("suiker", "el", 11),
                      ("suiker", "tl", 1.5),
                      ("honing", "ml", 0.8),
                      ("poedersuiker", "eetlepels", 10 ),
                      ("poedersuiker", "el", 10),
                      ("poedersuikeruitstrooibus", "eetlepels", 10),
                      ("rietsuiker", "eetlepels", 11),
                      ("wittebasterdsuiker", "el", 11),
                      ("wittebasterdsuiker", "eetlepels", 11),
                      ("keukenstroop", "el", 10),
                      ("vanillesuiker", "zakje", 8),
                      ("honing", "eetlepel", 12),
                      ("honing", "el", 12),
                      ("vloeibarehoning", "el", 12),
                      ("vloeibarevanillehoning", "eetlepel", 12),
                      ("aardbeienlimonadesiroop" , "eetlepels",12 ), #fix
                      ("limonadesiroopframbozen", "el",12),   #fix
                      ("poedersuikeromtebestrooien", "el", 10),
                      ("lichtbruinebasterdsuiker", "el", 11),
                      ("bruinebasterdsuiker", "el", 11),
                      ("bruinebasterdsuiker", "theelepels", 1.5),
                      ('Zeeuwsekeukenstroop','el', 10),
                      ("suikerwafels", '', 1),
                      ("schenkstroop", "eetlepels", 8),
                      ("schenkstroop", "ml", 1)]


    def amount_of_sugar(self,y):        #kitchen measurement unifing and calculate the amount of sugar in the different soort of sweeteners
        """every 100gram have x             x = stander_amount of sugar     y = the amount of the element in the recipe
        every y gram have z                   z = the amount of sugar in the amount of the element"""
        sugar_tuple = ()
        z = 0
        if "g" in y[2]:
            for w in self.sugar_amount_list:
                if w[0] == y[0]:
                    z = (int(y[1]) * w[1]) / 100
        else:
            for i in self.units:
                if y[0] == i[0] and y[2] == i[1]:
                    sugar_tuple = (y[0], int(y[1])*i[2])
            for w in self.sugar_amount_list:
                #print(sugar_tuple, "tup")
                if w[0] == sugar_tuple[0]:
                    z = (sugar_tuple[1] * w[1]) / 100
        return z
