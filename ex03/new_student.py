import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random ID
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student
    """
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Generate the attributes that use functions
        In this case id and login
        """
        self.id = generate_id()
        self.login = self.name[0].capitalize() + self.surname.lower()
