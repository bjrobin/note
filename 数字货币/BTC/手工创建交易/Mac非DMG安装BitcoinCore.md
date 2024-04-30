# 配置文件
拷贝到/Users/lhqer/Library/Application Support/Bitcoin

```shell
regtest=1
[regtest]
dbcache=10240
txindex=1
upnp=1
rpcuser=username
rpcauth=a:2e64d931cb789e1eb04a79ebc47e5117$99c4c1201d46884e10871bf869e8aa8aaf6d021f70fb1e46f6bf17f44fa20045
rpcpassword=_VUXUo9H-nAhcE3TDiYNsagYxCH_yB1P85M6WJn10Qs
daemon=1
server=1
rest=1
rpcallowip=0.0.0.0/0
fallbackfee=0.0001
datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0/data
```
# 环境变量
    vi ~/.bash_profile 
    export PATH=$PATH:/Users/lhqer/MY/2024/data/bitcoin-25.0/bin
    source ~/.bash_profile
    bitcoind --help 
# 启动
    bitcoind
    默认生成这个路径
    /Users/lhqer/Library/Application Support/Bitcoin/regtest

# 参考
    Bitcoin Regtest测试网Mint教程(Ordinal协议)
    https://blog.web3idea.xyz/post/blockchain%2Fbitcoin%2FOrdinal+BitcoinTestNetwork

# 停止
    bitcoin-cli stop

# 参考
创建本地比特币网络regtest，手工创建交易，极速理解比特币原理
https://zhuanlan.zhihu.com/p/592586339

# createwallet
    其实这里钱包的公钥和私有就已经生成好了。
    bitcoin-cli createwallet walletname0430
```json
{
  "name": "walletname0430"
}
```
# 检查钱包
    可以看到，初始状态，钱包余额、可用余额、交易数量等都是0
    bitcoin-cli getwalletinfo
