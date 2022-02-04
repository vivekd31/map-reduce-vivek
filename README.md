# map-reduce-VivekDrakshapally
This is practice for map and reduce

## Vivek-Drakshapally-beer costs at mlb stadiums
## Dataset
Link: [Raw Dataset](https://www.kaggle.com/yamqwe/2018-w43-the-cost-of-a-beer-at-mlb-stadiumse)

## About Data:
The data I have used consists cost of Beer at mlb stadium by Year,City.

## Study:
- For this Dataset, I want to find out the sum of Beer prices at different mlb team stadiums.

## Findings:
By using mapping and reducing scripts I have processed the data of 1087 cells to 63 cells which shows different Teams and sum of beer prices at their respective stadiums.
By Analzying the sorted data we came to know that Chicago cubs baseball team beer price is the highest with 38.75 and Arizona Diamondbacks baseball team beer price is the lowest with 20.

## Powershell Command:
- ***cat mlb_prices.csv | python 03mapper.py | python 03sorter.py | python 03reducer.py > VIVEKoutput.txt***

## Summary:
- By examining the final output, I can Conclude that the minimum sum of beer price is 20 and the highest is 38.75.


![image](https://github.com/vivekd31/map-reduce-vivek/blob/main/OutputImage1.png)



