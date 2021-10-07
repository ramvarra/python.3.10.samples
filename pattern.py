from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0
    y: int = 0

@dataclass
class ThreeDPoint(Point):
    z: int = 0

@dataclass
class CenterPoint(Point):
    z: int = 0
@dataclass
class Fruit:
    name: str
        
pts = [Point(10, 50), CenterPoint(10, 20, 30), ThreeDPoint(10, 20, 30), Fruit("apple")]

for pt in pts:
    match pt:
        case ThreeDPoint(x=10, y=_, z=_):
            print(f"We are 3d: {pt}")
        case CenterPoint(x=10, y=_, z=_):
            print(f"We are Center: {pt}")
        case Point(x=10, y=_):
            print(f"2D This it- {pt}")
        case _:
            print(f"Not a point: {pt}")
"""
Should produce following print output:

2D This it- Point(x=10, y=50)
We are Center: CenterPoint(x=10, y=20, z=30)
We are 3d: ThreeDPoint(x=10, y=20, z=30)
Not a point: Fruit(name="apple")
"""
