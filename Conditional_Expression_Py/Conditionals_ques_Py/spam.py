# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

string = "they make a lot of money buy selling this product so click this and buy now help them make more money also subscribe this for future notification."
# we can also take this message as in input.

if("make a lot of money" in string or 
   "buy now" in string or 
   "subscribe this" in string or 
   "click this" in string):
    print("Spam text is present in the string")
else:
    print("Spam text is not present")