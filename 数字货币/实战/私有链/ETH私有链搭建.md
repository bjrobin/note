# ETH 私有链搭建教程
## 安装 go-ethereum 客户端

    brew tap ethereum/ethereum
    brew install ethereum
## 检查安装是否成功：

    geth --help



# geth --datadir node1 account new
INFO [03-20|11:21:19.968] Maximum peer count                       ETH=50 total=50
Your new account is locked with a password. Please give a password. Do not forget this password.
Password: 
Repeat password: 

Your new key was generated

Public address of the key:   0x82cf08637D9E2524676c65916E0C80889328F9a3
Path of the secret key file: node1/keystore/UTC--2024-03-20T03-21-34.119832000Z--82cf08637d9e2524676c65916e0c80889328f9a3

- You can share your public address with anyone. Others need it to interact with you.
- You must NEVER share the secret key with anyone! The key controls access to your funds!
- You must BACKUP your key file! Without the key, it's impossible to access account funds!
- You must REMEMBER your password! Without the password, it's impossible to decrypt the key!


# geth --datadir node2 account new
INFO [03-20|11:23:10.225] Maximum peer count                       ETH=50 total=50
Your new account is locked with a password. Please give a password. Do not forget this password.
Password: 
Repeat password: 

Your new key was generated

Public address of the key:   0x769f487b5dCCE66579094A5E3bcF70AFe6b276E4
Path of the secret key file: node2/keystore/UTC--2024-03-20T03-23-15.816109000Z--769f487b5dcce66579094a5e3bcf70afe6b276e4

- You can share your public address with anyone. Others need it to interact with you.
- You must NEVER share the secret key with anyone! The key controls access to your funds!
- You must BACKUP your key file! Without the key, it's impossible to access account funds!
- You must REMEMBER your password! Without the password, it's impossible to decrypt the key!


# geth init --datadir node1 genesis.json
INFO [03-20|11:41:19.369] Maximum peer count                       ETH=50 total=50
INFO [03-20|11:41:19.374] Set global gas cap                       cap=50,000,000
INFO [03-20|11:41:19.374] Initializing the KZG library             backend=gokzg
INFO [03-20|11:41:19.390] Defaulting to pebble as the backing database
INFO [03-20|11:41:19.390] Allocated cache and file handles         database=/Users/lhqer/MY/2024/data/ethereum/node1/geth/chaindata cache=16.00MiB handles=16
INFO [03-20|11:41:19.923] Opened ancient database                  database=/Users/lhqer/MY/2024/data/ethereum/node1/geth/chaindata/ancient/chain readonly=false
INFO [03-20|11:41:19.923] State schema set to default              scheme=hash
INFO [03-20|11:41:19.923] Writing custom genesis block
INFO [03-20|11:41:19.979] Persisted trie from memory database      nodes=3 size=399.00B time=55.515813ms gcnodes=0 gcsize=0.00B gctime=0s livenodes=0 livesize=0.00B
INFO [03-20|11:41:20.193] Successfully wrote genesis state         database=chaindata hash=345c4d..03676d
INFO [03-20|11:41:20.193] Defaulting to pebble as the backing database
INFO [03-20|11:41:20.193] Allocated cache and file handles         database=/Users/lhqer/MY/2024/data/ethereum/node1/geth/lightchaindata cache=16.00MiB handles=16
INFO [03-20|11:41:20.639] Opened ancient database                  database=/Users/lhqer/MY/2024/data/ethereum/node1/geth/lightchaindata/ancient/chain readonly=false
INFO [03-20|11:41:20.640] State schema set to default              scheme=hash
INFO [03-20|11:41:20.640] Writing custom genesis block
INFO [03-20|11:41:20.659] Persisted trie from memory database      nodes=3 size=399.00B time=19.421233ms gcnodes=0 gcsize=0.00B gctime=0s livenodes=0 livesize=0.00B
INFO [03-20|11:41:20.872] Successfully wrote genesis state         database=lightchaindata hash=345c4d..03676d


