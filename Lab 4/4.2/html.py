class HTML:

    def web_page(ledStatus):
        
        if self.ledStatus == 0:
            led_state="OFF"
        else if self.ledStatus == 1:
            led_state="Blinking"
        else:
            led_state="Alternating"
        

        html = """
        <html>
        <head>
        <title>ESP Web Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>
        
            html{
                font-family: Helvetica;
                display:inline-block;
                margin: 0px auto;
                text-align: center;
            }
    
            h1{
                color: #0F3376;
                padding: 2vh;
            }
            
            h3{
                color: #367BF5;
            }
            
            p{
                font-size: 1.1rem;
                color: #5e96f8;
            }
            
            .button{
                display: inline-block;
                border: none; 
                border-radius: 4px;
                text-decoration: none;
                font-size: 16px;
                margin: 2px;
                cursor: pointer;
                width: 200px;
                height: 50px;
            }
            
            .button1{
                color: white;
                background-color: #367BF5;
            }
            
            .button2{
                color: #367BF5;
                background-color: #E6EFFF;
            }
            
        </style>
        </head>
        <body>
            
            <h1>ESP32 Web Server</h1>
            <h3> A simple demonstration to control LED sequence using Access Point(AP) Mode </h3>
            <p>LED Status: <strong>""" + led_state + """</strong></p>
            <a href="/?led=blink"><button class="button """ + {True: "button1", False: "button2"} [ledStatus == 1] +""" "><strong>Blink LED<strong></button></a>
            <a href="/?led=alt"><button class="button """ + {True: "button1", False: "button2"} [ledStatus == 2] +""" "><strong>Alternate LED<strong></button></a>
            <a href="/?led=off"><button class="button """ + {True: "button1", False: "button2"} [ledStatus == 0] +""" "><strong>Turn OFF<strong></button></a>
        </body>
        </html>

        """

        return html
