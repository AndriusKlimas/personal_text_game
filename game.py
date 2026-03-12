import random
import annotations


class Player:
    def __init__(self, name: str, health: int, max_health: int, damage: int, is_alive: bool):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.is_alive = is_alive

    