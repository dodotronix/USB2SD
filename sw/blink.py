#!/usr/bin/python

import time
from mcp2210 import Mcp2210, Mcp2210GpioDesignation, Mcp2210GpioDirection

mcp = Mcp2210(serial_number="0001102288", vendor_id=0x04d8, product_id=0x00de,
        immediate_gpio_update=True)

for i in range(9):
    mcp.set_gpio_designation(i, Mcp2210GpioDesignation.GPIO)

mcp.set_gpio_direction(1, Mcp2210GpioDirection.OUTPUT)

while True:
    mcp.set_gpio_output_value(1, True)
    time.sleep(0.5)
    mcp.set_gpio_output_value(1, False)
    time.sleep(0.5)

