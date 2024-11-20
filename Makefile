# 改进的Makefile示例

.PHONY: all test lint migrate help

all: lint test  # 默认执行lint和test目标

test:  # 运行测试
	pytest

lint:  # 检查代码风格
	flake8

migrate:  # 执行数据库迁移（假设您想使用alembic）
	alembic revision --autogenerate -m "New migration"
	# 注意：这里添加了迁移信息的描述，您可以根据需要调整

help:  # 显示帮助信息
	@echo "Available targets:"
	@echo "  all       - Run lint and test targets"
	@echo "  test      - Run pytest to execute tests"
	@echo "  lint      - Run flake8 to check code style"
	@echo "  migrate   - Generate a new alembic migration"
	@echo "  help      - Display this help message"