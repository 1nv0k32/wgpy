from remoulade import declare_actors
from remoulade import set_broker

from wgpy.worker.actors.main_actor import main_actor
from wgpy.worker.worker import get_broker


set_broker(get_broker())
declare_actors([main_actor])