```json
{
  "walletname": "walletname0430",
  "walletversion": 169900,
  "format": "sqlite",
  "balance": 0.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 0.00000000,
  "txcount": 0,
  "keypoolsize": 4000,
  "keypoolsize_hd_internal": 4000,
  "paytxfee": 0.00000000,
  "private_keys_enabled": true,
  "avoid_reuse": false,
  "scanning": false,
  "descriptors": true,
  "external_signer": false
}
```
# 挖矿
bitcoin-cli -generate 100
下面来创建100个区块，也就是挖矿，一下子挖100个区块出来。这里是本地环境，很快就能完成。不像真实的比特币网络，大量的矿场竞争比算力竞争，谁先挖到算谁的。
```json
{
  "address": "bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc",
  "blocks": [
    "3aa6bdbd800309fb4bd423375fb7bc51d3d6f07c126ca26061406a46f22f4ed1",
    "71144bceb7d339d782dda2ab7d13df630e399cb31a4b6d18f4be474d9cacd4c5",
    "32fd2ce1aa9a1368e6e39f24f87c10324a4f91a83c4e901c6cb8ec39592d03ae",
    "3517358e93073c1f9afe640c8f6ef6401b3c165da659ba91d50f696f962fe0a5",
    "7ca55dc20ba177cd734b8afb34fae5ad5560c8d33aa1275a88f5dd618547f755",
    "7f995553c6eff90c0e850876b3b3cccb154384e99cbd44706da11c2c43b22d4a",
    "2d5557a5b9ff74e026be3fb8e68e7188ace4b97ed45c453698973c2134a57533",
    "161654a54b4c83026951ce60422812fdabeebf5868e9bc072f07eb52cd8f8998",
    "33f9706af865e2be73d068885536a75bac5a4724fbce2be5d0e11c62b0ad5b55",
    "0958e5720c5b26eeff748fdcf08969e6c87446da5b1a82b5a1b8eb5e62e226bb",
    "36196270883dbff89dd681157126b4fcfb000361d4116325b24ebe8d0ff6773b",
    "33f6d4189369f6cafb6bb547f0c4cb5bb0f2fa5162bd3d73ec62c98b8befffcb",
    "4939501abd82c3c75f29e86b1ee8ed243392230a79943ff2518a7ca403802287",
    "721cc75d1c5599ddf491fc8beecc130f36a46b3a7e86d8db689ab2ce20576939",
    "43a91d77a32ef58946df84a55f714f58c58029c601dc432fea04ce74d84a8cec",
    "2e9707acb31b2712fc3c9b8c22a9e7c4a166d95d74ac0514edae06956f03980a",
    "3ba9de68369bff42055b31453a39ee6adfa79f3cef7d5d296e7f367d8ac4695b",
    "057ef786c79dc0862efc65259831cac9c8ca0a482631afcf8ecd0f0323a29737",
    "4c56189ca791fdaa8f3bd4ef47487e94691b3ab107f06576aa10a46283527042",
    "755a222b653b8459b46d159a87dde0b69029df48d781bc9b792c35b20374da81",
    "0851f57569282618efd928ac8eb776432c5f1fbe78a37071de78e32bd51d2c65",
    "4bc708a01a6e645e1fe8050c7a3d0431a38419182dfbd2238636ceb4fedef0b4",
    "59ddf2ec31307b837811e2f5b061361341c06dfbb875affc2f1b75f0741749bb",
    "15addd472480e18ad0ada07c79e200dd4d13d5ab873576cefd262188d0a4547b",
    "0e4daae3114aee672b9e6661cc7a40f18c4ecaafc0b92a92c510b2820468aa80",
    "0a17f39372235cc5617fba9945148e4f5880e2dc8c1a121bd2ad766d46a251cf",
    "5799f915bc700c5de383665cba1611c5190d2f06bd0ab640ac7fbfeb1070b592",
    "19b6185aaff5d729aaf0bc7351355d57134543ef3ac5667b891757b3ab39247b",
    "31afeff5e2b54b67243298a4e7cb6d7d10db4513b52a1c2dc7829429c35645cd",
    "29703155810a614803680a5c6f5d56ca4cc1329b045aef6807558fde02a23142",
    "4f025efd8525881904fcc0b4431b7d4e187fe0611c950f1f87e87973b720cf33",
    "006b2e76c75d1755f25f23dbd9cd82631f49e77ce9ec981f4a2441b20bf46da7",
    "7ca4648f416ad3bcbd95055be0f9ac055682f96f28d9ffbb2ff3bd7bc17df64a",
    "05190e6b114bc551399c3c6c77c8075b9ab3f5ab95a9819105512c6f417cae8b",
    "6090c2e416443abd27e9be577e3c040bbabdef080b1430f2e78634986511ecce",
    "58efeab5f26a290348940095f1a5addaf95b47966219e256ee31132733cd8fed",
    "2fb12dae9048964e1810de81d775bc4cbc6460f4861e45ea4549e93bd2e14f08",
    "50ec0d4322495189072a4b339df785905b92cde11ca470d111b8bb1fd6552fb3",
    "03376c54d13ae4228f26acc1e630642c24add270ff55f093bad0b07d8c9d6589",
    "2733d8222519e9e3577f17caaddcf37ef20708df9e5228702639f345bc7e1256",
    "5fea2e609f2c76016de3c26ab0fffa324a04032b128e06cfc200e220d228f0a1",
    "42b7eb491b9ed7221a7463ce09b46454edf74c15099a846f86069b3799ccad1b",
    "59f09170ec67d701c19c24fa3ef146799bc19a6e6cd7733a2f3f7b9a9112ee77",
    "19ccb116f212691138e1f44ee65ff23acfafe8379d84d01848d990192a77ce51",
    "0eab3be23c2c13c7a1ab5c9dec0ef14f0269dabc4463d1bd8cf7106eef812cca",
    "27f58dde53463787f22cbfdf4eabaaf5b42163b2cf18391c0c67ee8de151f6ca",
    "69506e134826fdebea41713881304008191a3de40bf18f758688c08095615f65",
    "69038e271157db6675adb5f75590ae0f5260aa29fab49048e7e76b534a325740",
    "2a092cb4fd7bc972d7f139a4b0578adcc9bb119847fea2cdf08247e0bd05cd92",
    "6a7210b12c72e90301d3574fd861ecf6ac788e3d0d472ce8474b9de2143d9abc",
    "5cd4e5b6627128d3f974c5eceb6a31d9a63f7b9b4f62a005103efc86e4ac8027",
    "11e8c3a07876edc14f5483079f824b40962656037c3ae536b8b3fba39e57c08c",
    "63bde64ff79656ddb9072b10b46c648d4fd85499a776c615fa9873e7cc4eff95",
    "159c843c5881ed69cac737702748c35b42adaf7e3562b88d7e3107a3f8392bd1",
    "5e84f65c083f9f1fe989c862479a757ebd441a1de05c908878309b8ef2e1f800",
    "6ec92c1feb1d0dde762e21b14406a5dbc1dd05caa17fc5acc19e3d5c877975d2",
    "497cb516e9c5c9764a9db04ffc51174077eaeaa3a6cd503b8898d1f720742f07",
    "68e2a57ec0ae5fc5701051ea63b3ba00f5a1b35346c45e70a967c75af5ac93cc",
    "28748f98701d6008fe9142606a0068a87c71889797906b05d759c5ff6d5233d8",
    "04c30e9248ebf6cf84e1f6efff2635f12f039d12b9a823a56d62fe3f9da41f4f",
    "351116382e73170584ac46f21d391f054f937c9238f527fb22c2955fb7f49717",
    "4184737fa9d411d8ba92a52eb703269e8d5916b40649206ae23e6a5a7437566a",
    "5ff2bdd19dc2d886c8cadf126270c31b84f5593f5211b369907fc36920f4d136",
    "717c57cc8f7bed39c460c50654de035edca187c5d3f1aaa019921b7d35e08795",
    "2f02ee91fa7c4ac04c4fb27caf049dc95670659330cce910be134d5be9cda8af",
    "0683ac899fef64a00f60d6acca8dc9ddcf0c2334da284bb35e8b06a093263159",
    "49366aa5608a196860bb99aa032984d25fc78d4ed099cad4ac13e86670e95d1b",
    "72105a273c2f24a5b88b710655f56e691ee0a61f561abf3f9fe606a37fcf81ac",
    "6c4334d59381d9abe08fe669f0df42bf7b0b63d4fe016ab7608b4f87a24a7c72",
    "7ad3fcb181eaab534ff68b82641d37fe8b0c0f6d79789f36bbc02ed93e06d303",
    "469331a2103cf0c0f79b158623023619fc3459343962c388c97f4c2a93f74974",
    "3cc806e7ad3526f93622f118226571bb59d92ec827e71720f01dcb11cdf7958a",
    "050baf92dc1581e60e4aa7ebc32bea953ea66fdd241f89fc030e0a1356c9a564",
    "5e5af2d1396b6c30875274371a80712125e826a81452bc87039d69c2b4deb37b",
    "43e36932cecd700bd5cd2470d4189e67f2818b9507b023b99d5ef7d12fc3bcf2",
    "358b870b2657e073d305f0477e95771ca7a7044dc22b589cc4bd0e169f2244e1",
    "2e8897b3a8356254ce36824b43e72161861159b504a6de6a96d10446e4c65ca2",
    "51263b15a4ef9a1fba0c4fae6f3f7c96d3ee0cdeb841fa694d0e9ab527b1166c",
    "1a667fa8a30aff1aae1c25972871f9d7add9e55e6ba4f564a1fec53680517a54",
    "38fdc93cd41faae0b1568326e7395b4a77b95aa76faf4f10f1e2d847888a098b",
    "3bd3aa421d1cc2b74e3f03e82c20ab5f450db4ba22110a929826f9ba99dcc8e2",
    "30e757330e470f976790c8586f715fdd46207a2305533bc6abaac42787a0ffb6",
    "51cd0bfa033b6ff6ed7cf41d5bdfc202c8d1b4aa9f572e5626aaede2a8b6007b",
    "36e260881ac05285f1fcaae887c36ea7c09549acdfc76da62313d6c7365e3c5c",
    "40e8511e7ae43a0eb3b073387ae00ff45a0f6e5b30b234a0edc067b931eceade",
    "5de6d5dc33a0835d26a69a78679f1f244195dd8384b956e2140c9f1aeee15a2a",
    "2a90d244c144b188a9b852a4ce21f2d034aa22f268638d4744b6611f19373df2",
    "7ab70dd7afe9f9a6719556e164e077737821d56413104fed80d943ca3ea929b9",
    "01abc41f276cbebbd574fba15418d1c4cfe6b7a4c1df5a16156789cdb414baa0",
    "0a631101904eff0b08c76122295450b23e204c05096ad60f1ad774f923ad6500",
    "7439db71c114d76f40ed5e45c7791705dbde584779e862ea17cf2228a201ad8c",
    "33aeca57482161b1ae2bdc23180bb6608ab0432fac119aeb6b7e5f43a3406a6b",
    "1b1277ec36546be82c564b12422c7b2bd64cc398cf5c7fa9ccddd88dab23abab",
    "6f9a020d36e8ae8afdda94f1d16bc0dedd2480c1c809a864990c1fc2159d7d52",
    "5c2e7c1a05fbf6d0c482c380f7cceb116c52d1189246e73262d5602635f06172",
    "32f3af630a686f5b13fbb38ce7c3c455c6ad67c5d3d5fe3498fed493a031d23d",
    "1fe3bedda3d606a5ac0eda9e8cde09a74290228fd9e610059d6336746393ad83",
    "6429ae5dc7f497ada098c9b97850edb6c992bb4dd2166375877fdd87875cf7e7",
    "25f3185c3d9c7e7330363d4a8cbe27647f289fb1513d7bc419b97bd462f94359",
    "40e9fed0e3d7734793da8fa5012c9fbc51e1bb7a95d5bd726b4a331b48701799"
  ]
}

```

