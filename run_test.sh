echo "Waiting for Grid"
sleep 10

pytest -s -v tests/test_login_page.py -n ${THREADS_COUNT} --browser ${BROWSER} --hub_host ${HUB_HOST}

