import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)
    print("""
                                  ,@                 @.                             
                         @,,,*****,,,@@@@@@@,,,/****,,,@                        
                       @**************,@,@,*************#@                      
                         ,,,&@**********@**/*******@%,,,.                       
                     @ . .    .,,@@@*****//**@@@,,.        #                    
                     ,              ,,,,@,,,,                                   
                      @.               @,@                @                     
                     @,,@&           @/,,,&@           @@,,@                    
                @@,,,,,,,,,,@@@@@@/,,,,,,,,,,,(@@@@@@,,,,,,,,,,@@               
              @,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@             
             @,,,,@@,,,,,,.,,,,,,,,,,,,,,...,,,,,,,,,,,,,,,,,@@,,,,@            
            @,,,@.,  ,.@@,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,@@..  ,.@,,,@           
            *,,,@%        @,@@@@@@/,,,,,,,,,,,/@@@@@@,@        &@,,,%           
           ,.,,,.&       @,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@       @,,,,*           
            @,,,,,,,&&.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.&&,,,,,,,@           
            /.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(.           
              @,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@             
                @,,,,,,,,.,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,.,.,,,,@               
                   @@,,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..@@                  
                   @(/(#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/(((@                  
                   @((((/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@((((@                  
                 . @((&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(((@                  
            ,@,,,,,@*@((**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**((@*@,,,,,@            
           @,,************,/***,,,,,,,,,,,,,,,,,,,************/****,,@          
           @***@((@***,**,**************,,*,******************@((#***@          
            @((@//****@*********************************,/@**/***@((@           
             @((/*****@*******/@@ ..............@@********@/*****((@            
     @@       @******@****/*@.......................@******@/****/@       @@    
     @****/%@@@@(****@*****@.........................#*****@/***@@@@@#*****@    
  @@@****************@*****@.,,.....................,@*****@****************@@@ 
.*********//*********&******@@@............,,....,@@@******@*****************/,%
    /@@*/********/@****///,,,@                     @*****,,,,#@***********@@*   
    @,***@@@  @@**************#@                 @,*************/@@  @@@****@   
            //*******************@             @*******************%.           
                    @****@                             @****@                   
                    @***,*                             %****@  
                    
    
 _____            _         _____  ______    _____       
/  __ \          | |       |  _  | |  ___|  |  _  |      
| /  \/_ __ _   _| |_ _ __ | |/' | | |_ _ __| |/' | __ _ 
| |   | '__| | | | __| '_ \|  /| | |  _| '__|  /| |/ _` |
| \__/\ |  | |_| | |_| |_) \ |_/ / | | | |  \ |_/ / (_| |
 \____/_|   \__, |\__| .__/ \___/  \_| |_|   \___/ \__, |
             __/ |   | |                            __/ |
            |___/    |_|                           |___/ 

I'm a frog QUACK! I make you rich by trading cryptos
v.0.01 written by @lonaya

    """)
    binance = BinanceClient("",
                            "",
                            testnet=True, # change this to let the  bot trade with real Money
                            futures=True)
    bitmex = BitmexClient("",
                           "",
                          testnet=True) # currently doesn't work

    root = Root(binance, bitmex)
    root.mainloop()
