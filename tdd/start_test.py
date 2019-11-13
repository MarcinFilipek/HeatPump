import unittest


dirs_modules = ['emodul',
                'emodul/values']

for dir in dirs_modules:
    loader = unittest.TestLoader()
    suite = loader.discover(dir)
    runner = unittest.TextTestRunner()
    runner.run(suite)
