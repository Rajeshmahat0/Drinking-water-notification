import time

from plyer import notification

if __name__ == "__main__":
    while True:
     notification.notify(
        title = "⏰ Time to Hydrate!",
        message = "Drinking water has numerous benefits. Water is crucial for many body functions, such as lubricating the joints, delivering oxygen throughout the body, preventing kidney damage, and more.",
        # app_icon = "C:\Users\rm713\live server\python\python_project\icon.ico", icon not working
        timeout = 5
    )
     time.sleep(60*60)


#   to run python programme in background enter the below text in python
#      pythonw.\main.py






