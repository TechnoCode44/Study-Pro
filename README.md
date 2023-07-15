# Study Pro

A api for a simple flash card system.

## /database

`/database` is a `GET` request that returns json of a learning course. It takes one parameter which is the *course name*.

```
/database/foo # Returns questions & answers to foo in json
/database/bar # Returns questions & answers to bar in json
```

