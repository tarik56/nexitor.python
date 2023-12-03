## Nexitor client for Python Flask, Django and FastApi integration

Install with:

```
pip install nexitor-python
```

Flask integration example:

```python
from flask import Flask, jsonify, request
from nexitor.nexitor_flask import NexitorFlask


app = Flask(__name__, )

NexitorFlask(
    url="https://demo.nexitor.io",
    application="Nexitor Test",
    instance="Development",
    api_key="api-key",
    handler=app
)
```

Django & FastAPI TBD
