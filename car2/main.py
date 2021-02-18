import speech_recognition as sr
import pyttsx3
import pygame

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#def take_command():
    #try:
    #    with sr.Microphone as source:
     #       print('listening...')
    #        voice = listener.listen(source)
     #       command = listener.recognize_google(voice)
      #      command = command.lower()
    #except:
     #   pass
    #return command


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'take the command' in command:
                command = command.replace('take the command', '')
    except:
        pass
    return command

pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 150
car_y = 300
focal_dis = 25
direction = 'up'
drive = True
clock = pygame.time.Clock()
def run_car():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    take_the_command = take_command()
    if take_the_command == 'right':
        if direction == 'up':
            direction = take_the_command
            car = pygame.transform.rotate(car, -90)
            car_x = car_x + 2
        elif direction == 'down':
            direction = take_the_command
            car = pygame.transform.rotate(car, 90)
            car_x = car_x + 2
    elif take_the_command == 'left':
        if direction == 'up':
            direction = take_the_command
            car = pygame.transform.rotate(car, 90)
            car_x = car_x - 2
        elif direction == 'down':
            direction = take_the_command
            car = pygame.transform.rotate(car, 90)
            car_x = car_x - 2
    if take_the_command == 'stop':
        direction = 'stop'

while True:
    run_car()











    window.blit(track, (0, 0)) # blit -> Block Image Transfer
    window.blit(car, (car_x, car_y))  # (150,300) -> initial position
    #pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
