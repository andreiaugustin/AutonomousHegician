#!/bin/sh
cd hegic_contracts
pip install web3==5.11.1
python HegicOptionsDeploy.py
pip install web3==5.2.2
cd ../
python autonomous_hegician/data_store.py
cd autonomous_hegician
aea -s run
