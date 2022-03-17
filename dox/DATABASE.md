# Data Base
SQLite

## Tables
1. Event
    1. Event Log
        | Column | DataType     | Index | Description |
        |--------|--------------|-------|-------------|
        | id     | BigAutoField | PK    | Primary Key |
1. GeoLoc
    1. Geographic Location
        | Column     | DataType        | Ndx | Description      |
        |------------|-----------------|-----|------------------|
        | id         | BigAutoField    | PK  | Primary Key      |
        | time_stamp | BigIntegerField |     | Time Stamp       |
        | latitude   | BigIntegerField |     | Latitude * 1000  |
        | longitude  | BigIntegerField |     | Longitude * 1000 |


1. Inventory
  1. Shelf Inventory
1. Tasking
  1. Tasking 
