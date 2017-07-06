FROM        bin_ubuntu
MAINTAINER  dev@hackathon.com

# 현재경로의 모든 파일들을 컨테이너의 /srv/deploy_eb_docker폴더에 복사
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

# uwsgi실행경로
#   /root/.pyenv/versions/binstagram/bin/uwsgi
# 1.실행중인 컨테이너의 내부에서 uwsgi를 사용해서 8000번 포트로 외부와 연결해서 Django를 실행해보기
    # uwsgi를
    #   http 8000포트,
    #   chdir 프로젝트 django 코드
    #   home 가상환경 경로 적용 후 실행
    #/root/.pyenv/versions/binstagram/bin/uwsgi --http :8000 --chdir /srv/binstagram/django_app --home /root/.pyenv/versions/binstagram -w config.wsgi.debug


# 2.docker run실행시 곧바로 uWSGI에 의해서 서버가 작동되도록 Dockerfile을 수정 후 build, run 해보기

# 3.uwsgi설정을 ini파일로 작성(.config/uwsgi/uwsgi-app.ini)하고
#   작성한 파일로 실행되도록 supervisor/uwsgi.conf파일을 수정
    #   /root/.pyenv/versions/binstagram/bin/uwsgi --ini /srv/binstagram/.config/uwsgi/uwsgi-app.ini

# 4.nginx 설정파일, nginx사이트파일 (nginx.conf, nginx-app.conf)을 각각
#   /etc/nginx/nginx.conf, /etc/nginx/sites-available/nginx-app.conf로 복사
#   이 후 링크 작성 (/etc/nginx/sites-enabled/nginx-app.conf로 /etc/nginx/sites-available/nginx-app.conf를 연결)
# 4-1. supervisord실행부분을 주석처리하고 docker run으로 /bin/zsh을 2개 실행 (2번째는 docker exec사용)
#       직접 nginx와 uwsgi를 실행해서 외부에서 80번 포트로 잘 연결되는지 확인
#       안되면 로그확인하기
#           uwsgi: /tmp/uwsgi.log
#           nginx: /var/log/nginx/error.log

        #- 1번 터미널 창 : NGINX 실행
        #	- `docker run --rm -it -p 9000:80 eb /bin/zsh`
        #	- `nginx`
        #
        #- 2번 터미널 창: UWSGI 실행
        #	- `docker ps` 실행되고 있는 container id 확인
        #	- `docker exec -it <container id 4자리> /bin/zsh`
        #	- `uwsgi --ini /srv/binstagram/.config/uwsgi/uwsgi-app.ini`




