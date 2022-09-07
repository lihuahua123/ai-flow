#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from ai_flow.common.util.string_utils import remove_escape_codes


class StreamLogWriter:
    """Allows to redirect stdout and stderr to logger"""

    encoding: None = None

    def __init__(self, logger, level):

        self.logger = logger
        self.level = level
        self._buffer = ''

    def _propagate_log(self, message):
        """Propagate message removing escape codes."""
        self.logger .log(self.level, remove_escape_codes(message))

    def write(self, message):
        """
        Do whatever it takes to actually log the specified logging record

        :param message: message to log
        """
        if not message.endswith("\n"):
            self._buffer += message
        else:
            self._buffer += message
            self._propagate_log(self._buffer.rstrip())
            self._buffer = ''

    def flush(self):
        """Ensure all logging output has been flushed"""
        if len(self._buffer) > 0:
            self._propagate_log(self._buffer)
            self._buffer = ''
