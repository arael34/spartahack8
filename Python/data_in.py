latest_temp = 0
latest_soundlevel = 0

def main():
    import serial
    import time
    from twiliomessage import check_temp

    arduinoData = serial.Serial('COM7', 9600)
    while True:
        if arduinoData.inWaiting() > 0:
            line = arduinoData.readline().decode("utf-8")
            # print(line) # for debugging
            lines = map(float, line.split('\n\n'))
            for l in lines:
                n = l.split()
                latest_temp = n[0]
                latest_soundlevel = n[1]
                check_temp(latest_temp)
        time.sleep(1)

def get_temp():
    return latest_temp

def get_soundlevel():
    return latest_soundlevel

if __name__ == '__main__':
    main()
