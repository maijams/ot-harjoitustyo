from entities.achievement import Achievement
from repositories.achievement_repository import (
    achievement_repository as default_achievement_repository
)

class AchievementService:
    def __init__(self, achievement_repository=default_achievement_repository):
        self._achievement_repository = achievement_repository
        
    def create_achievement(self, achievement):
        achievement = achievement
        return self._achievement_repository.create(achievement)
    
    def get_achievements(self):
        achievements = self._achievement_repository.find_all()
        return list(achievements)

achievement_service = AchievementService()