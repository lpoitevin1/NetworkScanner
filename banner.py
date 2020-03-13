import os 
import time 
  


class Banner:
    def __init__(self):
        #You can change the width of the display according to your wish. 
        self.WIDTH = 100
        
        # Written below currently is GeeksForGeeks. If you wish to get more 
        # written, you have to add each alphabet manually. 
        self.message = "john doe".upper() 
        
        #The message will get printed here. 
        self.printedMessage = [ "","","","","","","","","","","","","","", ] 


        self.characters = {
                " " : [ " ", 
                        " ", 
                        " ", 
                        " ", 
                        " ", 
                        " ", 
                        " " ], 

                'J':['*******',
                    '   *   ',
                    '   *   ',
                    '*  *   ',
                    ' ***   ',],

                'O':['*******',
                    '*     *',  
                    '*     *',
                    '*     *',
                    '*******'],
                
                'N':['**    *',
                    '* *   *',
                    '*  *  *',
                    '*   * *',
                    '*     *'],
                
                'H':['*     *',
                    '*     *',
                    '*******',
                    '*     *',
                    '*     *'],


                'D':['*****  ',
                    '*    * ',
                    '*     *',
                    '*    * ',
                    '*****  '],


                'E':['*******',
                    '*      ',
                    '****   ',
                    '*      ',
                    '*******',       
                    ]
            }

    def start(self):
        for row in range(5): 
            for char in self.message: 
                self.printedMessage[row] += (str(self.characters[char][row]) + "  ") 

        offset = self.WIDTH 
        while True: 
            os.system("clear") 

            for row in range(7): 
                print(" " * offset + self.printedMessage[row][max(0,offset*-1):self.WIDTH - offset]) 

            offset -=1

            if offset <= ((len(self.message)+2)*6) * -1: 
                offset = self.WIDTH 

            #Use this to change the speed of the animation that you wish to keep. 
            time.sleep(0.001) 



b = Banner()
b.start()