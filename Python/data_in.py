latest_temp = 0.
latest_soundlevel = 0

def main():
    import serial
    import time
    import re
    from twiliomessage import check_temp

    arduinoData = serial.Serial('COM7', 9600)
    while True:
        if arduinoData.inWaiting() > 0:
            block = arduinoData.readline().decode("utf-8")
            # print(line) # for debugging
            nums = re.sub(r'[\n\r]+', ' ', block).split()
            t = True
            for num in nums:
                if t:
                    latest_temp = float(num)
                    check_temp(latest_temp)
                else:
                    latest_soundlevel = int(num)
                t = not t
        time.sleep(1)

def get_temp():
    return latest_temp

def get_soundlevel():
    return latest_soundlevel

if __name__ == '__main__':
    main()