# geth init --datadir node2 genesis.json
lhqer@lhqer64 ethereum % geth init --datadir node2 genesis.json
INFO [03-20|11:42:02.971] Maximum peer count                       ETH=50 total=50
INFO [03-20|11:42:02.976] Set global gas cap                       cap=50,000,000
INFO [03-20|11:42:02.976] Initializing the KZG library             backend=gokzg
INFO [03-20|11:42:02.995] Defaulting to pebble as the backing database
INFO [03-20|11:42:02.995] Allocated cache and file handles         database=/Users/lhqer/MY/2024/data/ethereum/node2/geth/chaindata cache=16.00MiB handles=16
INFO [03-20|11:42:03.409] Opened ancient database                  database=/Users/lhqer/MY/2024/data/ethereum/node2/geth/chaindata/ancient/chain readonly=false
INFO [03-20|11:42:03.409] State schema set to default              scheme=hash
INFO [03-20|11:42:03.409] Writing custom genesis block
INFO [03-20|11:42:03.431] Persisted trie from memory database      nodes=3 size=399.00B time=20.982566ms gcnodes=0 gcsize=0.00B gctime=0s livenodes=0 livesize=0.00B
INFO [03-20|11:42:03.641] Successfully wrote genesis state         database=chaindata hash=345c4d..03676d
INFO [03-20|11:42:03.641] Defaulting to pebble as the backing database
INFO [03-20|11:42:03.641] Allocated cache and file handles         database=/Users/lhqer/MY/2024/data/ethereum/node2/geth/lightchaindata cache=16.00MiB handles=16
INFO [03-20|11:42:04.149] Opened ancient database                  database=/Users/lhqer/MY/2024/data/ethereum/node2/geth/lightchaindata/ancient/chain readonly=false
INFO [03-20|11:42:04.149] State schema set to default              scheme=hash
INFO [03-20|11:42:04.149] Writing custom genesis block
INFO [03-20|11:42:04.169] Persisted trie from memory database      nodes=3 size=399.00B time=19.504119ms gcnodes=0 gcsize=0.00B gctime=0s livenodes=0 livesize=0.00B
INFO [03-20|11:42:04.417] Successfully wrote genesis state         database=lightchaindata hash=345c4d..03676d


# bootnode
先生成一个key，生成之后下次启动bootnode就不用再特意生成key了，直接用已有的key
bootnode -genkey boot.key


# bootnode -nodekey boot.key -addr :30305
This key can then be used to generate a bootnode as follows:
bootnode -nodekey boot.key -addr :30305
enode://f3cfc1597b9fbae6788aa3f1539895c01a56dab5f9c22a7d63085f793c3c53de5c943d33fa978db7903fadd65e0578156d3911847325428f07fbf5e9b99b7b50@127.0.0.1:0?discport=30305
Note: you're using cmd/bootnode, a developer tool.
We recommend using a regular node as bootstrap node for production deployments.
INFO [03-20|11:39:12.334] New local node record                    seq=1,710,905,952,333 id=a17542ed30bf4604 ip=<nil> udp=0 tcp=0





geth --datadir node1 --port 30306 --bootnodes "enode://f3cfc1597b9fbae6788aa3f1539895c01a56dab5f9c22a7d63085f793c3c53de5c943d33fa978db7903fadd65e0578156d3911847325428f07fbf5e9b99b7b50@127.0.0.1:0?discport=30305"  --networkid 12345 --unlock 0x82cf08637D9E2524676c65916E0C80889328F9a3 --password node1/password.txt --authrpc.port 8551 --mine --miner.etherbase 0x82cf08637D9E2524676c65916E0C80889328F9a3

geth --datadir node2 --port 30307 --bootnodes "enode://f3cfc1597b9fbae6788aa3f1539895c01a56dab5f9c22a7d63085f793c3c53de5c943d33fa978db7903fadd65e0578156d3911847325428f07fbf5e9b99b7b50@127.0.0.1:0?discport=30305"  --networkid 12345 --unlock 0x769f487b5dCCE66579094A5E3bcF70AFe6b276E4 --password node2/password.txt --authrpc.port 8552



geth attach node1/geth.ipc


geth attach node2/geth.ipc

eth.getBalance(eth.accounts[0])


eth.sendTransaction({
  to: '0x769f487b5dCCE66579094A5E3bcF70AFe6b276E4',
  from: eth.accounts[0],
  value: 1
});


geth --unlock 0x82cf08637D9E2524676c65916E0C80889328F9a3 --mine

