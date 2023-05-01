class HTML:
    def __init__(self, ledBlue):
        self.ledBlue = ledBlue

    def web_page(self):
        
        if self.ledBlue.value() == 1:
            gpio_state="ON"
            gpio_prompt = "OFF"
        else:
            gpio_state="OFF"
            gpio_prompt = "ON"

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
            
            p{
                font-size: 1.1rem;
                color: #66638d;
            }
            
        .button{
            display: inline-block;
            border: none; 
            border-radius: 4px;
            text-decoration: none;
            font-size: 24px;
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
            <h3> A simple demo using Access Point(AP) Mode </h3>
            <p>Blue LED Status: <strong>""" + gpio_state + """</strong></p>
            <a href="/?led=""" + {True: "off", False: "on"} [gpio_state == "ON"] + """"><button class="button """ + {True: "button1", False: "button2"} [gpio_state == "ON"] +""" ">Turn it <strong>""" + gpio_prompt + """<strong></button></a>
        </body>
        </html>

        """

        return html