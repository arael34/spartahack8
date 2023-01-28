def main():
    import serial
    import time
    from twiliomessage import check_temp

    arduinoData = serial.Serial('COM7', 9600)
    while True:
        if arduinoData.inWaiting() > 0:
            line = arduinoData.readline().decode("utf-8")
            print(line)
            # need to read line by line, careful
            temps = map(float, line.split('\n\n'))
            for temp in temps:
                check_temp(temp)
        time.sleep(1)

if __name__ == '__main__':
    main()
