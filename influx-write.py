# Refer: https://github.com/influxdata/influxdb-python
# Refer: https://influxdb-python.readthedocs.io/en/latest/examples.html#tutorials-basic

from influxdb import InfluxDBClient

# InfluxDB configs
INFLUX_HOST = "localhost"
INFLUX_PORT = 8086
INFLUX_USER = "root"
INFLUX_PASS = "root"
INFLUX_BASE = "root"

# Payload
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.65
        }
    }
]

# Connect to client
# client = InfluxDBClient(host, port, user, password, dbname)
client = InfluxDBClient(INFLUX_HOST, INFLUX_PORT, INFLUX_USER, INFLUX_PASS, INFLUX_BASE)

# Create Database
client.create_database('example')

# Write to Database 
client.write_points(json_body)

# Read from Database
result = client.query('select value from cpu_load_short;')

print("Result: {0}".format(result))