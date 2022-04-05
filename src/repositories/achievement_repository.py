from pathlib import Path
from entities.achievement import Achievement
from config import ACHIEVEMENTS_FILE_PATH

class AchievementRepository:
    def __init__(self, file_path: str):
        self._file_path = file_path
        
    def _read(self):
        achievements = []
        self._ensure_file_exists()
        with open(self._file_path) as file:
            for row in file:
                achievement = row.replace('\n','')
                data = achievement.split(';')
                sport = data[0]
                date = data[1]
                duration = data[2]

                achievements.append(Achievement(sport, date, duration))
        
        return achievements
        
    def _write(self, achievements: list):
        self._ensure_file_exists()
        with open(self._file_path, 'w') as file:
            for achievement in achievements:
                row = f'{achievement.sport};{achievement.date};{achievement.duration}'
                file.write(row+'\n')
    
    def find_all(self):
        return self._read()
    
    def create(self, achievement: Achievement):
        achievements = self.find_all()

        achievements.append(achievement)

        self._write(achievements)

        return achievement

    def delete_all(self):
        self._write([])
        
    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    
    
achievement_repository = AchievementRepository(ACHIEVEMENTS_FILE_PATH)