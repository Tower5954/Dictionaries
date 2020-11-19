programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
   "Function": "A piece of code that you can easily call over and over again.",
}

#Adding new items    
programming_dictionary["loop"] = "The action of doing something over and over again"

#Create an empty dictionary  
empty_dictionary = {}

#Wipe an existing dictionary  
# programming_dictionary = {}

#edit an item in a dictionary  
programming_dictionary["Bug"] = "A moth in your computer"

#loop through a dictionary  
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])