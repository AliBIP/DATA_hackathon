import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


data_str = """Device Information	OS	Severity Level					
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Android	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Android	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Android	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Android	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Android	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Android	High			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Android	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	High			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Linux	Low			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Opera	Linux	High			
Opera	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Android	High			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	Medium			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Android	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Android	High			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	High			
Opera	Windows	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Android	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Opera	Linux	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Android	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Android	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Android	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Android	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Opera	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Opera	Linux	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Opera	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Android	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Android	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Android	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Linux	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Android	Medium			
Mozilla	Windows	High			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Linux	High			
Mozilla	Windows	Low			
Mozilla	Android	Medium			
Opera	Linux	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Android	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Opera	Windows	Low			
Opera	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Linux	High			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Mozilla	Linux	Low			
Opera	Linux	High			
Opera	Windows	High			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Opera	Linux	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	High			
Mozilla	Linux	High			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Windows	High			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Android	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Opera	Linux	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Windows	Low			
Opera	Linux	Low			
Opera	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Linux	Medium			
Mozilla	Android	Medium			
Mozilla	Linux	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	High			
Opera	Windows	Low			
Mozilla	Windows	Low			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Android	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Opera	Windows	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	High			
Mozilla	Windows	Low			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Opera	Linux	High			
Mozilla	Windows	High			
Mozilla	Android	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Medium			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	High			
Mozilla	Android	Low			
Opera	Windows	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Android	Low			
Opera	Linux	Medium			
Mozilla	Windows	Low			
Opera	Linux	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	High			
Opera	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Medium			
Mozilla	Linux	High			
Opera	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Low			
Opera	Linux	High			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	High			
Mozilla	Mac OS	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Linux	High			
Mozilla	Linux	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	Low			
Opera	Linux	Low			
Opera	Windows	Low			
Mozilla	Linux	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Medium			
Opera	Windows	Medium			
Mozilla	Mac OS	High			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Low			
Opera	Linux	Medium			
Mozilla	Windows	High			
Mozilla	Windows	High			
Mozilla	Windows	High			
Opera	Windows	Medium			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Medium			
Opera	Linux	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Windows	Low			
Mozilla	Mac OS	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	Medium			
Opera	Linux	High			
Mozilla	Windows	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Windows	High			
Mozilla	Linux	Low			
Mozilla	Mac OS	Low			
Mozilla	Linux	High			
Mozilla	Mac OS	Low			
Mozilla	Linux	Low			
Opera	Linux	Medium			
Mozilla	Linux	Low			
Mozilla	Windows	High			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Opera	Windows	Low			
Mozilla	Windows	Medium			
Mozilla	Linux	Medium			
Mozilla	Mac OS	Medium			
Opera	Linux	Low			
Mozilla	Mac OS	Medium			
Mozilla	Mac OS	Low			
Opera	Windows	Low			
Mozilla	Windows	Low			
Mozilla	Mac OS	Medium			
Mozilla	Windows	Medium			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Opera	Windows	High			
Mozilla	Windows	High			
Mozilla	Mac OS	Medium			
Mozilla	Windows	High			
Mozilla	Windows	Low			
Mozilla	Linux	Low			
Mozilla	Mac OS	Medium			
"""

data = pd.read_csv(io.StringIO(data_str), sep='\t')


print(data.head())


print(data.info())


print(data.describe())


sns.countplot(x='Severity Level', data=data)
plt.show()


sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()