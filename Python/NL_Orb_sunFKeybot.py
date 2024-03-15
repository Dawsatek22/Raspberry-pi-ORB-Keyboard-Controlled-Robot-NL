     #deze code is vertaald in nederlands.
#deze code is bedoeld (het is niet noodzakelijk  ) om met de onderdelen van  Openroboticsplatform(orb) te gebruiken. meer info hier : https://openroboticplatform.com/
#en de : SunFounder Robot HAT Expansion Board Designed for Raspberry Pi. documentatie voor is in deze link : https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/# 
# also it is ment to use with VNC Viewer. more info in this link :https://www.realvnc.com/en/connect/download/viewer/   


import pygame # Voor keyboard besturing meer als je de library niet hebt hier is meer info :https://www.pygame.org/
from time import sleep

# Import Motor class
from robot_hat import Motors

# Create Motor object
motors = Motors()
motors.set_left_id(1) #Set de linker motor.
motors.set_right_id(2)#Set de rechter motor.
#!Waarschuwing ik weet niet waarom maar de  motors."richting"() command zijn omgekeert (je  kan het veranderen als je wilt. ).

#zorg dat de Keyboard gaat werken.
pygame.init()
window = pygame.display.set_mode((300,300))
pygame.display.set_caption("Pygame Demonstration")

   

    
    

mainloop=True
while mainloop:

    pygame.time.delay(100)
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            mainloop=False

        pressed = pygame.key.get_pressed()
        buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
        print(buttons)  # print list to console
     
            
        if pressed[pygame.K_s]: # s key stopt de robot
            
            motors.stop()
            print("s = stop")
            sleep(0.1)
           
           
        
        if pressed[pygame.K_f]: # f key rijd de robot naar voren.
            
            motors.turn_right(100)
            sleep(0.1)
            motors.stop()
            print("forward")
        if pressed[pygame.K_b]: # b key rijd de robot acteruit.
            
            motors.turn_left(100)
            sleep(0.1)
            motors.stop()
            print("backwards")
          
        if pressed[pygame.K_l]: # l key rijd de robot links.
            
            motors.backward(100)
            
            sleep(0.1)
            motors.stop()
            print("left")
        if pressed[pygame.K_r]: # r key rijdt de robot rechts.
            
            motors.forward(50)
            sleep(0.1)
            motors.stop()
            print("right")
        if pressed[pygame.K_1]: # 1 key rijd de rechts vooruit.
            
            motors.turn_right(100)
           
            sleep(1)
            motors.backward(50)
            sleep(0.1)
            motors.stop()
            print("right forward ")
        if pressed[pygame.K_2]: # 2 key rijdt de robot  links vooruit .
            
            motors.turn_right(100)
           
            sleep(1)
            motors.forward(50)
            sleep(0.1)
            motors.stop()
            print("left forward ")
        
        if pressed[pygame.K_3]: # 3 key rijdt de robot links achter. 
            
            motors.turn_left(100)
           
            sleep(1)
            motors.forward(60)
            sleep(0.1)
            motors.stop()
            print("left backwards ")
        
        if pressed[pygame.K_4]: # 4 key rijd de motor rechts achteruit. 
            
            motors.turn_left(100)
           
            sleep(1)
            motors.backward(60)
            sleep(0.1)
            motors.stop()
            print("right backwards ")
            
                              

pygame.quit()                
