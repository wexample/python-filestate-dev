from typing import Any, Optional

from wexample_config.const.types import DictConfig
from wexample_filestate.config_option.text_filter_config_option import (
    TextFilterConfigOption,
)
from wexample_filestate.const.disk import DiskItemType
from wexample_helpers.helpers.string import string_ensure_end_with_new_line


class WithVersionWorkdirMixin:
    def append_version(self, config: DictConfig | None = None) -> DictConfig:
        config.get("children").append(
            {
                "name": "version.txt",
                "type": DiskItemType.FILE,
                "should_exist": True,
                "default_content": self._get_version_default_content(),
                "text_filter": [TextFilterConfigOption.OPTION_NAME_ENSURE_NEWLINE],
            }
        )

        return config

    def _get_version_default_content(self) -> Any:
        return string_ensure_end_with_new_line("0.0.1")
