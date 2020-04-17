# SQSトリガーのDEMO

## 初期化

```
$ cd demo_04
$ make init 
```
**.env.aws-credentials** が作られるのでアクセスキーとシークレットアクセスキーを書き込んでください。

APIをデプロイしたら、API GatewayのエンドポイントURLを下記のファイルの3行目のurlへコピペしてください。

demo_04/site/app.js


## デプロイ

```
$ make deploy
```

## 削除

```
$ make remove
```
