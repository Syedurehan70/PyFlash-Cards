# PyFlash-Cards

It's a Flash Card Project, which displays french words first than displays their english meanings after 3 sec of delay, you can check which words you know and cross whichever 
word you think you want to learn.

First we setup a TKinter window, positioned the buttons and canvas accordingly on the screen, makes image objects.

There are some functions:

flipping: we create a window.after delay before executing it, once it's executed it replaces title of 'French" with 'English' and also replace the french word with english 
word, delay is usually of 3 sec, and also put back_img on canvas in place of front_img.

save: save basically gets executed when we click exit button on screen, it takes the word_dict_list which doesn't have those words which we've already learned, only
consist those which need to be learned, and through pandas lib save it in words_to_learn.csv in a form of DataFrame.

known_words: It triggers when we click check mark, it checks the length of word_dict_list, 
if not zero than removes the word which was displayed on screen last, and call unknown_words, 
if length is zero it simply displays welldone in title and you've learned it all in words section.

unknown_words: It triggers when we click cross on screen, and also called it in known_words and right after setting up the window.
It checks the length of word_dict_list, 
if not zero choose a random french word from it and displays on it screen, also called flipping function inside it at an interval
of 3 sec, 
if it's zero than displaying a same well done message.
