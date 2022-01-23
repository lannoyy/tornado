## Limits REST API

## Table of content

1. [Running](#launch)
3. [API](#apies)
4. [Credits](#credits)

## Running the app <a name="launch"></a>

```bash
$ docker-compose up -d --build
```

## API <a name="apies"></a>

1) 
    Post request with url - localhost:8000/api/add
   
    Create new request

    ```
    If body valid, return response with 200 status in format:
   ```json
   {
      "key": str,
      "data": str,
      "duplicates": int
   }
   ```
2)
    Put request with url - localhost:8000/api/put?key={key}
   
    Change request

    If body valid, return response with 200 status in format:
   ```json
   {
      "key": str,
      "data": str,
      "duplicates": int
   }
   ```

3) 
    Delete request with url - localhost:8000/api/delete?key={key}
   
    Delete request

   If request exists, return response with 200 status in format:
   ```json
   {
      "key": str,
      "data": str,
      "duplicates": int
   }
   ```
   If object with given key not found , return response with 404 status with format:
   ```json
   {
      "Error": "not found"
   }
   ```

4) 
    Get request with url - localhost:8000/api/get?key={key}
    
    View request

    If request exists return response with 200 status in format:
   ```json
   {
      "key": str,
      "data": str,
      "duplicates": int
   }
   ```

5)
    Get statistic with url - localhost:8000/api/statistic
    
    View statistic
   ```json
   {
    "total_count": int,
    "total_duplicate": int,
    "duplicate_to_requests": int
   }
   ```

## Credits <a name="credits"></a>

- Author - Yury Ledovsky
- [Telegram](https://t.me/lannoyy)
- [Github](https://github.com/lannoyy)