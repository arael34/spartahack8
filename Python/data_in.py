def main():
    import pickle
    import serial
    import re
    from twiliomessage import check_temp
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
                    with open("temp.p", "wb") as tempfile:
                        pickle.dump(latest_temp, tempfile)
                else:
                    latest_soundlevel = int(num)
                    with open("noise.p", "wb") as noisefile:
                        pickle.dump(latest_soundlevel, noisefile)
                t = not t

if __name__ == '__main__':
    main()
