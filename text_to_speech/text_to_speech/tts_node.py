import rclpy
from rclpy.node import Node

from std_msgs.msg import String

#from gtts import gTTS
#import os
#from playsound import playsound
# import pygame

import pyttsx3
# espeak is required for this, sudo apt install espeak

class VoiceSubscriber(Node):

    def __init__(self):
        super().__init__('voice_subscriber')
        self.subscription = self.create_subscription(
            String,
            'voice',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.converter = pyttsx3.init() 
        self.converter.setProperty('rate', 150) 
        # Set volume 0-1 
        self.converter.setProperty('volume', 0.7) 

        # self.converter.setProperty('voice', 'norwegian')
        self.converter.setProperty('voice', 'english')

    def listener_callback(self, msg):
        # myobj = gTTS(text=str(msg.data), lang='en', slow=False)
        # myobj.save("speech.mp3")
        
        # pygame.mixer.init()
        # pygame.mixer.music.load("speech.mp3")
        # pygame.mixer.music.play()
        
        # while pygame.mixer.music.get_busy() == True:
        #     continue
        
        self.converter.say(str(msg.data))
        self.converter.runAndWait()
        



def main(args=None):
    rclpy.init(args=args)

    voice_subscriber = VoiceSubscriber()

    rclpy.spin(voice_subscriber)

    voice_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()