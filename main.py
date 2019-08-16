import tkinter as tk
from world import MainWorld
from time import sleep

def main():
    mainWorld = MainWorld(440, 640, 120, 120, 5)

    mainWorld.drew_main(20, 30)
    mainWorld.run_show()
    pass

if __name__ == "__main__":
    main()
