"""Scheduled task handlers for gift_cards module."""
import logging
logger = logging.getLogger(__name__)

def check_expiry(payload):
    """Mark expired gift cards and send expiry notifications."""
    logger.info('gift_cards.check_expiry called')
    return {'status': 'not_implemented'}
