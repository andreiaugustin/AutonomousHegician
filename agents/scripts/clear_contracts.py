"""Clear contracts script."""

import yaml


path = "../hegic_deployer/skills/hegic_deployer/skill.yaml"
with open(path) as f:
    i = yaml.safe_load(f)

to_clear = [
    "btcoptions",
    "btcpool",
    "btcpriceprovider",
    "ethoptions",
    "ethpool",
    "exchange",
    "hegic",
    # 'ledger_id',
    "priceprovider",
    "stakingeth",
    "stakingwbtc",
    "wbtc",
]
new_params = {
    k: "" for k, v in i["models"]["strategy"]["args"].items() if k in to_clear
}

i["models"]["strategy"]["args"].update(new_params)

with open(path, "w") as f:
    yaml.dump(i, f)
