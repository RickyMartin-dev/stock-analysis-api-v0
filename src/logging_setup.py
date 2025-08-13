import logging, sys, json

logger = logging.getLogger("stock_api")
logger.setLevel(logging.INFO)
h = logging.StreamHandler(sys.stdout)
h.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(h)

def log_json(**kw):
    logger.info(json.dumps(kw))