import os
print(os.environ.get('PYTHONPATH', '').split(os.pathsep))