import Adafruit_DHT

#While this is running take the temperatue and humidity and write it to the textfile
# Sometimes the sensor get "none"value then it skips
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    if temperature != 'None':
        with open('data.txt', 'w') as f:
            f.write(str(temperature))
    print("wrote to file")
