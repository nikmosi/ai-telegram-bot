from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationBaseException(Exception):
    @property
    def message(self) -> str:
        return "Exception happen in application."
