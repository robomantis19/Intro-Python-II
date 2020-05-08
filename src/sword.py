import pyglet


start = pyglet.resource.media('item.wav', streaming = False)
sword = pyglet.resource.media('swordHit.wav', streaming = False)
magic = pyglet.resource.media('magic.wav', streaming = False)
loop = True
# music.play()
count = 0
while loop == True: 
    if count == 0 or inputs == 'h' or inputs =='help': 	
        start.play()
        print('\n--------------------\n\nAttack directions, for magic: press r key | for sword: press f key | \n\n  ')
    count += 1
    
    inputs = input("\n\n--->  ")
    if inputs == 'r': 
        
        sword.play()
    if inputs == 'f':
        magic.play() 

        
        

