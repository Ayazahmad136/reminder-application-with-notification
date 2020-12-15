import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title ='incomplete work',
            message='the excel sheet you were making is still incomplete..please make it complete',

            # displaying time
            timeout =10
        )

        # waiting time
        time.sleep(60*60)

# to run this notification in background open terminal and type pythonw.exe -\main.py