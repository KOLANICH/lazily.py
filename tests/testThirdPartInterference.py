import sys
from pathlib import Path
import unittest
import os

class Tests(unittest.TestCase):
	def testThirdPartyInterference(self):
		self.etalon = [
		]

		from lazily.functools import partial
		import csv
		os.stat(csv.__file__)


if __name__ == "__main__":
	unittest.main()