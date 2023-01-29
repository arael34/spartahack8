def main():
    import serial
    import time
    import re
    from twiliomessage import check_temp

    global latest_temp
    global latest_soundlevel

    arduinoData = serial.Serial('COM7', 9600)
    while True:
        if arduinoData.inWaiting() > 0:
            block = arduinoData.readline().decode("utf-8")
            nums = re.sub(r'[\n\r]+', ' ', block).split()
            t = True
            for num in nums:
                if t:
                    latest_temp = float(num)
                    check_temp(latest_temp)
                else:
                    latest_soundlevel = int(num)
                t = not t

if __name__ == '__main__':
    main()
