# *Torch.ly* Weather-Api
### Simple guide - Version 1
#### Run as Server:
To run on the server use `uvicorn main:app`
#### Use as client:
Just make a simple http request to the server and get your answer as a json. 

### Answer notation
#### Version 1:
#### Route: /v1/
*Request*: No parameters

*Response*: JSON-Array of weather conditions

## Upcoming updates:
### Version 1.2
Adding the optional feature to configure the weather conditions and corresponding weights
### Version 1.3
Make the server a docker container
### Version 2
Get back a random continuous map of weather conditions.
### Version 3
Given a date and a seed get a deterministic, random continuous map of weather conditions.
### Version 4
Given a date, seed and map of geographic features get a deterministic, random continuous map of weather conditions.
