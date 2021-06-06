import eel
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import time
#import bstrap as bs
import sqlite3
import configparser
import math

eel.init('web')
done = False
con = sqlite3.connect("taro.db")
cur = con.cursor()

@eel.expose
def add_entry():
    return

eel.start("index.html", size=(200,700)) #
