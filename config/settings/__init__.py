import os, glob
from split_settings.tools import optional, include
from .utils import get_key

# 구동 환경 체크
ENV = os.environ.get('PROJECT_ENV') or 'development'
print('****Running on %s settings****' % ENV)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = get_key('SECRET_KEY')

# 설정 파일 분리
COMPONENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'components')
COMPONENTS = [
    'components/{}'.format(os.path.basename(component)) for component
    in glob.glob(os.path.join(COMPONENT_DIR, '*.py'))
]
SETTINGS = COMPONENTS + [
    'environments/%s.py' % ENV,
]
include(*SETTINGS)

"""
Component 안내
"""
"""
app: 장고 앱 + 써드파티 앱 + 프로젝트 앱 관리
database: 데이터베이스 관리
rest_framework: Rest Framework 설정
static_files: 정적 파일 설정
"""
