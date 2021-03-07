#!/usr/bin/env bash -v

./main.py --service-uri samplekafka-senior-b7bb.aivencloud.com:26096 --ca-path ~/work/aiven/kafkaCerts/ca.pem --key-path ~/work/aiven/kafkaCerts/service.key --cert-path ~/work/aiven/kafkaCerts/service.cert --producer