# 检查钱包
    bitcoin-cli getwalletinfo
    需要注意的是：balance为0，immature_balance为5000。这是因为区块奖励需要在101次确认之后才变为可用状态。
```json
{
  "walletname": "walletname0430",
  "walletversion": 169900,
  "format": "sqlite",
  "balance": 0.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 5000.00000000,
  "txcount": 100,
  "keypoolsize": 4000,
  "keypoolsize_hd_internal": 4000,
  "paytxfee": 0.00000000,
  "private_keys_enabled": true,
  "avoid_reuse": false,
  "scanning": false,
  "descriptors": true,
  "external_signer": false
}

```
# 挖矿
    再执行一次挖矿操作
    bitcoin-cli -generate 1
```json
{
  "address": "bcrt1qs5w0daey40yuj8wytq526me573z8rte5xsdwxy",
  "blocks": [
    "70f40d15f3f1d99171c33ca173a2a1330370584869923ea253082c3da0b17204"
  ]
}
```
# 再次检查钱包
可以看到可用余额balance变为了50。
bitcoin-cli getwalletinfo
```json
{
  "walletname": "walletname0430",
  "walletversion": 169900,
  "format": "sqlite",
  "balance": 50.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 5000.00000000,
  "txcount": 101,
  "keypoolsize": 4000,
  "keypoolsize_hd_internal": 4000,
  "paytxfee": 0.00000000,
  "private_keys_enabled": true,
  "avoid_reuse": false,
  "scanning": false,
  "descriptors": true,
  "external_signer": false
}
```
# listunspent
    使用 listunspent 指令显示未花交易输出USXOs也能印证：
    bitcoin-cli listunspent
