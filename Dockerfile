FROM        archys/bin_ubuntu
MAINTAINER  dev@hackathon.com

# 현재경로의 모든 파일들을 컨테이너의 /srv/binstagram폴더에 복사
COPY        . /srv/binstagram
# cd /srv/binstagram와 같은 효과
WORKDIR     /srv/binstagram
# requirements설치
RUN         /root/.pyenv/versions/binstagram/bin/pip install -r .requirements/deploy.txt

# supervisor 파일복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/

# nginx 파일복사
COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

# collectstatic 실행
RUN         /root/.pyenv/versions/binstagram/bin/python /srv/binstagram/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput

# supervisord 실행
CMD         supervisord -n

# 외부 노출할 포트
EXPOSE      80 8000
