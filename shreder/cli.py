#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import argparse

from .__main__ import Shreder
from .badges import Badges


class ShrederCLI(Shreder, Badges):
    description = ""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-a', '--address', dest='address', help='Single address.')
    parser.add_argument('-u', '--username', dest='username', help='SSH username.')
    parser.add_argument('-l', '--list', dest='list', help='Passwords list.')
    args = parser.parse_args()

    def start(self):
        password = self.brute(
            self.args.address.split(':')[0],
            self.args.address.split(':')[1],
            self.args.username,
            self.args.list
        )

        if password:
            self.output_success("Password has been found!")
            self.output_information(f"Password: {password}")
        else:
            self.output_warning("Password is not found.")

def main():
    cli = ShrederCLI()
    cli.start()