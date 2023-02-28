from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from .operations import operations, _check_health

logger = get_logger('baracuddaRBL')


class baracuddaRBL(Connector):

    def execute(self, config, operation, params, **kwargs):
        action = operations.get(operation)
        return action(config, params)


    def check_health(self, config):
        _check_health(config)
