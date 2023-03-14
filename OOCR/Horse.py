from Animal import Animal
from Water import Water
from Oxygen import Oxygen


class Leg:
    def __init__(self, leg):
        print("my " + leg)


class Horse(Animal):
    m_lbLeg: Leg
    m_rbLeg: Leg
    m_laLeg: Leg
    m_raLeg: Leg

    def __init__(self):
        m_lbLeg = Leg(" left back Leg")
        m_rbLeg = Leg(" right back Leg")
        m_laLeg = Leg(" left ahead Leg")
        m_raLeg = Leg(" right ahead Leg")

    def metabolize(self, o, w):
        print("Horse Depends on Oxygen and Water")

    def propagate(self):
        print("propagate: Mares give birth 30kg")
