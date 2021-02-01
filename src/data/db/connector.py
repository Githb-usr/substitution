#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

class Connector:
    """
        Connector class
        To manage the connection to the MySQL database
    """
    cnx = None
    
    def connection(self):
        """
            To open the connection to the MySQL database
            :return: the connection object
        """
        self.cnx = mysql.connector.connect(
            user='pbadmin', password='pass38',
            host='127.0.0.1',
            database='substitution'
            )

        return self.cnx
    
    def close(self):
        """ To close the connection to the MySQL database """
        self.cnx.close()
        