# サーバレスのMy躓いてないけど苦手DEMO

詳細はこちら

https://blog.i-tale.jp/2020/04/12/

## 初期化

```
$ cd demo_02
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
