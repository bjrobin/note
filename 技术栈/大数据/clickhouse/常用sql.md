

# address
```sql
CREATE TABLE address(
height Int32 ,
address String ,
p_address String ,
)
ENGINE = MergeTree()
PARTITION BY height
ORDER BY (height,address)
SETTINGS index_granularity=8192
```

