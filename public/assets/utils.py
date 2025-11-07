import logging
import os
import pickle
import redis
from typing import Any, Mapping

logger = logging.getLogger(__name__)

def get_redis_config(config: Mapping[str, str]) -> redis.ConnectionPool:
    host = config.get('host', 'localhost')
    port = config.get('port', 6379)
    db = config.get('db', 0)

    try:
        pool = redis.ConnectionPool(host=host, port=port, db=db)
        return pool
    except redis.ConnectionError as e:
        logger.error(f"Failed to connect to Redis: {e}")
        raise

def load_cache(file_path: str) -> Any:
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'rb') as f:
        return pickle.load(f)

def save_cache(file_path: str, cache: Any) -> None:
    with open(file_path, 'wb') as f:
        pickle.dump(cache, f)