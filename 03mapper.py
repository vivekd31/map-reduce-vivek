# Mapper

import sys 


for line in sys.stdin:
  datalist = line.strip().split(",")

  if (len(datalist) == 5) : 
    Year,Team,Nickname,City,Price = datalist

    print(Team,"\t",Price)