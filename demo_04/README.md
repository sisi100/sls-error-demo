# 「あなたはXX番目の訪問者です」のDEMO

詳細は[この文字列をクリック](https://blog.i-tale.jp/2020/04/17/)←ブログへ飛びます。

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
