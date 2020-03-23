[![CircleCI](https://circleci.com/gh/GovWizely/lambda-canada-trade-leads/tree/master.svg?style=svg)](https://circleci.com/gh/GovWizely/lambda-canada-trade-leads/tree/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/c2a11b9417165bffcb1f/maintainability)](https://codeclimate.com/github/GovWizely/lambda-canada-trade-leads/maintainability)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=GovWizely/lambda-canada-trade-leads)](https://dependabot.com)

# Canada Trade Leads Lambda

This project provides an AWS Lambda that creates a single JSON document from [Canada Trade Leads](https://buyandsell.gc.ca).
It uploads that JSON file to a S3 bucket.

## Prerequisites

- This project is tested against Python 3.7+ in [CircleCI](https://app.circleci.com/github/GovWizely/lambda-canada-trade-leads/pipelines).

## Getting Started

	git clone git@github.com:GovWizely/lambda-canada-trade-leads.git
	cd lambda-canada-trade-leads
	mkvirtualenv -p /usr/local/bin/python3.8 -r requirements-test.txt canada-trade-leads

If you are using PyCharm, make sure you enable code compatibility inspections for Python 3.7/3.8.

### Tests

```bash
python -m pytest
```

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, you can do something like `export AWS_DEFAULT_PROFILE=govwizely`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control.

## Invocation

	lambda invoke -v
 
## Deploy
    
To deploy:

	lambda deploy --requirements requirements.txt
