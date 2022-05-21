#!/usr/bin/env python3

import logging
import asyncio
from hbmqtt.broker import Broker


logger = logging.getLogger(__name__)

config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '192.168.55.105:9999',
            'max-connections': 50,
        },
    },
    'sys_interval': 90,
    'timeout-disconnect-delay': 300, # in seconds before broker kicks-off the client 
    'topic-check': {
        'enabled': True,
        'plugins': ['topic_taboo'],
    }
}


broker = Broker(config)

#@asyncio.coroutine
async def startBroker():
    await broker.start()

if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(startBroker())

    asyncio.get_event_loop().run_forever()
