# yurenizer_backend
Backend of Yurenizer

## RUN LOCAL
```
poetry install
poetry shell
cd app
uvicorn main:app --reload
```

## Test Local
```
curl -X 'GET' \
  'http://127.0.0.1:8000/healthcheck' \
  -H 'accept: application/json'
```

```
curl -X 'POST' \
  'http://127.0.0.1:8000/normalize_text?text=text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "config": {
    "unify_level": "lexeme",
    "taigen": true,
    "yougen": false,
    "expansion": "from_another",
    "other_language": true,
    "alias": true,
    "old_name": true,
    "misuse": true,
    "alphabetic_abbreviation": true,
    "non_alphabetic_abbreviation": true,
    "alphabet": true,
    "orthographic_variation": true,
    "misspelling": true,
    "custom_synonym": true
  }
}'
```


## RUN Docker
```
docker build ./ -t yurenizer_backend 
docker run --name yurenizer_backend -p 9000:8080 yurenizer_backend 
```

## Test Docker on Local
```
 curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"resource": "/", "path": "/healthcheck", "httpMethod": "GET", "requestContext": {}}'
```

```
curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" \
-d '{
  "resource": "/",
  "path": "/normalize_text",
  "httpMethod": "POST",
  "queryStringParameters": {
    "text": "text"
  },
  "body": "{\"config\": {\"unify_level\": \"lexeme\", \"taigen\": true, \"yougen\": false, \"expansion\": \"from_another\", \"other_language\": true, \"alias\": true, \"old_name\": true, \"misuse\": true, \"alphabetic_abbreviation\": true, \"non_alphabetic_abbreviation\": true, \"alphabet\": true, \"orthographic_variation\": true, \"misspelling\": true, \"custom_synonym\": true}}",
  "requestContext": {}
}'
```