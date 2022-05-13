from matplotlib.pyplot import table
from sqlmodel import SQLModel, Field
from sqlmodel import select


class Beer(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int


brewdog = Beer(name='Brewdog', style='NEIPA', flavor=6, image=8, cost=8)


# from dataclasses import dataclass

# @dataclass
# class Beer:
#     name: str
#     style: str
#     flavor: int
#     image: int
#     cost: int
