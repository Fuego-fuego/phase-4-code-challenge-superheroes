#  Superheroes API
## Description
This is an API for tracking heroes and their superpowers.

All the responses are return in JSON data format

## Setup
To download the dependencies for the frontend and backend, run:

```console
pipenv install
pipenv shell
npm install --prefix client
```

You can run your Flask API on [`localhost:5555`](http://localhost:5555) by
running:

```console
python server/app.py
```

You can run your React app on [`localhost:4000`](http://localhost:4000) by
running:

```sh
npm start --prefix client
```

- There are tests included which you can run using `pytest -x`.
- There is a file `challenge-2-superheroes.postman_collection.json` that
  contains a Postman collection of requests for testing each route you will
  implement.



## Models
 The model classes are related in this way.

- A `Hero` has many `Power`s through `HeroPower`
- A `Power` has many `Hero`s through `HeroPower`
- A `HeroPower` belongs to a `Hero` and belongs to a `Power`


## Routes
### GET /heroes

Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  {
    "id": 2,
    "name": "Doreen Green",
    "super_name": "Squirrel Girl"
  },
  {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  {
    "id": 4,
    "name": "Janet Van Dyne",
    "super_name": "The Wasp"
  },
  {
    "id": 5,
    "name": "Wanda Maximoff",
    "super_name": "Scarlet Witch"
  },
  {
    "id": 6,
    "name": "Carol Danvers",
    "super_name": "Captain Marvel"
  },
  {
    "id": 7,
    "name": "Jean Grey",
    "super_name": "Dark Phoenix"
  },
  {
    "id": 8,
    "name": "Ororo Munroe",
    "super_name": "Storm"
  },
  {
    "id": 9,
    "name": "Kitty Pryde",
    "super_name": "Shadowcat"
  },
  {
    "id": 10,
    "name": "Elektra Natchios",
    "super_name": "Elektra"
  }
]
```

### GET /heroes/:id

If the `Hero` exists, return JSON data in the format below:

```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```

If the `Hero` does not exist, return the following JSON data, along with the
appropriate HTTP status code:

```json
{
  "error": "Hero not found"
}
```

### GET /powers

Return JSON data in the format below:

```json
[
  {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  },
  {
    "description": "gives the wielder the ability to fly through the skies at supersonic speed",
    "id": 2,
    "name": "flight"
  },
  {
    "description": "allows the wielder to use her senses at a super-human level",
    "id": 3,
    "name": "super human senses"
  },
  {
    "description": "can stretch the human body to extreme lengths",
    "id": 4,
    "name": "elasticity"
  }
]
```

### GET /powers/:id

If the `Power` exists, return JSON data in the format below:

```json
{
  "description": "gives the wielder super-human strengths",
  "id": 1,
  "name": "super strength"
}
```

If the `Power` does not exist, return the following JSON data, along with the
appropriate HTTP status code:

```json
{
  "error": "Power not found"
}
```

### PATCH /powers/:id

This route should update an existing `Power`. It should accept an object with
the following properties in the body of the request:

```json
{
  "description": "Valid Updated Description"
}
```

If the `Power` exists and is updated successfully (passes validations), update
its description and return JSON data in the format below:

```json
{
  "description": "Valid Updated Description",
  "id": 1,
  "name": "super strength"
}
```

If the `Power` does not exist, return the following JSON data, along with the
appropriate HTTP status code:

```json
{
  "error": "Power not found"
}
```

If the `Power` is **not** updated successfully (does not pass validations),
return the following JSON data, along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

### POST /hero_powers

This route should create a new `HeroPower` that is associated with an existing
`Power` and `Hero`. It should accept an object with the following properties in
the body of the request:

```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

If the `HeroPower` is created successfully, send back a response with the data
related to the new `HeroPower`:

```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
}
```

If the `HeroPower` is **not** created successfully, return the following JSON
data, along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```
