#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read_register
# read 10 registers and print result on stdout

# you can use the tiny modbus server "mbserverd" to test this code
# mbserverd is here: https://github.com/sourceperl/mbserverd

# the command line modbus client mbtget can also be useful
# mbtget is here: https://github.com/sourceperl/mbtget

from pyModbusTCP.client import ModbusClient
import time
ms = time.time_ns() // 1000000 

SERVER_HOST = "192.168.0.65"
SERVER_PORT = 502

PRE_ADDR = 6097
STATUS_ADDR = 2589


c = ModbusClient()
global MBSCAN
# Scan time in seconds
MBSCAN = 0.001

# uncomment this line to see debug message
#c.debug(True)

# define modbus server host, port
c.host(SERVER_HOST)
c.port(SERVER_PORT)

# open or reconnect TCP to server
if not c.is_open():
    if not c.open():
        print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    
    while True:
        # if open() is ok, read register (modbus function 0x03)
        if c.is_open():

            # Write multiple registers
            bits1 = c.write_multiple_registers(PRE_ADDR, [50,35])
            if bits1:
                print(+int(time.time_ns() // 1000000 - ms), "Registers write success!")
            else:
                print("Registers write failed!")

            # sleep 2s before next polling
            time.sleep(MBSCAN)

            # Write multiple coils
            bits1 = c.write_multiple_coils(STATUS_ADDR, [False, False])
            # if success display registers
            if bits1:
                print(+int(time.time_ns() // 1000000 - ms), "Coil write success!")
            else:
                print("Coil write failed!")
    
            # sleep 2s before next polling
            time.sleep(MBSCAN)

