#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import Error

class Connector:
    """
        Connector class
        To manage the connection to the MySQL database
    """
    cnx = None

    def connection(self):
        """
            Open the connection to the MySQL database
            :return: the connection object
        """
        try:
            self.cnx = mysql.connector.connect(option_files='mysql.conf')

            return self.cnx

        except Error as e:
            print("La connexion à la base de données a échoué", e)    

    def close(self):
        """ Close the connection to the MySQL database """
        self.cnx.close()
  