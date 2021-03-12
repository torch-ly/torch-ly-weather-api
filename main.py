import json
from copy import deepcopy
import random

standardValues = {'temperature': 1, 'cloud': 1, 'rain': 1, 'wind': 1}

temperatureStages = ['freezing', 'cold', 'lightly cold', 'comfortable', 'lightly warm', 'warm', 'burning hot']
temperatureStagesValues = [5, 10, 22.5, 25, 22.5, 10, 5]
cloudStages = ['clear', 'bright', 'cloudy', 'very cloudy', 'overcast', 'covered in clouds']
cloudStagesValues = [20, 20, 20, 15, 10, 10]
rainStages = ['no rain', 'drizzling', 'light rain', 'rain', 'heavy rain', 'storm']
rainStagesValues = [20, 20, 20, 15, 15, 10]
windStages = ['calm', 'light breeze', 'medium wind', 'windy', 'heavy wind', 'hurricane']
windStagesValues = [15, 25, 25, 20, 10, 5]

Stages = [temperatureStages, cloudStages, rainStages, windStages]
StageValues = [temperatureStagesValues, cloudStagesValues, rainStagesValues, windStagesValues]

unlogicalCombinations = {'clear': rainStages[1:], 'bright': rainStages[-2:]}
"""
Json-Object structure:
{
'catastrophes': true,
'standardDistribution': true,
(optional)
'cloudWeight': int,
'rainWeight': int,
'windWeight': int,
'cloudStages':
}

"""


# Non configurable API-Endpoint
def getWeather():
    Max = []

    for values in StageValues:
        _sum = 0
        for i in range(len(values)):
            _sum += values[i]
            values[i] = _sum
        Max.append(_sum)

    Rs = []
    for m in Max:
        Rs.append(random.random() * m)

    condition = []
    for i in range(len(Stages)):
        for j, sv in enumerate(StageValues[i]):
            if Rs[i] <= sv:
                condition.append(Stages[i][j])
                break

    for key in unlogicalCombinations.keys():
        if key in condition:
            for c in unlogicalCombinations[key]:
                if c in condition:
                    return getWeather()

    return condition

if __name__ == "__main__":
    print(getWeather())