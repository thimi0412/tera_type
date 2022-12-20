from enum import Enum


class Type(Enum):
    NONE = "none"
    NORMAL = "normal"
    FIRE = "fire"
    WATAR = "watar"
    GRASS = "grass"
    ICE = "ice"
    FIGHTING = "fighting"
    POISON = "poison"
    GROUND = "ground"
    FLYING = "flying"
    PSYCHIC = "psychic"
    BUG = "bug"
    ROCK = "rock"
    GHOST = "ghost"
    DRAGON = "dragon"
    DARK = "dark"
    STEEL = "steel"
    FAIFY = "fairy"


compatibility_table = {
    "none": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 1.0,
        "fairy": 1.0,
    },
    "normal": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 0,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 1.0,
        "fairy": 1.0,
    },
    "fire": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 0.5,
        "watar": 0.5,
        "electric": 1.0,
        "grass": 2.0,
        "ice": 2.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 2.0,
        "rock": 0.5,
        "ghost": 1.0,
        "dragon": 0.5,
        "dark": 1.0,
        "steel": 2.0,
        "fairy": 1.0,
    },
    "watar": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 2.0,
        "watar": 0.5,
        "electric": 1.0,
        "grass": 0.5,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 2.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 2.0,
        "ghost": 1.0,
        "dragon": 0.5,
        "dark": 1.0,
        "steel": 1.0,
        "fairy": 1.0,
    },
    "electric": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 2.0,
        "electric": 0.5,
        "grass": 0.5,
        "ice": 1.0,
        "fighting": 2.0,
        "poison": 1.0,
        "ground": 0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 0.5,
        "dark": 1.0,
        "steel": 1.0,
        "fairy": 1.0,
    },
    "grass": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 0.5,
        "watar": 2.0,
        "electric": 1.0,
        "grass": 0.5,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 0.5,
        "ground": 2.0,
        "flying": 0.5,
        "psychic": 1.0,
        "bug": 0.5,
        "rock": 2.0,
        "ghost": 1.0,
        "dragon": 0.5,
        "dark": 1.0,
        "steel": 0.5,
        "fairy": 1.0,
    },
    "ice": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 0.5,
        "watar": 0.5,
        "electric": 1.0,
        "grass": 2.0,
        "ice": 0.5,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 2.0,
        "flying": 2.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 2.0,
        "dark": 1.0,
        "steel": 0.5,
        "fairy": 1.0,
    },
    "fighting": {
        "none": 1.0,
        "normal": 2.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 2.0,
        "fighting": 1.0,
        "poison": 0.5,
        "ground": 1.0,
        "flying": 0.5,
        "psychic": 0.5,
        "bug": 0.5,
        "rock": 2.0,
        "ghost": 0,
        "dragon": 1.0,
        "dark": 2.0,
        "steel": 2.0,
        "fairy": 0.5,
    },
    "poison": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 2.0,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 0.5,
        "ground": 0.5,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 0.5,
        "ghost": 0.5,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 0,
        "fairy": 2.0,
    },
    "ground": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 2.0,
        "watar": 1.0,
        "electric": 2.0,
        "grass": 0.5,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 2.0,
        "ground": 1.0,
        "flying": 0,
        "psychic": 1.0,
        "bug": 0.5,
        "rock": 2.0,
        "ghost": 1.0,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 2.0,
        "fairy": 1.0,
    },
    "flying": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 0.5,
        "grass": 2.0,
        "ice": 1.0,
        "fighting": 2.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 2.0,
        "rock": 0.5,
        "ghost": 1.0,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 0.5,
        "fairy": 1.0,
    },
    "psychic": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 2.0,
        "poison": 2.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 0.5,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 1.0,
        "dark": 0,
        "steel": 0.5,
        "fairy": 1.0,
    },
    "bug": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 0.5,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 2.0,
        "ice": 1.0,
        "fighting": 0.5,
        "poison": 0.5,
        "ground": 1.0,
        "flying": 0.5,
        "psychic": 2.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 0.5,
        "dragon": 1.0,
        "dark": 2.0,
        "steel": 0.5,
        "fairy": 0.5,
    },
    "rock": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 2.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 2.0,
        "fighting": 0.5,
        "poison": 1.0,
        "ground": 0.5,
        "flying": 2.0,
        "psychic": 1.0,
        "bug": 2.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 0.5,
        "fairy": 1.0,
    },
    "ghost": {
        "none": 1.0,
        "normal": 0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 2.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 2.0,
        "dragon": 1.0,
        "dark": 0.5,
        "steel": 1.0,
        "fairy": 1.0,
    },
    "dragon": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 2.0,
        "dark": 1.0,
        "steel": 0.5,
        "fairy": 0,
    },
    "dark": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 1.0,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 0.5,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 2.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 2.0,
        "dragon": 1.0,
        "dark": 0.5,
        "steel": 1.0,
        "fairy": 0.5,
    },
    "steel": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 0.5,
        "watar": 0.5,
        "electric": 0.5,
        "grass": 1.0,
        "ice": 2.0,
        "fighting": 1.0,
        "poison": 1.0,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 2.0,
        "ghost": 1.0,
        "dragon": 1.0,
        "dark": 1.0,
        "steel": 0.5,
        "fairy": 2.0,
    },
    "fairy": {
        "none": 1.0,
        "normal": 1.0,
        "fire": 0.5,
        "watar": 1.0,
        "electric": 1.0,
        "grass": 1.0,
        "ice": 1.0,
        "fighting": 2.0,
        "poison": 0.5,
        "ground": 1.0,
        "flying": 1.0,
        "psychic": 1.0,
        "bug": 1.0,
        "rock": 1.0,
        "ghost": 1.0,
        "dragon": 2.0,
        "dark": 2.0,
        "steel": 0.5,
        "fairy": 1.0,
    },
}