```json
[
  {
    "txid": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
    "vout": 0,
    "address": "bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc",
    "label": "",
    "scriptPubKey": "0014907ee8b73f268afa5fccabeaaf17c3d49b3559a3",
    "amount": 50.00000000,
    "confirmations": 101,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([0889741b/84'/1'/0'/0/0]03c3ecb76ac26a69d80525245f3886b1a8b41a5c56038e96a7a003ddcfac524cbc)#49s8tqtd",
    "parent_descs": [
      "wpkh(tpubD6NzVbkrYhZ4YYcQfvUQ64Pw7dC6CVwCBAt5a39mvFRc5BDdPo9BvQhjXg7HULu1JbWtzMuPJhu1krvR2t3c6a2ikscsWeqjom1MXy89FGY/84'/1'/0'/0/*)#5z0esfzc"
    ],
    "safe": true
  }
]
```

# gettransaction
这里的金额是从哪里来的？就是那个挖100个区块，其中的第一个区块！后面挖了101次（包括后面刚刚单独generate加了一次），所以就确认了。马上验证一下：

根据txid，使用gettransaction查询
bitcoin-cli gettransaction 921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2
```json
{
  "amount": 50.00000000,
  "confirmations": 101,
  "generated": true,
  "blockhash": "3aa6bdbd800309fb4bd423375fb7bc51d3d6f07c126ca26061406a46f22f4ed1",
  "blockheight": 1,
  "blockindex": 0,
  "blocktime": 1714474026,
  "txid": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
  "wtxid": "ca4635d1ed833672627aeb0938d16b158f725ebccd56c8eda9e0896e46979ba7",
  "walletconflicts": [
  ],
  "time": 1714474026,
  "timereceived": 1714474026,
  "bip125-replaceable": "no",
  "details": [
    {
      "address": "bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc",
      "parent_descs": [
        "wpkh(tpubD6NzVbkrYhZ4YYcQfvUQ64Pw7dC6CVwCBAt5a39mvFRc5BDdPo9BvQhjXg7HULu1JbWtzMuPJhu1krvR2t3c6a2ikscsWeqjom1MXy89FGY/84'/1'/0'/0/*)#5z0esfzc"
      ],
      "category": "generate",
      "amount": 50.00000000,
      "label": "",
      "vout": 0
    }
  ],
  "hex": "020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff025100ffffffff0200f2052a01000000160014907ee8b73f268afa5fccabeaaf17c3d49b3559a30000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf90120000000000000000000000000000000000000000000000000000000000000000000000000"
}
```
    可以看到blockhash为： 3aa6bdbd800309fb4bd423375fb7bc51d3d6f07c126ca26061406a46f22f4ed1
    之前挖100个区块的指令，其输出第一个hash不就是这个嘛！
    那么，如果继续generate挖矿，区块奖励继续得以确认，钱包balance也会相应的增加。动手试试吧~

