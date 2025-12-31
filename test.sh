set -eo pipefail
# 0이 아니면 실행이 되지 않음 echo $?

COLOR_GREEN=`tput setaf 2;`
#터미널 초록색
COLOR_NC=`tput sgr0;`
#터미널 초기화 노컬러

echo "Starting black"
poetry run black .
echo "OK"

echo "Starting ruff"
poetry run ruff check --select I --fix
poetry run ruff check --fix
echo "OK"

echo "Starting mypy"
poetry run mypy app --explicit-package-bases
echo "OK"

echo "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"