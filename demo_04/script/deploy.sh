#! /bin/sh

ACCOUNT_ID=`aws sts get-caller-identity --query 'Account' --output text`
sls deploy --account_id $ACCOUNT_ID
