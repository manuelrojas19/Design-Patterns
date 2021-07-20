""" The Observer Pattern defines one-to-many dependency beetwen objects so that when one object
    changes state, all of its dependents are notified and updated automatically.

    With the Observer Pattern, the subject is the object that contains the state and control.
    So the is one object with state. The observers use this state.

    When two objects are loosely coupled, the can interact, but have very little knowledge of each
    other. The observer pattern provides an object desing where subjects and observers are loosely
    coupled.
"""


from observer import CurrentConditionDisplay
from subject import WheaterData


def main():

    wheaterData = WheaterData()
    currentConditionsDisplay = CurrentConditionDisplay(wheaterData)

    wheaterData.setMeasurements(80, 65, 35.4)
    wheaterData.setMeasurements(82, 70, 29.9)
    wheaterData.setMeasurements(81, 68, 29.9)

if __name__ == '__main__':
    main()
