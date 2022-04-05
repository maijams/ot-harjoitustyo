import os

dirname = os.path.dirname(__file__)

ACHIEVEMENTS_FILENAME = os.getenv('ACHIEVEMENTS_FILENAME') or 'achievements.csv'
ACHIEVEMENTS_FILE_PATH = os.path.join(dirname, '..', 'data', ACHIEVEMENTS_FILENAME)
