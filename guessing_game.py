secret = 35
guess = int(input ('Guess number: '))
if guess == secret:
    print (f'You are right the number is {secret}')
elif guess < secret:
    print ('Number you put was too low')
else:
    print ('Number you put was too high')