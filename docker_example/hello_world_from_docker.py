import datetime
from time import sleep

import pandas as pd

print("Hello world from Docker!!!")

while True:
    df = pd.DataFrame(
        data={
            "timestamp": [datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7)],
            "col2": [3, 4],
        }
    )
    # print(datetime.datetime.now())
    print(df)
    sleep(1)


# docker run --rm -d -p 8010:8008 --name quizez_cont quizez
# docker build -t quizez .

# docker run --rm -d -p 8010:8008 -v D:\Hillel\quizez\quizez\src:/quizez --name quizez_cont quizez

# docker run --rm -d -p 8010:8008 -v D:\Hillel\quizez\quizez:/quizez --name quizez_cont quizez ./commands/start_server.sh