## 在 /Desktop/blockchain 下新建 ethereum 目录，在其中再建一个 genesis.json
文件和一个子目录 /data。

由于 eth 经历过一次升级从 PoW 改为 PoS，目前最新版的 geth 已经不再内置 ethash，因此 PoS 的 genesis.json 和之前的文章会略有不同。下面这个是 PoS 版的 genesis.json 文件：
```json
{
  "config": {
    "chainId": 12345,
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
  "extradata": "0x00000000000000000000000000000000000000000000000000000000000000007df9a875a174b3bc565e6424a0050ebc1b2d1d820000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  "alloc": {
    "7df9a875a174b3bc565e6424a0050ebc1b2d1d82": { "balance": "300000" },
    "f41c74c9ae680c1aa78f42e5647a62f353b7bdde": { "balance": "400000" }
  }
}
```
## 执行初始化
    cd /Users/lhqer/MY/2024/data/ethereum
    geth --datadir data init ./genesis.json

    geth init --datadir node1 genesis.json
执行后，将提示成功初始化创世区


## 目录说明：

keystore 用来保存账户信息
geth 用来保存区块信息
## 进入控制台：
    geth  --networkid 9999 console
    geth --datadir data --networkid 8888 console
    geth --networkid 8888 console

    geth --datadir data --networkid 8888 console 2>geth.log
    networkid 为上面的 genesis.json 配置的 id，以太坊主网 id 为 1
    2>geth.log 这里的 2 是代表 stderr，这里是为了让私链的以太坊日志独立输出，防止影响命令行交互的显示

JavaScript Console
https://geth.ethereum.org/docs/interacting-with-geth/javascript-console

