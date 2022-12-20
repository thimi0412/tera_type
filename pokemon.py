from collections import Counter
from enum import Enum
from typing import ClassVar, Dict, List

from pprint import pprint
from type import Type, compatibility_table


class Pokemon:
    name: str
    type_1: Type
    type_2: Type
    week_types: Dict

    def __init__(self, name, type_1, type_2):
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.week_types = self.week_check()

    def attack(self, attack_type: Enum) -> float:
        magnification = compatibility_table[attack_type.value][
            self.type_1.value
        ]
        magnification *= compatibility_table[attack_type.value][
            self.type_2.value
        ]
        # print(
        #     f"Attak {attack_type.value}! -> Type({self.type_1.value}, {self.type_2.value})"
        # )
        # print(f"Magnification: {magnification}")
        return magnification
    
    def week_check(self) -> List[Type]:
        week_types = {}
        for t in Type:
            week = self.attack(t)
            if week >= 2.0:
                week_types[t] = week
        
        return week_types
    
    def better_tera_type(self) -> Type:
        result = []
        for week_type, magnification in self.week_types.items():
            for t in Type:
                magnification = compatibility_table[week_type.value][t.value]
                if magnification < 1.0:
                    result.append(t)
        c = Counter(result)
        pprint(c.most_common())


def main() -> None:
    poke = Pokemon("a", Type.GRASS, Type.DARK)
    poke.better()



if __name__ == "__main__":
    main()