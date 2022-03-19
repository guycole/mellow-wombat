# Data Base
SQLite, controlled by Django

## Tables
1. Event
    1. Event log
        | Column       | DataType        | Ndx | Description        |
        |--------------|-----------------|-----|--------------------|
        | id           | BigAutoField    | PK  | Primary Key        |
        | time_stamp   | BigIntegerField |     | Time Stamp         |
        | slot         | IntegerField    |     | Slot within crate  |
        | event        | CharField(256)  |     | Event text         |

1. GeoLoc
    1. Geographic location
        | Column       | DataType        | Ndx | Description        |
        |--------------|-----------------|-----|--------------------|
        | id           | BigAutoField    | PK  | Primary Key        |
        | time_stamp   | BigIntegerField |     | Time Stamp         |
        | latitude     | BigIntegerField |     | Latitude * 1000    |
        | longitude    | BigIntegerField |     | Longitude * 1000   |

1. Inventory
    1. Shelf inventory
        | Column       | DataType      | Ndx | Description           |
        |--------------|---------------|-----|-----------------------|
        | id           | BigAutoField  | PK  | Primary key           |
        | power_on     | BooleanField  |     | True, power on        |
        | slot         | IntegerField  |     | Slot within crate     |
        | shelf_type   | IntegerField  |     | Enumerated shelf type |
        | description  | CharField(64) |     | Shelf description     |

1. ShelfPower
    1. Shelf power history
        | Column        | DataType        | Ndx | Description         |
        |---------------|-----------------|-----|---------------------|
        | id            | BigAutoField    | PK  | Primary key         |
        | slot          | IntegerField    |     | Slot within crate   |
        | power_on_ts   | BigIntegerField |     | Power on timestamp  |
        | power_off_ts  | BigIntegerField |     | Power off timestamp |

1. Tasking
    1. Tasking 
        | Column     | DataType        | Ndx | Description      |
        |------------|-----------------|-----|------------------|
        | id         | BigAutoField    | PK  | Primary Key      |
