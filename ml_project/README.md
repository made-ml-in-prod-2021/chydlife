Installation:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Usage:

python ml_example/pipeline.py configs/train_config.yaml


Test:

pytest tests/
