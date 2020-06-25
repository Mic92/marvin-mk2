from typing import Any
from typing import Awaitable
from typing import Callable
from typing import Dict
from typing import List


class CommandRouter:
    def __init__(self, subrouters: List["CommandRouter"] = []) -> None:
        self.command_handlers: Dict[str, Callable[..., Awaitable[Any]]] = dict()
        for subrouter in subrouters:
            self.command_handlers.update(subrouter.command_handlers)

    def register_command(self, regex: str) -> Callable[[Callable], Callable]:
        def decorator(
            function: Callable[..., Awaitable[Any]]
        ) -> Callable[..., Awaitable[Any]]:
            self.command_handlers[regex] = function
            return function

        return decorator
