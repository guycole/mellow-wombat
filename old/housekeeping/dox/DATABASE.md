# Data Base
SQLite, controlled by Django

## Tables
1. EventLog
    1. Event log
        | Column     | DataType       | Ndx | Description       |
        |------------|----------------|-----|-------------------|
        | id         | BigAutoField   | PK  | Primary key       |
        | time_stamp | DateTimeField  |     | time stamp        |
        | slot       | IntegerField   |     | Slot within crate |
        | event      | CharField(256) |     | Event text        |

1. GeoLoc
    1. Geographic location
        | Column       | DataType        | Ndx | Description        |
        |--------------|-----------------|-----|--------------------|
        | id           | BigAutoField    | PK  | Primary Key        |
        | host_ts      | BigIntegerField |     | Host Time Stamp    |
        | gps_ts       | BigIntegerField |     | GPS Time Stamp     |
        | altitude     | IntegerField    |     | Altitude * 10      |
        | latitude     | IntegerField    |     | Latitude * 1000    |
        | longitude    | IntegerField    |     | Longitude * 1000   |
        | speed        | IntegerField    |     | Speed * 1000       |
        | track        | IntegerField    |     | Track * 100        |
        | status       | CharField(64)   |     | Fix status         |
        | epx          | IntegerField    |     | EPX * 1000         |
        | epy          | IntegerField    |     | EPY * 1000         |
        | epv          | IntegerField    |     | EPV * 1000         |
        | eps          | IntegerField    |     | EPS * 1000         |
        | epc          | IntegerField    |     | EPC * 1000         |
        | epd          | IntegerField    |     | EPS * 1000         |

1. ShelfInventory
    1. Shelf inventory
        | Column      | DataType      | Ndx | Description           |
        |-------------|---------------|-----|-----------------------|
        | id          | BigAutoField  | PK  | Primary key           |
        | power       | BooleanField  |     | True, power on        |
        | slot        | IntegerField  |     | Slot within crate     |
        | shelf_type  | IntegerField  |     | Enumerated shelf type |
        | description | CharField(64) |     | Shelf description     |

1. Tasking
    1. Tasking 
        | Column     | DataType        | Ndx | Description      |
        |------------|-----------------|-----|------------------|
        | id         | BigAutoField    | PK  | Primary Key      |