# 创建一个新的钱包
下面创建一个新的钱包，试验一下多个钱包间转账
bitcoin-cli createwallet walletname0430-1
```json
{
  "name": "walletname0430-1"
}
```
# 查询钱包
    现在我们有两个钱包了， walletname0430 和 walletname0430-1
## walletname0430
    bitcoin-cli -rpcwallet=walletname0430 listunspent
```json
[
  {
    "txid": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
    "vout": 0,
    "address": "bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc",
    "label": "",
    "scriptPubKey": "0014907ee8b73f268afa5fccabeaaf17c3d49b3559a3",
    "amount": 50.00000000,
    "confirmations": 101,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([0889741b/84'/1'/0'/0/0]03c3ecb76ac26a69d80525245f3886b1a8b41a5c56038e96a7a003ddcfac524cbc)#49s8tqtd",
    "parent_descs": [
      "wpkh(tpubD6NzVbkrYhZ4YYcQfvUQ64Pw7dC6CVwCBAt5a39mvFRc5BDdPo9BvQhjXg7HULu1JbWtzMuPJhu1krvR2t3c6a2ikscsWeqjom1MXy89FGY/84'/1'/0'/0/*)#5z0esfzc"
    ],
    "safe": true
  }
]
```
## walletname0430-1
    bitcoin-cli -rpcwallet=walletname0430-1 listunspent

```json
[
]
```
# 装载钱包
bitcoin-cli -regtest loadwallet walletname0430
bitcoin-cli -regtest loadwallet walletname0430-1

