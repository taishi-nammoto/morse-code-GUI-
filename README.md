# Morse Code Converter
[This script](https://github.com/taishi-nammoto/morse-code-GUI-/blob/main/main.py) allows you to convert text to morse codes and make sound signals.

## Example 
By using tkinter, a GUI displays a window below.
![window](https://github.com/taishi-nammoto/morse-code-GUI-/blob/main/Data/sample_img.png)

## Dataset
[Data Scraping](https://github.com/taishi-nammoto/morse-code-GUI-/blob/main/data_scraping.ipynb) gets morse codes and saves a CSV file. 

## Installation 
import the following modules
```
from tkinter import *
import pandas as pd 
from pydub import AudioSegment
from pydub.playback import play
import time
```
