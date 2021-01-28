from octobot_tentacles_manager.api.inspector import check_tentacle_version
from octobot_commons.logging.logging_util import get_logger

if check_tentacle_version('1.2.0', 'binanceus', 'OctoBot-Default-Tentacles'):
    try:
        from .binanceus import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading binanceus: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bitmax', 'OctoBot-Default-Tentacles'):
    try:
        from .bitmax import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bitmax: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'coinbase_pro', 'OctoBot-Default-Tentacles'):
    try:
        from .coinbase_pro import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading coinbase_pro: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'kucoin', 'OctoBot-Default-Tentacles'):
    try:
        from .kucoin import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading kucoin: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'binance', 'OctoBot-Default-Tentacles'):
    try:
        from .binance import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading binance: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'kraken', 'OctoBot-Default-Tentacles'):
    try:
        from .kraken import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading kraken: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'default_spot_ccxt', 'OctoBot-Default-Tentacles'):
    try:
        from .default_spot_ccxt import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading default_spot_ccxt: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.2.0', 'bitmex', 'OctoBot-Default-Tentacles'):
    try:
        from .bitmex import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading bitmex: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')
