from Animal import Animal
from Water import Water
from Oxygen import Oxygen


class Leg:
    def Leg(self,leg):
        print("my "+leg);
class Horse(Animal):
    m_lbLeg: Leg
    m_rbLeg: Leg
    m_laLeg: Leg
    m_raLeg: Leg
    def Horse(self):
        m_lbLeg = Leg(" left back Leg\n");
        m_rbLeg = Leg(" right back Leg\n");
        m_laLeg = Leg(" left ahead Leg\n");
        m_raLeg = Leg(" right ahead Leg\n");

    def metabolize(self, o, w):
        print("Horse Depends on Oxygen and Water\n");

    def propagate(self):
        print("Horse generat small horse 30kg\n");