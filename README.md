# Morse Code Converter
[This script](https://github.com/taishi-nammoto/morse-code-GUI-/blob/main/main.py) allows you to convert text to morse codes and make sound signals.
<img src="https://github.com/taishi-nammoto/morse-code-GUI-/blob/main/Data/sample_img.png">

# Task Details:
With the help of this particular data set you have to build ***a recommended engine***. And your recommended engine will return maximum 10 movies name if an user search for a particular movie.


Recommended engine generally in three types <br>
***1.content Based recommended engine*** <br>
2.collaborative recommender engine <br>
3.hybrid recommended engine


# Goal Details:
Recommended engine must return 5 movie names and maximum it can return 10 movie names if an user search for a particular movie. This recommender engine should not give suggestion in between 1 to 4 and 6 to 10 it have to return 5 movie names for 10 movie names.


# Data source
https://www.kaggle.com/shivamb/netflix-shows



## Example 
By using tkinter, a GUI displays a window below. <br>
<img src="https://github.com/taishi-nammoto/morse-code-GUI-/blob/main/Data/sample_img.png" width="600">

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

## License
[MIT](https://choosealicense.com/licenses/mit/)
