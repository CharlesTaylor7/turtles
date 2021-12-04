from dataclasses import dataclass


@dataclass
class Config:
    debug: bool = False


settings = Config(debug=True)