# 创建地址
    我们准备从 walletname0430 钱包给 walletname0430-1 钱包转10个比特币。
    注意：首先，需要给 walletname0430-1 创建地址，没有地址就没法收款，这个与现实中体验是一致的，很好理解。
    bitcoin-cli -rpcwallet=walletname0430-1 getnewaddress
    创建成功，返回地址如下
```json
bcrt1q506jexgq565v3au70h346cc4g60fdzq8ryl5r5
```
# 从B钱包转

    bitcoin-cli -rpcwallet=walletname0430-1 sendtoaddress bcrt1q506jexgq565v3au70h346cc4g60fdzq8ryl5r5 10
    马上报错说余额不足了。符合预期。
```shell
error code: -6
error message:
Insufficient funds
```
# 从A钱包转
    bitcoin-cli -rpcwallet=walletname0430 sendtoaddress bcrt1q506jexgq565v3au70h346cc4g60fdzq8ryl5r5 10 
    返回交易txid
```shell
6d49e9cc99085f746aa92feb34e8d93d79b43c9bed83f008cafca0fcc017d45f
```
# gettransaction
bitcoin-cli -rpcwallet=walletname0430 gettransaction 6d49e9cc99085f746aa92feb34e8d93d79b43c9bed83f008cafca0fcc017d45f true true
最后一个true参数表示显示decode信息
```json
{
  "amount": -10.00000000,
  "fee": -0.00001410,
  "confirmations": 0,
  "trusted": true,
  "txid": "6d49e9cc99085f746aa92feb34e8d93d79b43c9bed83f008cafca0fcc017d45f",
  "wtxid": "574ee9e43ca48a306a00ceb897c161d0a19b0ca1be2347d34cf21d1c0d53d85f",
  "walletconflicts": [
  ],
  "time": 1714475383,
  "timereceived": 1714475383,
  "bip125-replaceable": "yes",
  "details": [
    {
      "address": "bcrt1q506jexgq565v3au70h346cc4g60fdzq8ryl5r5",
      "category": "send",
      "amount": -10.00000000,
      "vout": 1,
      "fee": -0.00001410,
      "abandoned": false
    }
  ],
  "hex": "02000000000101a29a8bf4f729b28fafb474c89d927946ed16aba07a06639a7bb583e0f86c1a920000000000fdffffff027e226bee0000000016001475aa9a328c6b21620927d14d81c37d332d4e4c1b00ca9a3b00000000160014a3f52c9900a6a8c8f79e7de35d6315469e9688070247304402206771eff63c7baeb4c5adb33a9d42a8129c83ebad67bf5ce952f08eb83771e8ee022030d7a9d366b09204c92b41c3b19ba565bd30b3315f4c7741ef6eb3151b595078012103c3ecb76ac26a69d80525245f3886b1a8b41a5c56038e96a7a003ddcfac524cbc65000000",
  "decoded": {
    "txid": "6d49e9cc99085f746aa92feb34e8d93d79b43c9bed83f008cafca0fcc017d45f",
    "hash": "574ee9e43ca48a306a00ceb897c161d0a19b0ca1be2347d34cf21d1c0d53d85f",
    "version": 2,
    "size": 222,
    "vsize": 141,
    "weight": 561,
    "locktime": 101,
    "vin": [
      {
        "txid": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
        "vout": 0,
        "scriptSig": {
          "asm": "",
          "hex": ""
        },
        "txinwitness": [
          "304402206771eff63c7baeb4c5adb33a9d42a8129c83ebad67bf5ce952f08eb83771e8ee022030d7a9d366b09204c92b41c3b19ba565bd30b3315f4c7741ef6eb3151b59507801",
          "03c3ecb76ac26a69d80525245f3886b1a8b41a5c56038e96a7a003ddcfac524cbc"
        ],
        "sequence": 4294967293
      }
    ],
    "vout": [
      {
        "value": 39.99998590,
        "n": 0,
        "scriptPubKey": {
          "asm": "0 75aa9a328c6b21620927d14d81c37d332d4e4c1b",
          "desc": "addr(bcrt1qwk4f5v5vdvskyzf869xcrsmaxvk5unqmacn782)#c4csmraw",
          "hex": "001475aa9a328c6b21620927d14d81c37d332d4e4c1b",
          "address": "bcrt1qwk4f5v5vdvskyzf869xcrsmaxvk5unqmacn782",
          "type": "witness_v0_keyhash"
        }
      },
      {
        "value": 10.00000000,
        "n": 1,
        "scriptPubKey": {
          "asm": "0 a3f52c9900a6a8c8f79e7de35d6315469e968807",
          "desc": "addr(bcrt1q506jexgq565v3au70h346cc4g60fdzq8ryl5r5)#rx0ff6ww",
          "hex": "0014a3f52c9900a6a8c8f79e7de35d6315469e968807",
          "address": "bcrt1q506jexgq565v3au70h346cc4g60fdzq8ryl5r5",
          "type": "witness_v0_keyhash"
        }
      }
    ]
  }
}

```

