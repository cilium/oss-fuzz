#!/usr/bin/env python
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
"""Custom options for pixman."""
import os

import package


class Package(package.Package):
  """pixman package."""

  def __init__(self, apt_version):
    super(Package, self).__init__('pixman', apt_version)

  def post_download(self, source_directory):  # pylint: disable=no-self-use
    """Workaround for incorrect checking of GCC vector extension availability."""
    os.system('sed s/support_for_gcc_vector_extensions=yes/'
              'support_for_gcc_vector_extensions=no/ -i %s/configure.ac' %
              source_directory)

  def pre_build(self, _source_directory, env, _custom_bin_dir):  # pylint: disable=no-self-use
    """Pre-build configuration for pixman."""
    blacklist_flag = ' -fsanitize-blacklist=' + os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'pixman_blacklist.txt')
    env['DEB_CXXFLAGS_APPEND'] += blacklist_flag
    env['DEB_CFLAGS_APPEND'] += blacklist_flag
