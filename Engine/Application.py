import arcade
from Engine.EntityManager import *
from Engine.InputManager import *
from Engine.SceneManager import *


class Application(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Application',color:str = arcade.color.BLACK):
        super().__init__(width, height, title)
        self.inputManager = InputManager()
        self.sceneManager = SceneManager()
        self.deltaTime = 0
        arcade.set_background_color(color)

    def update(self, deltaTime: float):
        self.deltaTime = deltaTime
        entityManager = self.sceneManager.getCurrentScene().entityManager
        entityManager.firstUpdate()
        entityManager.update()
        entityManager.lateUpdate()
        self.inputManager.clearKeys()

    def on_draw(self):
        # Esto siempre es lo primero
        arcade.start_render()
        # Todo lo otro después
        self.sceneManager.getCurrentScene().entityManager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.inputManager.keyPressed(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        self.inputManager.keyReleased(symbol)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.inputManager.mousePos = (x,y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 4:
            button = 1
        elif button == 1:
            button = 0
        self.inputManager.mousePressed(button)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == 4:
            button = 1
        elif button == 1:
            button = 0
        self.inputManager.mouseReleased(button)


    def run(self):
        if self.sceneManager.init():
            arcade.run()
        else:
            print("No scenes found")
            exit()

    def exit(self):
        arcade.close_window()