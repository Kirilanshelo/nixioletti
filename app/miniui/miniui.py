import os
import logging
import random

def do_api_task(body):
    log = logging.getLogger('miniui')

    MYVAR = os.environ.get('MYVAR', 'default_value')

    log.info(f'mytask done')
    log.info(f'{body}')
    log.info(f'body.value {body.value}')

    return {'done':True, 'value': f'{MYVAR} {random.randint(0,100)} - Q: {body.value}'}
