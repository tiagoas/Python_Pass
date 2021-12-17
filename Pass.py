import random
import string
import pyfiglet


from pyfiglet import Figlet
word = pyfiglet.figlet_format("Tiago7w_ Pass")
print(word)



size = 10   
   
                                                
chars = string.ascii_letters + string.digits + '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~.'


rnd = random.SystemRandom()


print(''.join(rnd.choice(chars) for i in range(size)))
