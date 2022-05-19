# BeagleBoneBlack Cape
Hardware control interface for BeagleBone Black.

## Introduction
The Mellow Wombat housekeeping BeagleBoneBlack supports these hardware items:
1. 12 VDC power to application shelves (4x, GPIO)
1. Voltage/current sensors
1. GPS receiver w/PPS output (UART)
1. Door switches (2x, GPIO, for trailer deployment)
1. Lux sensor (1x)
1. Temperature sensor
1. Humidity sensor
1. Acceleromters (vibration) sensors

## Pins
    | Header | Pin | Name      | Description         |
    |--------|-----|-----------|---------------------|
    | P8     |  7  | GPIO_66   | Power Relay 6 (out) |
    | P8     |  8  | GPIO_67   | Power Relay 0 (out) |
    | P8     |  9  | GPIO_69   | Power Relay 7 (out) |
    | P8     | 10  | GPIO_68   | Power Relay 1 (out) |
    | P8     | 11  | GPIO_45   | Door Switch 0 (in)  |
    | P8     | 12  | GPIO_44   | Power Relay 2 (out) |
    | P8     | 14  | GPIO_26   | Power Relay 3 (out) |
    | P8     | 15  | GPIO_47   | Door Switch 1 (in)  |
    | P8     | 16  | GPIO_46   | Power Relay 4 (out) |
    | P8     | 17  | GPIO_27   | Buzzer (out)        |
    | P8     | 18  | GPIO_65   | Power Relay 5 (out) |
    | P9     |  1  | DGND      | Ground              |
    | P9     |  5  | VDD_5V    | Power Relay Vcc     |
    | P9     |  7  | SYS_5V    | GPS Vin             |
    | P9     | 12  | GPIO_60   | GPS PPS (in)        |
    | P9     | 19  | I2C2_SCL  | I2C Devices         |
    | P9     | 20  | I2C2_SDA  | I2C Devices         |
    | P9     | 24  | UART1_TXD | GPS Rx              |
    | P9     | 26  | UART1_RXD | GPS Tx              |

# Power
1. VDD_5V can supply 1A
1. DC_3.3V can supply 250 mA  

## Details
1. 12 VDC power to application shelves
    1. 8x reserved, 4x used.  FET power control to off cape relays.
    1. BS270 FET: 3.3V at 5 uA (8x = 40 uA)
    1. Relay: 5V at 400 uA (8x = 3.2 mA)

1. Voltage/current sensors
    1. tbd

1. GPS receiver w/PPS output
    1. Must be UART, not USB.
    1. Power?

1. Door switches (for trailer deployment)
    1. 2x reserved.  Magnetic reed switch.

1. Lux sensor
    1. TBD

1. Temperature/Humidity sensor
    1. DHT-20 https://www.adafruit.com/product/5183
    1. i2c device 0x38

1. Accelerometers
    1. I2C device
    
1. Buzzer
    1. GPIO