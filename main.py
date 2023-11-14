import adafruit_dht
from board import D12
from prometheus_client import start_http_server, Gauge
import time

PORT = 8000

INTERVAL = 60  # seconds

start_http_server(PORT)


dht22_sensor = adafruit_dht.DHT22(pin=D12, use_pulseio=False)

dht22_temperature_gauge = Gauge('dht22_temperature', 'Temperature of the DHT22 sensor')
dht22_humidity_gauge = Gauge('dht22_humidity', 'Humidity of the DHT22 sensor')

while True:
    try:
        temperature = dht22_sensor.temperature
        humidity = dht22_sensor.humidity

        if temperature is None or humidity is None:
            # retry
            continue

        dht22_temperature_gauge.set(temperature)
        dht22_humidity_gauge.set(humidity)

        time.sleep(INTERVAL)

    except RuntimeError:
        # retry
        continue
