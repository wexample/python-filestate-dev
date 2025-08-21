from typing import Optional, Any

from wexample_config.const.types import DictConfig
from wexample_filestate.config_option.text_filter_config_option import TextFilterConfigOption
from wexample_filestate.const.disk import DiskItemType


class WithVersionWorkdirMixin:
    def append_version(self, config: Optional[DictConfig] = None) -> DictConfig:
        config.get("children").append({
            "name": 'version.txt',
            "type": DiskItemType.FILE,
            "should_exist": True,
            "default_content": self._get_version_default_content(),
            "text_filter": [
                TextFilterConfigOption.OPTION_NAME_ENSURE_NEWLINE
            ],
        })

        return config

    def _get_version_default_content(self) -> Any:
        return "0.0.1"
