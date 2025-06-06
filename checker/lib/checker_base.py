from abc import ABC, abstractmethod
from github import Github
from typing import List, Optional

from lib.db_models import CheckInfoElement, CheckResultElement

class CheckerBase(ABC):
    @abstractmethod
    def check(self, data: CheckInfoElement) -> CheckResultElement:
        pass

