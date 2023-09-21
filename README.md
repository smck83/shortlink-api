# shortlink-api
FastAPI using dbm for URL shortener service

# docker run

    docker run -it -p 8000:8000 -e HOST_URL="https://example.com" smck83/shortlink-api

# create url
GET request
    https://localhost:8000/createShortURL?url=https://www.longurl.example.com

Response:

    {
      "url": "https://example.com/2N78N",
      "longURL": "https://www.longurl.example.com"
    }

    
# visit url

    https://localhost:8000/2N78N or https://example.com/2N78N
    
