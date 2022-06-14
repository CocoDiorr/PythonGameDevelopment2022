import os


DOIT_CONFIG = {"default_tasks": ["extract", "update", "compile", "tests", "docstyle", "flake"]}

Death_screen = os.path.join(os.path.dirname(__file__), "Zelda", "menu", "DeathScreen.py")
Death_screen_msg = os.path.join(os.path.dirname(__file__), "Zelda", "locale", "death_screen", "messages.pot")
Death_screen_locale = Death_screen_msg.replace("messages.pot", "")

Start_menu = os.path.join(os.path.dirname(__file__), "Zelda", "menu", "StartMenu.py")
Start_menu_msg = os.path.join(os.path.dirname(__file__), "Zelda", "locale", "start_menu", "messages.pot")
Start_menu_locale = Start_menu_msg.replace("messages.pot", "")

Companion = os.path.join(os.path.dirname(__file__), "Zelda", "companion", "Companion.py")
Companion_msg = os.path.join(os.path.dirname(__file__), "Zelda", "locale", "companion", "messages.pot")
Companion_locale = Companion_msg.replace("messages.pot", "")


def task_extract():
    return {
        "actions": ["pybabel extract " + Death_screen + " -o " + Death_screen_msg,
                    "pybabel extract " + Start_menu + " -o " + Start_menu_msg,
                    "pybabel extract " + Companion + " -o " + Companion_msg
                    ],
        "file_dep": [Death_screen, Start_menu, Companion],

        "targets": [Death_screen_msg, Start_menu_msg, Companion_msg]

    }


def task_update():
    return {
        "actions": ["pybabel update -i " + Death_screen_msg + " -d " + Death_screen_locale + " -D DeathScreen",
                    "pybabel update -i " + Start_menu_msg + " -d " + Start_menu_locale + " -D StartMenu",
                    "pybabel update -i " + Companion_msg + " -d " + Companion_locale + " -D Companion"],

        "file_dep": [Death_screen_msg, Start_menu_msg, Companion_msg]
    }


def task_compile():
    return {
        "actions": ["pybabel compile -D DeathScreen -d " + Death_screen_locale,
                    "pybabel compile -D StartMenu -d " + Start_menu_locale,
                    "pybabel compile -D Companion -d " + Companion_locale],

        "file_dep": [os.path.join(Death_screen_locale, "ru", "LC_MESSAGES", "DeathScreen.po"),
                     os.path.join(Start_menu_locale, "ru", "LC_MESSAGES", "StartMenu.po"),
                     os.path.join(Companion_locale, "ru", "LC_MESSAGES", "Companion.po")],

        "targets": [os.path.join(Death_screen_locale, "ru", "LC_MESSAGES", "DeathScreen.mo"),
                    os.path.join(Start_menu_locale, "ru", "LC_MESSAGES", "StartMenu.mo"),
                    os.path.join(Companion_locale, "ru", "LC_MESSAGES", "Companion.mo")]
    }


def task_tests():
    return {
        "actions": ["python3 -m unittest discover -s tests"]
    }


def task_docstyle():
    return {
        "actions": ["pydocstyle Zelda"]
    }


def task_flake():
    return {
        "actions": ["flake8"]
    }
