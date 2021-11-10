#!/usr/bin/env python3
import os
import yaml
import time
from core.util.util import ether_to_eth
from dotenv import load_dotenv
import logging
import logging.config
from datetime import datetime, date
from core.connectors.flexpool import Flexpool
from core.connectors.gsheets import GoogleSheet
from core.util import *
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

start = datetime.now()

logging.config.fileConfig('config/logger.conf', defaults={'logfilename': f'logs/run-{start.strftime("%Y%m%d%H%M%S")}.log'})
logger = logging.getLogger('mainIntegration')
#loading .env 
load_dotenv()

#loading project settings
config = {}
with open('config/settings.yml') as fs:
    try:
        config = yaml.safe_load(fs)
    except yaml.YAMLError:
        logger.exception('Failed to load project settings yaml file.')
        exit()

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']  
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

description="""
    [############################################################]
        Mining monitoring tool for Flexpool
        Authors: @Davidson Mizael
    [############################################################]
    """

print(description)

if __name__ == '__main__':
    try:
        logger.info('Starting main process.')
        flexpool = Flexpool(logger, config['flexpool']['base_url'], config['flexpool']['wallet'], config['flexpool']['coin'])
        
        balance = flexpool.check_balance()['content']
        balance = ether_to_eth(balance['result']['balance'])
        logger.info(f"Current balance: {balance}")

        current_date = start.strftime("%d/%m/%Y")

        gs = GoogleSheet(creds)
        sheet_instance = gs.get_sheet('Crypto Mining', 3)
        sheet_instance.append_row([current_date, str(balance)])

        end = datetime.now()
        logger.info(f'Script finished. Time elapsed: {end - start}.')
    except KeyboardInterrupt:
        logger.info('Interrupting process.')
        exit()
