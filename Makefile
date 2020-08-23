PYTHON_VERSION := python3.8
VIRTUALENV_DIR := venv
RED='\033[1;91m'
NC='\033[0m' # No Color


# Creating Virtual env
define create_venv
	if [[ -d "./${VIRTUALENV_DIR}" ]]; then \
		echo "Virtual env already exists"; \
	else \
		${PYTHON_VERSION} -m venv ${VIRTUALENV_DIR}; \
	fi
endef

# Activating Virtual env
define activate
	$(call create_venv) && source $(VIRTUALENV_DIR)/bin/activate
endef

# Installing Packages
define install_packages
	pip install -r requirements.txt
endef

# Installing test Packages
define install_test_packages
	pip install -r requirements-test.txt
endef

.PHONY:clean build test collector writer

clean::
	rm -rf $(VIRTUALENV_DIR) .cache .eggs .tmp *.egg-info ./*.egg-info
	find . -name ".DS_Store" -exec rm -rf {} \; || true
	find . -name "*.pyc" -exec rm -rf {} \; || true
	find . -name "__pycache__" -exec rm -rf {} \; || true


build:
	$(call create_venv) && \
	$(call activate) && \
	$(call install_packages)
	$(call install_test_packages)

test: build
	$(call install_test_packages) && tox -- -svx -vv


