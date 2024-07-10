FROM python

WORKDIR /Home/PythonProject

ADD ./src ./src
ADD ./tests ./tests
ADD requirements.txt .
ADD run_test.sh .

RUN apt update
RUN apt -yq install curl
RUN apt -yq install jq
RUN pip install -r requirements.txt



ENTRYPOINT pytest -s -v tests/test_login_page.py -n ${THREADS_COUNT} --browser ${BROWSER} --hub_host ${HUB_HOST}
#ENTRYPOINT sh ./run_test.sh

