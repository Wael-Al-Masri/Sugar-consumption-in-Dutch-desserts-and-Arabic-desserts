# Sugar-consumption-in-Dutch-desserts-and-Arabic-desserts
Our code uses qualitative and quantitative methods to find the amount of sugar used in Dutch desserts and Arabic desserts.
Our program contains 4 classes, which are:
- Class arabic_data_scrapper:
In this class, we loop through every page of a specific URL and save all the page's URL in a list. Next, the code loop through the URL list, and save the title, ingredients and the servings of every recipe in the website. Finally, export all the collected information as an excel file.
- Class main:
This class has 5 functions:
* Function find_sugar: in this function, we loop through the ingredients column and find all sort of sweetener has been used in the recipe. And this process is done by comparing every ingredient with a pre-made sweeteners list in the class(sugar_lists) if any exist save it in a new list.
* Function find_linked_recipes: in this function, we loop through both databases the Dutch one and the Arabic one. If the number in the  Linking ID column has been matched print( in our case we print the title, but it can bee changed to other things like the following:  (sheeto.cell_value(i, 1) replace the one with : 0, so it will print the linking ID.
                                                1 the title of the recipe
                                                2 the ingredients
                                                3 the serving
                                                4 the URL)
* Function find_none_repetitive_sugar_list: it will loop through the ingredients column through every recipe's ingredients and whenever a new sort of sweetener has been found it will check the list if it's not in the list it will be added. And by this, we will have a list containing all the different sorts of sweeteners used in the whole database without replication.

* Function write_into_excel: which simply write the results in excel file.
* Function Main: will open the database and call the other functions.
- Class sugar_lists:
 In this class we have 3 very important lists which are:
 * sweeteners_list: in this list, we tried to add all possible name of sweetener used in desserts in order to be able to find a match from this list with an ingredient in the ingredients list.
* sugar_amount_list: in this list made a tuple, and in every tuple, we have as the first element the name of sweetener and the second element is the amount of sugar in this sweetener per 100gram. And by comparing the founded sweetener with the first element of the tuples in the list, we can calculate how much sugar in the sweetener regarding its amount in the recipe.
* units list: it contains tuples of three elements. The first element is the name of the sweetener. The second element the potential used unite in measuring while preparing the recipe. The third element is the number of grames of this sweetener in the unite used. For example 
("suiker", "eetlepels", 11) every eat spoon of sugar contains 11 gram, and by looping in the founded sugar list, we can replace every spoon of sugar with 11gram.
And at the end of this class, we have a function where it loops through the founded sugar and unify the measuring unites used, calculate the amount of sugar in the different sweeteners.
- Last Class is ingredients_cleaner:
This class will loop through the final founded sugar list and clean the content form punctuation and brackets. And sum all the amount of sugar in the recipe in order to be compared.
