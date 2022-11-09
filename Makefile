build:
	# docker build -t leetcode-bot:latest . # local
	flyctl launch --dockerfile Dockerfile
	flyctl secrets set --app leetcode-bot-2 ZULIP_API_KEY=$(ZULIP_API_KEY) ZULIP_EMAIL=$(ZULIP_EMAIL) ZULIP_SITE=$(ZULIP_SITE)
deploy:
	flyctl deploy --dockerfile Dockerfile --app leetcode-bot-2
test:
	pytest --cov=src tests/
	rm assets/coverage.svg
	coverage-badge -o assets/coverage.svg