vin中txid：指的是本次交易的输入交易的id。即本次转账的金额来源： 921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2
查看一下这个交易：

bitcoin-cli -rpcwallet=walletname0430 gettransaction 921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2 true true
```json
{
  "amount": 50.00000000,
  "confirmations": 101,
  "generated": true,
  "blockhash": "3aa6bdbd800309fb4bd423375fb7bc51d3d6f07c126ca26061406a46f22f4ed1",
  "blockheight": 1,
  "blockindex": 0,
  "blocktime": 1714474026,
  "txid": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
  "wtxid": "ca4635d1ed833672627aeb0938d16b158f725ebccd56c8eda9e0896e46979ba7",
  "walletconflicts": [
  ],
  "time": 1714474026,
  "timereceived": 1714474026,
  "bip125-replaceable": "no",
  "details": [
    {
      "address": "bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc",
      "parent_descs": [
        "wpkh(tpubD6NzVbkrYhZ4YYcQfvUQ64Pw7dC6CVwCBAt5a39mvFRc5BDdPo9BvQhjXg7HULu1JbWtzMuPJhu1krvR2t3c6a2ikscsWeqjom1MXy89FGY/84'/1'/0'/0/*)#5z0esfzc"
      ],
      "category": "generate",
      "amount": 50.00000000,
      "label": "",
      "vout": 0
    }
  ],
  "hex": "020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff025100ffffffff0200f2052a01000000160014907ee8b73f268afa5fccabeaaf17c3d49b3559a30000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf90120000000000000000000000000000000000000000000000000000000000000000000000000",
  "decoded": {
    "txid": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
    "hash": "ca4635d1ed833672627aeb0938d16b158f725ebccd56c8eda9e0896e46979ba7",
    "version": 2,
    "size": 167,
    "vsize": 140,
    "weight": 560,
    "locktime": 0,
    "vin": [
      {
        "coinbase": "5100",
        "txinwitness": [
          "0000000000000000000000000000000000000000000000000000000000000000"
        ],
        "sequence": 4294967295
      }
    ],
    "vout": [
      {
        "value": 50.00000000,
        "n": 0,
        "scriptPubKey": {
          "asm": "0 907ee8b73f268afa5fccabeaaf17c3d49b3559a3",
          "desc": "addr(bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc)#2uhw2ap7",
          "hex": "0014907ee8b73f268afa5fccabeaaf17c3d49b3559a3",
          "address": "bcrt1qjplw3dely6905h7v4042797r6jdn2kdr2l6zjc",
          "type": "witness_v0_keyhash"
        }
      },
      {
        "value": 0.00000000,
        "n": 1,
        "scriptPubKey": {
          "asm": "OP_RETURN aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9",
          "desc": "raw(6a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9)#cav96mf3",
          "hex": "6a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf9",
          "type": "nulldata"
        }
      }
    ]
  }
}
```


