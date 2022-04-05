from datetime import datetime
from tkinter import Tk
from ui.ui import UI
from repositories.achievement_repository import AchievementRepository
from entities.achievement import Achievement
from services.achievement_service import achievement_service


def main(): #Text UI
    print()
    print('Welcome to MySportAchievements!')
    print()
    while True:
        print('Enter "1" to add a new activity')
        print('Enter "2" to look at old achievements')
        print('Enter "3" to quit')
        print()
        value = input()
        
        if value == "1":
            sport = input('Enter sport: ')
            day = input('Enter date (dd/mm/yyyy): ')
            date = datetime.strptime(day, "%d/%m/%Y")
            duration = int(input('Enter duration (min): '))
            achievement = Achievement(sport, date, duration)
            achievement_service.create_achievement(achievement)         
         
        elif value == "2":
            data = achievement_service.get_achievements()
            print('Diary:\n')
            for achievement in data:
                print(achievement)
            print()
        
        elif value == "3":
            print('See you again!')
            break
        
        else:
            print('Invalid input\n')
        
        
def main2(): #Graphical UI
    window = Tk()
    window.title('MySportAchievements')
    
    ui_view = UI(window)
    ui_view.start()
    
    window.mainloop()

        
        
if __name__ == '__main__':
    main()