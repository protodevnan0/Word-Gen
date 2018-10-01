import random;

print (" Word Gen Test");
print (" ");

word = "word" # Which word are You trying to generate?
word_try = ""; # Stores Your generated letters as a word
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]; # Alphabet, we should add upper case and numbers soon, but it will slow down a lot our generator, so we have to redesign everything lol
attempts = 0; # Number of generated words

while True: # Loops generating new words until they match word
 word_try = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters); # One random.choice(letters) equals one letter in Your word
 attempts += 1;
 print (" Current word: " + str(word_try) + " Amount of retries: " + str(attempts));
 if (word_try == word):
  break;

#
#  To-do list
#
#
#  Stop code from generating previous words (might reduce performance?)
#  Automatic letter count detection
#  Redesign code
#  Modify the code so that it can be run with CUDA. (It should increase performance a lot)
#
#  Note: The shorter the word, the faster it will be generated.
