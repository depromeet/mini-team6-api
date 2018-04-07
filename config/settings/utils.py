import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
conf_file = os.path.join(BASE_DIR, 'conf.json')

with open(conf_file) as f:
    secrets = json.loads(f.read())


def get_key(settings, secrets=secrets):
    # Configuration 파일에서 중요 키 가져오기
    try:
        return secrets[settings]
    except KeyError:
        raise ImproperlyConfigured("Set the {} environment variable".format(settings))
