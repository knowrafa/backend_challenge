# How to run this application

## 1. Clone this repo
```shell
$ git clone https://github.com/knowrafa/backend_challenge/
```
## 2. Download [Docker](https://docs.docker.com/engine/install/) and check if is installed.
```shell
$ docker -v
```
## 3. After installed, go do solution/car_maintenance/ directory
```shell
$ cd solution/car_maintenance/
```
## 4. Run inside this directory
```shell
$ docker-compose up
```

## 5. Acess http://localhost:8050/docs/swagger/ for Api Documentation and using. You can make all requisitions from swagger page.

## ACTIONS



### CreateCar ->  POST to /api/v1/car/ with body as follows:
```json
{
  "name": "Car name",
  "gas_capacity": 200
}
```

> - You car will be created with 200 liters of capacity, 100% of gas_count and 4 new tyres with no degradation.

### Trip -> POST to endpoint /api/v1/car/{car_pk}/trip/ with body as follows
```json
{
  "kilometers": 10,
}
```

#### In case of error, will receive a error like

```json
{
  "errors": {
    "degradation": [
      "Your degradation cannot be greater than 100. Change your tyres or take a shorter trip. "
    ]
  },
  "status": 400,
  "exception": "{'degradation': [ErrorDetail(string='Your degradation cannot be greater than 100. Change your tyres or take a shorter trip. ', code='max_degradation')]}"
}

```

> - All errors in plataform will be like above structure. Made by exception handler to padronize all error messages.


### Refuel -> POST to endpoint /api/v1/car/{car_pk}/refuel/ with body as follows
```json
{
  "liters": 50,
}
```


In case of error, will receive a error like

```json
{
  "errors": {
    "invalid": "The car should NOT be refueled before it has less than 5% gas on tank!"
  },
  "status": 400,
  "exception": "{'invalid': ErrorDetail(string='The car should NOT be refueled before it has less than 5% gas on tank!', code='invalid')}"
}

or

{
  "errors": {
    "gas_count": [
      "Your gas count cant be cannot be greater than 100. Refuel your car with less liters."
    ]
  },
  "status": 400,
  "exception": "{'gas_count': [ErrorDetail(string='Your gas count cant be cannot be greater than 100. Refuel your car with less liters.', code='max_gas_count')]}"
}

# or other error in same structure

```

### GetCarStatus -> GET in endpoint /api/v1/car/{car_pk}/

Will receive a response in the following format:
```json
{
  "id": 6,
  "name": "Sample car",
  "gas_capacity": 200,
  "gas_count": 4,
  "tyres": [
    {
      "id": 28,
      "car": 6,
      "degradation": 6.666666666666667,
      "in_use": true
    },
    {
      "id": 27,
      "car": 6,
      "degradation": 6.666666666666667,
      "in_use": true
    },
    {
      "id": 26,
      "car": 6,
      "degradation": 6.666666666666667,
      "in_use": true
    },
    {
      "id": 25,
      "car": 6,
      "degradation": 6.666666666666667,
      "in_use": true
    },
    {
      "id": 21,
      "car": 6,
      "degradation": 100,
      "in_use": false
    },
    {
      "id": 23,
      "car": 6,
      "degradation": 100,
      "in_use": false
    },
  ]
}
```

### CreateTyre -> POST to endpoint /api/v1/tyre/ with body as follows
```json
{
  "car": 6,
}
```

Response body will be
```json
{
  "id": 32,
  "car": 6,
  "degradation": 0,
  "in_use": false
}
```

### For Swap Tyres -> POST to endpoint /api/v1/tyre/{tyre_pk}/swap/ with body as follows:

> - tyre_pk = id of tyre to be replaced
> - tyre = new tyre
```json
{
  "tyre": 10
}
```

In case of sucess:

```json
{
  "id": 32,
  "car": 6,
  "degradation": 0,
  "in_use": false
}
```

In case of failure:

```json

{
  "errors": {
    "invalid": "Both tyres should be from same car. Choose only same car tyres."
  },
  "status": 400,
  "exception": "{'invalid': ErrorDetail(string='Both tyres should be from same car. Choose only same car tyres.', code='invalid')}"
}

or

{
  "errors": {
    "invalid": "You cannot create another tyre, this car is already with 4 in use"
  },
  "status": 400,
  "exception": "{'invalid': ErrorDetail(string='You cannot create another tyre, this car is already with 4 in use', code='invalid')}"
}

# or other error in same structure
```
