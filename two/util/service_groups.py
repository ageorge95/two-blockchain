from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": "two_harvester two_timelord_launcher two_timelord two_farmer two_full_node two_wallet".split(),
    "node": "two_full_node".split(),
    "harvester": "two_harvester".split(),
    "farmer": "two_harvester two_farmer two_full_node two_wallet".split(),
    "farmer-no-wallet": "two_harvester two_farmer two_full_node".split(),
    "farmer-only": "two_farmer".split(),
    "timelord": "two_timelord_launcher two_timelord two_full_node".split(),
    "timelord-only": "two_timelord".split(),
    "timelord-launcher-only": "two_timelord_launcher".split(),
    "wallet": "two_wallet two_full_node".split(),
    "wallet-only": "two_wallet".split(),
    "introducer": "two_introducer".split(),
    "simulator": "two_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
