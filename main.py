#!/usr/bin/venvp5 python
# -*- coding: utf-8 -*-

from src.data.db.helpers import Helpers
from src.view.main_view import MainView

# Let's start the application
if __name__ == "__main__":
    # view = Helpers()
    # view.populate_database()

    view = MainView()
    view.start_program()