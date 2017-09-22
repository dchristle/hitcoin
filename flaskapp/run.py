#!/usr/bin/env python
from hitcoinapp import app
import gp
import os
import sys
import numpy as np
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

