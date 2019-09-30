docker build -t mantao/mustdie3:latest . -f Dockerfile
docker tag mantao/mustdie3:latest registry.cn-hangzhou.aliyuncs.com/healthshare/mantao_test_python:1.0
docker push registry.cn-hangzhou.aliyuncs.com/healthshare/mantao_test_python:1.0