bitcoin-cli importaddress bcrt1qh83qc3lrsayw0fepr78xx2qg7cvqll6q59sdat
bitcoin-cli importaddress walletname0430

# 解释
这里，我们仔细分解一下比特币交易的过程具体如何进行。
可以看到：
"A"挖矿得到的50个比特币（交易 921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2 ）
，"A"转账给"B"（交易 6d49e9cc99085f746aa92feb34e8d93d79b43c9bed83f008cafca0fcc017d45f ）的资金来源。

更确切的说：交易921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2的输出，
相当于提出了一道【题目】，题目中包含了"A"的公钥hash: 907ee8b73f268afa5fccabeaaf17c3d49b3559a3
而在真正需要使用这笔资金的时候，在交易 6d49e9cc99085f746aa92feb34e8d93d79b43c9bed83f008cafca0fcc017d45f 中，需要去给出【答案】，
即在其输入中，txinwitness，第一个值为"A"的签名，第二个值为公钥。

然后，根据题目要求，使用答案去验证：

1）双重hash验证公钥：把本次交易提供的public key做两次hash运算RIPEMD160(SHA256(pubKey)) 与上次交易（题目中）的公钥hash比对。这里用python来计算验证一下。

import hashlib
import codecs

publickey = codecs.decode('03c3ecb76ac26a69d80525245f3886b1a8b41a5c56038e96a7a003ddcfac524cbc', 'hex')
s = hashlib.new('sha256', publickey).digest()
r = hashlib.new('ripemd160', s).digest()

print(codecs.encode(s, 'hex').decode("utf-8"))
print(codecs.encode(r, 'hex').decode("utf-8"))
输出公钥 907ee8b73f268afa5fccabeaaf17c3d49b3559a3 符合预期。
```shell
01634d164eb397dde916405580e0f6fe0f3dc0b647f7568d29d5f824e138bac2
907ee8b73f268afa5fccabeaaf17c3d49b3559a3
```
2）验证签名：简单的说，使用一个私钥签名的信息，只有使用对应的公钥才能验证通过。从而保证了安全，其它人无法知道"A"的私钥，无法伪造其签名，也就不可能偷走x的资金。

# getblock
bitcoin-cli getblock 3aa6bdbd800309fb4bd423375fb7bc51d3d6f07c126ca26061406a46f22f4ed1 1
{
  "hash": "3aa6bdbd800309fb4bd423375fb7bc51d3d6f07c126ca26061406a46f22f4ed1",
  "confirmations": 101,
  "height": 1,
  "version": 536870912,
  "versionHex": "20000000",
  "merkleroot": "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2",
  "time": 1714474026,
  "mediantime": 1714474026,
  "nonce": 4,
  "bits": "207fffff",
  "difficulty": 4.656542373906925e-10,
  "chainwork": "0000000000000000000000000000000000000000000000000000000000000004",
  "nTx": 1,
  "previousblockhash": "0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206",
  "nextblockhash": "71144bceb7d339d782dda2ab7d13df630e399cb31a4b6d18f4be474d9cacd4c5",
  "strippedsize": 212,
  "size": 248,
  "weight": 884,
  "tx": [
    "921a6cf8e083b57b9a63067aa0ab16ed4679929dc874b4af8fb229f7f48b9aa2"
  ]
}


# 挖矿
    再执行一次挖矿操作
  bitcoin-cli -rpcwallet=walletname0430 -generate 1
```json
{
  "address": "bcrt1qdlss0v7gg7xs0wuvtnqkwtyz6xlp0d86f2pv0x",
  "blocks": [
    "17b3b19342d1d9c6416c797a3627a6ecbd08d015a478ea98a70cd542a393cd07"
  ]
}
```
# 挖矿
bitcoin-cli -rpcwallet=walletname0430 -generate 200
bitcoin-cli -rpcwallet=walletname0430 listunspent
bitcoin-cli -rpcwallet=walletname0430 getbalance
8765.00000000
bitcoin-cli -rpcwallet=walletname0430 -generate 200
bitcoin-cli -rpcwallet=walletname0430 getbalance
12477.50000000