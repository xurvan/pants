# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import logging

from pants.option.option_types import ArgsListOption, BoolOption, SkipOption
from pants.option.subsystem import Subsystem

logger = logging.getLogger(__name__)


class JavacSubsystem(Subsystem):
    options_scope = "javac"
    name = "javac"
    help = "The javac Java source compiler."

    skip = SkipOption("check")
    args = ArgsListOption(example="-g -deprecation")

    tailor_source_targets = BoolOption(
        default=True,
        help="If true, add `java_sources` and `java_tests` targets with the `tailor` goal.",
        advanced=True,
    )
