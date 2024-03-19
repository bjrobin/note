# ETH 私有链搭建教程
## 安装 go-ethereum 客户端

    brew tap ethereum/ethereum
    brew install ethereum
## 检查安装是否成功：

    geth --help
## 在 /Desktop/blockchain 下新建 ethereum 目录，在其中再建一个 genesis.json
文件和一个子目录 /data。
PoW 共识版本的 genesis.json 文件内容如下：
```json
{
   "config": {
     "chainId": 1001,
     "homesteadBlock": 0,
     "eip150Block": 0,
     "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
     "eip155Block": 0,
     "eip158Block": 0,
     "byzantiumBlock": 0,
     "constantinopleBlock": 0,
     "petersburgBlock": 0,
     "istanbulBlock": 0,
     "ethash": {}
   },
   "nonce": "0x0",
   "timestamp": "0x5ddf8f3e",
   "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
   "gasLimit": "0x47b760",
   "difficulty": "0x00002",
   "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
   "coinbase": "0x0000000000000000000000000000000000000000",
   "alloc": { },
   "number": "0x0",
   "gasUsed": "0x0",
   "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```
由于 eth 经历过一次升级从 PoW 改为 PoS，目前最新版的 geth 已经不再内置 ethash，因此 PoS 的 genesis.json 和之前的文章会略有不同。下面这个是 PoS 版的 genesis.json 文件：
```json
{
   "config": {
     "chainId": 8888,
     "homesteadBlock": 0,
     "eip150Block": 0,
     "eip155Block": 0,
     "eip158Block": 0,
     "byzantiumBlock": 0,
     "constantinopleBlock": 0,
     "petersburgBlock": 0,
     "istanbulBlock": 0,
     "berlinBlock": 0,
     "clique": {
       "period": 5,
       "epoch": 30000
     }
   },
   "difficulty": "1",
   "gasLimit": "8000000",
   "extradata": "0x0000000000000000000000000000000000000000000000000000000000000000b7e24438A3fe363f46994feEEdfbF5ad5078378d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
   "alloc": {
     "27883476a0a617d8e6aa40888253608a0e05cfa4": { "balance": "300000" },
     "b7e24438A3fe363f46994feEEdfbF5ad5078378d": { "balance": "300000" },
     "87edfb2aed4875144fe1c3b28870284881990418": { "balance": "300000" }
   }
}
```
## 运行

    geth --datadir data init ./genesis.json


## 目录说明：

keystore 用来保存账户信息
geth 用来保存区块信息
## 启动以太坊私链：
    geth --datadir data --networkid 8888 console 2>geth.log
    networkid 为上面的 genesis.json 配置的 id，以太坊主网 id 为 1
    2>geth.log 这里的 2 是代表 stderr，这里是为了让私链的以太坊日志独立输出，防止影响命令行交互的显示