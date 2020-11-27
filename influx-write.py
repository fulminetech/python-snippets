# Refer: https://github.com/influxdata/influxdb-python
# Refer: https://influxdb-python.readthedocs.io/en/latest/examples.html#tutorials-basic

from influxdb import InfluxDBClient

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
            "value": 0.64
        }
    }
]

# Connect to client
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')

# Create Database
client.create_database('example')

# Write to Database 
client.write_points(json_body)

# Read from Database
result = client.query('select value from cpu_load_short;')

print("Result: {0}".format(result))