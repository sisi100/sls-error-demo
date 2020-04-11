# サーバレスのMy躓いたDEMO

## 初期化

```
$ cd demo_01
$ make init 
```
**.env.aws-credentials** が作られるのでアクセスキーとシークレットアクセスキーを書き込んでください。

## デプロイ

```
$ make sls p='sls deploy'
```

## 削除

```
$ make sls p='sls remove'
```
