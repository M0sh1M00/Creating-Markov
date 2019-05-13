# Creating-Markov
Create your own wacky sentences with an input

How it works:

This is the File:

This is some text.\n
It can be whatever i want!\n
i hope the text is good.\n
if it is not then i will be unhappy!\n
how are you feeling today because i am feeling good with this!\n
this is because my machine is epic!\n
yes, you read that right, it is epic.\n
i am a communist!\n

Step1: Picks a random word that is the start of a line

Step2: Uses Markov theory to determine the next word. Essentially if the first word is 'i' then it will search for all possible words that happen after i, such as 'will', 'want!', 'am' and 'hope'. However since 'am' appears twice after 'i' it will have double the chance of being chosen as the next letter

Step3: Repeat Step2 until a word at the end of a line is reached

Step4: Does the same as Step2 with the addition of a chance to end the word chain, if that chance happens then the program is terminated

Step5: Push enter to go back to Step1
