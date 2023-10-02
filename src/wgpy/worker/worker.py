from remoulade.brokers.rabbitmq import RabbitmqBroker

from wgpy.config import get_settings


BROKER: RabbitmqBroker | None = None


def get_broker() -> RabbitmqBroker:
    global BROKER

    if not BROKER:
        settings = get_settings()
        broker = RabbitmqBroker(
            url=settings.rabbitmq.url_string,
        )
        BROKER = broker

    return BROKER