## log
lhqer@lhqer64 ethereum % geth --datadir data --networkid 8888 console
INFO [03-20|10:28:54.282] Maximum peer count                       ETH=50 total=50
INFO [03-20|10:28:54.285] Set global gas cap                       cap=50,000,000
INFO [03-20|10:28:54.286] Initializing the KZG library             backend=gokzg
INFO [03-20|10:28:54.304] Allocated trie memory caches             clean=154.00MiB dirty=256.00MiB
INFO [03-20|10:28:54.304] Using pebble as the backing database
INFO [03-20|10:28:54.304] Allocated cache and file handles         database=/Users/lhqer/MY/2024/data/ethereum/data/geth/chaindata cache=512.00MiB handles=5120
INFO [03-20|10:28:54.508] Opened ancient database                  database=/Users/lhqer/MY/2024/data/ethereum/data/geth/chaindata/ancient/chain readonly=false
INFO [03-20|10:28:54.509] State scheme set to already existing     scheme=hash
INFO [03-20|10:28:54.510] Initialising Ethereum protocol           network=8888 dbversion=8
INFO [03-20|10:28:54.510] 
INFO [03-20|10:28:54.510] ---------------------------------------------------------------------------------------------------------------------------------------------------------
INFO [03-20|10:28:54.510] Chain ID:  8888 (unknown)
INFO [03-20|10:28:54.510] Consensus: Clique (proof-of-authority)
INFO [03-20|10:28:54.510] 
INFO [03-20|10:28:54.510] Pre-Merge hard forks (block based):
INFO [03-20|10:28:54.510]  - Homestead:                   #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/homestead.md)
INFO [03-20|10:28:54.510]  - Tangerine Whistle (EIP 150): #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/tangerine-whistle.md)
INFO [03-20|10:28:54.510]  - Spurious Dragon/1 (EIP 155): #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/spurious-dragon.md)
INFO [03-20|10:28:54.510]  - Spurious Dragon/2 (EIP 158): #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/spurious-dragon.md)
INFO [03-20|10:28:54.510]  - Byzantium:                   #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/byzantium.md)
INFO [03-20|10:28:54.510]  - Constantinople:              #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/constantinople.md)
INFO [03-20|10:28:54.510]  - Petersburg:                  #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/petersburg.md)
INFO [03-20|10:28:54.510]  - Istanbul:                    #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/istanbul.md)
INFO [03-20|10:28:54.510]  - Berlin:                      #0        (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/berlin.md)
INFO [03-20|10:28:54.510]  - London:                      #<nil> (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/london.md)
INFO [03-20|10:28:54.510] 
INFO [03-20|10:28:54.510] The Merge is not yet available for this network!
INFO [03-20|10:28:54.510]  - Hard-fork specification: https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/paris.md
INFO [03-20|10:28:54.510] 
INFO [03-20|10:28:54.510] Post-Merge hard forks (timestamp based):
INFO [03-20|10:28:54.510] 
INFO [03-20|10:28:54.510] ---------------------------------------------------------------------------------------------------------------------------------------------------------
INFO [03-20|10:28:54.510] 
INFO [03-20|10:28:54.510] Loaded most recent local block           number=0 hash=0efe09..ad72c3 td=1 age=55y2d2h
INFO [03-20|10:28:54.511] Initialized transaction indexer          range="last 2350000 blocks"
INFO [03-20|10:28:54.512] Loaded local transaction journal         transactions=0 dropped=0
INFO [03-20|10:28:54.520] Enabled snap sync                        head=0 hash=0efe09..ad72c3
INFO [03-20|10:28:54.520] Gasprice oracle is ignoring threshold set threshold=2
WARN [03-20|10:28:54.540] Unclean shutdown detected                booted=2024-03-19T18:07:07+0800 age=16h21m47s
WARN [03-20|10:28:54.541] Engine API enabled                       protocol=eth
WARN [03-20|10:28:54.541] Engine API started but chain not configured for merge yet
INFO [03-20|10:28:54.541] Starting peer-to-peer node               instance=Geth/v1.13.14-stable/darwin-amd64/go1.22.0
INFO [03-20|10:28:54.652] New local node record                    seq=1,710,838,927,538 id=10d1ce86ca718157 ip=127.0.0.1 udp=30303 tcp=30303
INFO [03-20|10:28:54.653] Started P2P networking                   self=enode://655af653f51250f50bc5c2e85472c191e817d94c518669e9419452639bdcf43d8941f424390828cb8c8ed40f568d9f2872cd186c579e4151405adc791624372a@127.0.0.1:30303
INFO [03-20|10:28:54.655] IPC endpoint opened                      url=/Users/lhqer/MY/2024/data/ethereum/data/geth.ipc
INFO [03-20|10:28:54.655] Loaded JWT secret file                   path=/Users/lhqer/MY/2024/data/ethereum/data/geth/jwtsecret crc32=0xe8031a0e
INFO [03-20|10:28:54.656] WebSocket enabled                        url=ws://127.0.0.1:8551
INFO [03-20|10:28:54.656] HTTP server started                      endpoint=127.0.0.1:8551 auth=true prefix= cors=localhost vhosts=localhost
WARN [03-20|10:28:54.684] Served eth_coinbase                      reqid=3 duration="28.067µs" err="etherbase must be explicitly specified"
Welcome to the Geth JavaScript console!

instance: Geth/v1.13.14-stable/darwin-amd64/go1.22.0
at block: 0 (Thu Jan 01 1970 08:00:00 GMT+0800 (CST))
 datadir: /Users/lhqer/MY/2024/data/ethereum/data
 modules: admin:1.0 clique:1.0 debug:1.0 engine:1.0 eth:1.0 miner:1.0 net:1.0 rpc:1.0 txpool:1.0 web3:1.0

To exit, press ctrl-d or type exit
> INFO [03-20|10:28:57.936] New local node record                    seq=1,710,838,927,539 id=10d1ce86ca718157 ip=103.84.44.162 udp=30303 tcp=30303
INFO [03-20|10:29:04.867] Looking for peers                        peercount=0 tried=142 static=0
INFO [03-20|10:29:14.955] Looking for peers                        peercount=0 tried=141 static=0
INFO [03-20|10:29:25.005] Looking for peers                        peercount=0 tried=167 static=0
INFO [03-20|10:29:36.061] Looking for peers                        peercount=0 tried=136 static=0
INFO [03-20|10:29:46.208] Looking for peers                        peercount=0 tried=100 static=0
INFO [03-20|10:29:56.209] Looking for peers                        peercount=0 tried=199 static=0
INFO [03-20|10:30:06.228] Looking for peers                        peercount=2 tried=88  static=0
INFO [03-20|10:30:16.333] Looking for peers                        peercount=1 tried=105 static=0
