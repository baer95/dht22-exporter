# dht22-exporter

A prometheus exporter for the `DHT22`/`AM2302` temperature and humidity sensor.

 * Baud rate: 115200
 * Sampling Rate: 0.5Hz

## Usage

```shell
apt update
apt upgrade
apt install python3-pip

python3 -m pip install -r requirements.txt

python3 main.py
```

Then, open http://localhost:8000/

## Docs & Links

**`DHT22`/`AM2302` Sensor**

 * https://m.media-amazon.com/images/I/91T9FaRG0nL.pdf
 * https://github.com/adafruit/Adafruit_CircuitPython_DHT

**Prometheus**

 * https://github.com/prometheus/client_python
 * https://prometheus.io/docs/practices/instrumentation/
 * https://prometheus.io/docs/instrumenting/writing_exporters/
