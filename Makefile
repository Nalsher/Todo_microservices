lint:
	poetry run flake8

add:
	git add .

commit:
	git commit -m "$(message)"

push:
	git push origin $(branch)