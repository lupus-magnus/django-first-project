from .models import Project
from apscheduler.schedulers.background import BackgroundScheduler


default_projects = [
    {
        "title": "Informed", 
        "description": "Informed is a mobile app that displays the weather forecast and customizable news to the user."
    },
    {
        "title": "Maestro X", 
        "description": "A mobile web that focuses on self-improvement and productivity for the user."
    },
    {
        "title": "Alexandria Project", 
        "description": "The Alexandria Project is a bot for telegram made using the python-telegram-api. It serves the user free pdf books accordingly to what title he asks for."
    }
]

def reset_projects():
    Project.objects.all().delete()
    for project in default_projects:
        Project.objects.create(title=project["title"], description=project["description"])

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_projects, 'interval', minutes=45)
    scheduler.start()

