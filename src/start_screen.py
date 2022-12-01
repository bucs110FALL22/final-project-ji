import Tools 
class Start_screen: 
    def __init__( self, display:Display) -> None:
    '''
    object containing display info
    '''
    self.display = display
    self.init
    def treatimage(self): 
    image = Assets.images.get('treat')
    image_width = self.display.width / 4
    image_height = self.display.height / 4
    self.welcome_image = Image(image_file, image_width, image_height)


    def draw(self):
        '''
        Draws the welcome screen.
        '''
        self.draw_game_title()
        self.draw_welcome_character()
        self.display_instructions()

    def draw_game_title(self):
        '''
        Draws the app title
        '''
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height / 2

        text = 'Treat Run'
        font_size = 100
        Tools.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press SPACE to start'
        font_size = 50
        Tools.print(surface, text, font_size, (x_text, y_text))

    def display_instructions(self):
        '''
        Prints the game instructions on the screen.
        '''
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height - 140

        text = 'Avoid the dogs and catch as many tennis balls as you can!'
        font_size = 20
        Tools.print(surface, text, font_size, (x_text, y_text))

        
    def draw_welcome_character(self):
        '''
        Draws the main character in the screen.
        '''
        surface = self.display.surface
        x_image = self.display.width / 4
        y_image = self.display.height / 4
        self.welcome_image.draw(surface, x_image, y_image)
