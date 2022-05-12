from dataclasses import dataclass


@dataclass
class Beer:
    name: str
    style: str
    flavor: int
    image: int
    cost: int


brewdog = Beer(name='Brewdog', style='NEIPA', flavor=6, image=8, cost=8)
