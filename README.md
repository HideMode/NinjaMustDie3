# NinJaMustDie Utils

## Prerequisite

1. 安装[Python3.X](https://www.python.org/downloads/)

2. 安装依赖
```bash
pip3 install -r requirement.txt
```

## Usage
> `uids.txt` 为游戏uid列表，自行更新（一行一id）

```bash
# 进入项目目录后执行
python3 src/giftCodeViewThread.py 兑换码名称


## 新手礼包
```
cat 新手兑换码| while read line
do
echo $line
python3 src/giftCodeViewThread.py $line
done
```
