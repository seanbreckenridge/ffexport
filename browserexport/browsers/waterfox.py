from .common import (
    Path,
    platform,
)
from .firefox import Firefox

# seems to match firefox schema well enough for all of our usage
class Waterfox(Firefox):
    @classmethod
    def data_directory(cls) -> Path:
        if platform == "darwin":
            # TODO: add
            return Path(".")
        else:
            return Path("~/.waterfox/").expanduser()