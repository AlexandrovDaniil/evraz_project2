import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    BROKER_URL: str = f'amqp://' \
                      f"{os.getenv('RABBITMQ_USER', 'user')}:" \
                      f"{os.getenv('RABBITMQ_PASSWORD', 'password')}@" \
                      f"{os.getenv('RABBITMQ_HOST', 'localhost')}:" \
                      f"{os.getenv('RABBITMQ_PORT', 5672)}"

    LOGGING_LEVEL: str = 'INFO'

    @property
    def LOGGING_CONFIG(self):
        return {
            'loggers': {
                'kombu': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }
