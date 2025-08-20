from typing import Optional

from wexample_config.const.types import DictConfig
from wexample_filestate.const.disk import DiskItemType


class WithVersionWorkdirMixin:
    def append_version(self, config: Optional[DictConfig] = None) -> DictConfig:
        config.get("children").append({
            "name": 'version.txt',
            "type": DiskItemType.FILE,
            "should_exist": True,
            "default_content": f"0.0.1",
            "text_filter": [
                "trim"
            ],
        })

        return config
