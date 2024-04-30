

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
#local testnet
fallbackfee=0.0001
datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0/data

# https://blog.web3idea.xyz/post/blockchain%2Fbitcoin%2FOrdinal+BitcoinTestNetwork
# /Users/lhqer/MY/2024/data/bitcoin-25.0/bin/bitcoind -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0
# /Users/lhqer/MY/2024/data/bitcoin-25.0/bin/bitcoin-cli -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0 stop
# vi ~/.bash_profile 
# export PATH=$PATH:/Users/lhqer/MY/2024/data/bitcoin-25.0/bin
# source ~/.bash_profile
# bitcoind --help 


# 错误
bitcoin-cli -regtest createwallet walletname0430
error: Could not locate RPC credentials. No authentication cookie could be found, and RPC password is not set.  See -rpcpassword and -stdinrpcpass.  Configuration file: (/Users/lhqer/Library/Application Support/Bitcoin/bitcoin.conf)

# 启动
    bitcoind -conf=/Users/lhqer/MY/2024/data/bitcoin-25.0/bitcoin.conf -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0
    bitcoind -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0
# 停止
    bitcoin-cli -conf=/Users/lhqer/MY/2024/data/bitcoin-25.0/bitcoin.conf -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0 stop
    bitcoin-cli -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0 stop

# 参考
创建本地比特币网络regtest，手工创建交易，极速理解比特币原理
https://zhuanlan.zhihu.com/p/592586339

# createwallet
其实这里钱包的公钥和私有就已经生成好了。
bitcoin-cli -conf=/Users/lhqer/MY/2024/data/bitcoin-25.0/bitcoin.conf -regtest -datadir=/Users/lhqer/MY/2024/data/bitcoin-25.0 createwallet walletname0430
{
  "name": "walletname0430"
}
# 检查钱包
可以看到，初始状态，钱包余额、可用余额、交易数量等都是0
bitcoin-cli -conf=/Users/lhqer/MY/2024/data/bitcoin-25.0/bitcoin.conf -regtest getwalletinfo
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
# 将bitcoin.conf复制到/Users/lhqer/Library/Application Support/Bitcoin/
# 挖矿
bitcoin-cli -regtest -generate 100
下面来创建100个区块，也就是挖矿，一下子挖100个区块出来。这里是本地环境，很快就能完成。不像真实的比特币网络，大量的矿场竞争比算力竞争，谁先挖到算谁的。
输出：
{
  "address": "bcrt1qhk2wdr07u358hkp7cn2k05lah6wrtaga66llum",
  "blocks": [
    "78bb917f07b38d8735488fe73e24d0c52d15f7dc3f1fd5929790a422d1b83048",
    "07db2835212607990babf4cd1b85a908a8cb66193ec30066e5cb2011424ee0c7",
    "32b9f6604778ffc3a7701c65ce1f8bd8ee90138251358c418350f30f45753d42",
    "500469483977395bec722625f6ae659bf31e71e2953e40969114b261f6eeddfc",
    "4ddadc68fccd48174dccb56d3ede10e695f6708106092718fa2d04c4d1d0be3e",
    "53f43c91fcd4412b91e2d80d93443a91d80cfc6a7c657a429c9d03c922e6074e",
    "185cc3635bcda4d8a675154473d0e8e1bf7d92f520f38ae96f360d6a4792a440",
    "0a7ca4e6441dda0a8167f561264c351975de83677f5fb6fd9d656b1a6f0b8f89",
    "64ca102587b7a2ca18490c91b6e83d27d04e1a7074a77eaadd76344331220689",
    "474a44f309a92cb85d6a4176f52bb35021aee115de4dca2aae13b7c87e3b40ca",
    "5951f0a9a40b252ea593b46f8099e112534e369f28283b7398c70fef99b771bc",
    "6ab5cb71a6b154e37875175f7eb1ae9a56585e0d2a28efec5893dc9ca90461f9",
    "354505f2a5ed5a42a699f3d1ff2753cd5744830786a84c2bdf8c522b2dbba677",
    "54b1365d6a61fde8d48291319aeefc8a618d46958e23c7aa71fc70c11f170afb",
    "0147681aaf15271feeff8dcd50434e9586e6d59d1e8b2f9559d32f22c22d4ff2",
    "4d6155ec6c0f5c59d46d8513e89661e9073ed97a1eabbedc0bc256f9f86ed863",
    "2eb2d83a232e6d9f01cc5133089f1a256437f9bd8d5913a43951ef0435c075b4",
    "5d37d0fd087135e17806563102396b1bb8393b043f3c66f356cae1f4c60e23ff",
    "74f57cd5b15e815ed03407e5e99bb860b3835e9663e065096ec913645bcc063c",
    "0aee9cd146236f03fb64dafc6e98b6fef8675cbaf00b43c46543fe4491e640ac",
    "766e2ce3f077552da30f318bdfd705e64e355b81ca2116238235b3313fe815ad",
    "438390cd7f0a68b40df7d628c152751027fa5c9c74ab4f57c970b1909897c2e2",
    "461de440aeb81fde7e9a81daa145fa941560701e401c2fdeafda77ad4695db2d",
    "3940cfe8187d8b1765f1bf4da3af094ed63d655553c2a6c95295216be8910433",
    "48ff9775419ff8576be77c0d0e3d8c933befb86ad686a1040c0745c379994325",
    "05d51bef94772b3091a96b177a734167e7e6f661805f997ccdfead7db0705cbb",
    "6ca51cd7493c6ec4352b345cc5233998592f2594d918bfaa2a4e26baee9d8a54",
    "03729721e13ed8e007b41f621e19fa276d4a46c4c295d1e93c32cca13bb48171",
    "7c7569853c3742685b4dcf5c0a9a731c72e3a7fb173ce92f262f4e2d9a9864ec",
    "58fbeefbe0c9a085f65dca3da935c84f709bcb636fb8f2b0d60ec0cb7e3e6b02",
    "1364651e98e33c8819b572ee9d063e9e0e28d9cf8b0065eecc1b28ecd30840e6",
    "2a25dd9fd87ad29cea1400c88b56d34826b2fce2c2b209930c2b773bf367c4e7",
    "67a4b6ac4a36798dd96e72aada4d436eac3dd94d3fec22cd03e34703ffbc6349",
    "58a5aeb6f1a5d4432726722e4540f05e92d2d69f5350b995cfbc0bec5a54f62d",
    "41a8973f7dff33845f47dc0b885cc171e0f33197ad6f693d3395c7f493bb35a3",
    "1c2633567235192f4b2b6ef6aa1cea31553b0d54809f11711d9f35b3ca328981",
    "69efd8bf1824eabd815fe646ef312f96c3f35e7cd7edf937931e9a7de95ce120",
    "1fc2d2a9bf3bfffd6513719157eb31046c9c12f8993f4added6f2f1aa4247e71",
    "118017772cba47b6e7989186a26225a55dd2032f22234623e8193aeb85e8ff50",
    "302d8301ef72730be245315e10d94cde0ffeac6ecc3ae223691fe9a2de738ae5",
    "1ca6b24f9106b5df2de8563ede57fbaa24c4c602303ae029ad707effd89cd199",
    "59c461e2ad32874f152329719031ff848f16cc36a78e94deca13b7cc6ac2c9ee",
    "0ef6877aac0f45ec46dde805cdb4b284b66381356593d58c1bb7a5e52b152cd9",
    "55ab3912b8bd9520c85687789510182eb9e4dd578426c18b7f7c955ddf7c10db",
    "6e0287225f0a03a2756421ba6b0d77ef771dbd0f0086691bb230a42343ecff4f",
    "30695d96d3edeede02c74870ca0f574a118e5592b23b52bee51b44dae65e8084",
    "1e972912f8089254fb656c5a908f7364676cd7bb7e202d195a8b381c646b4f06",
    "37041d92b88dc7c25a41a1f54b7428984ed6c58681959113256b7b7c14262976",
    "1810b9d6ba1ee274ffc1b26115af2bba2d454c90e8620bdcca82eb4958ca37f8",
    "312c4d555f35167043d29bdd48e1d13bb1fbbe393bc9bdd69d2f44eaa7c3a3f1",
    "4cce6f99180e72a567078766ac8a30194f6976b32a54bc086e36aa762e46b2ce",
    "7800d80496df796da6b35921091380b3b2dd7bea82df8eb9aaa134cd17dbf318",
    "43bfbc4ee54bc41670d1536adb8f3917f023875c362206f8fd955a9681aab264",
    "449e6b7126f1ca93cddc9b8b84fa1516445cfa35743b4c98660e11db59e3d23f",
    "339fb70a419a7e13cd7b1778bbf0b41bfc03b6ed9d5dddc0218aa1853a7617eb",
    "3ed50380a3171c68fc01850c4d490088b87fc9394c8cbb5084571d49b1035cb1",
    "2e20dab3ed0d66f2b26ef15c2417ecb6d8e0f3487be46706b1ea33399890fd33",
    "108910c5ac36b93c9ea98e65f8efd66b0c9ef8637cf52c74ace95f1fdaaf35d9",
    "770d45d70c36be48ae9705b8544ac0f5499989e8f947b660c614f9d493ba077c",
    "5168033397fba579207c14e88958b2b666644d6131351e5ad03344c0c8b3780f",
    "1b7b68b8513455bdac15872090ccbfcff7501c085a2a7f9657d5542433d2b4ac",
    "2a957c5f1815a0e03bfbdbdb1ff403428bec083231193bf5e2c355a15de2c330",
    "0f5ad37935befcecbafa5ef1282652c3125d4582b2c6c79234264ef5ecc2c809",
    "0f178c6175b141fcb36b768195fe2c4368bf37f228fd1523fa101856664ac7de",
    "68c465a910add69e82c8aa4bb4619ddb7d37d32a81880487f1ba4eff7f7d5863",
    "2c3ec889744fdc066ce3d742f4e9089533188253e37859037c626f01602ecd70",
    "0705aaadc008bc23a3914dbf96c857a681078dd6c9fb9d566768ce2c688d8b41",
    "3ea4ee356f00b01358ca0e7408cffc0a7176d718e9f70ed3dc0a431cda04d1a3",
    "593e7dcf2127fbd8f7fb8e311954c085b6a6131ca2fd1ce49e5ea1b8e6a7699a",
    "26e5bf4da94f6d28e5f85b01db915682f1dda90a3e0abf6291061f36ecb9c8fb",
    "2e4bb8367b3daf9a86838bb0bf56162984aa28d85b713ed7ea4aa383614c6fbc",
    "17d67263c00714e43c43d8d2f95efc216a679b623f57d608c31398236dbdda1e",
    "59b255a5c8e853cc56d3ddc28d1f09052e4d1fedb713545f40418f3d685e137e",
    "49ba379be41f62bc43e1234f993e83651b49a9cf837fb83153749adf951de492",
    "01f17f45206c118844c0629b75ad4a876f8c8c57c1a1071799b6dfb8e2e701c4",
    "26b4f67bc34dde379562ed67e4ded547dd6910cc9fec241935342029b68d4fd6",
    "6fc695bb57575ba3c88357557aa7005a419c9383a11a2a75e7e77c999ff5e534",
    "526450f38d8edac385caa17472c4afdff2009418fab4a2d30c5088c5898725d6",
    "5a3a2b0ac635f80aaeef4270d8a69889240f350ded25a5e9d5bda0d37127c6e3",
    "281f553e9dccef6d8217db146bab67e3d1c5c31484478481a1333353a1c0ba5d",
    "7dcfeabcc41886d7fc79db5f94581ffa8583ffe7587561e3f703634716ff323d",
    "1d43fa8cff0c593539808773347a660097194dec1e2a0f42c1f676bac7145977",
    "1323d531db7cc59e6ea82d19c531625b211ec9730c0ea55729dba6980f6e5992",
    "6de3a5f2fd3b78d2a4ecb528cb7255ea2df94f96b5f9bf3bf5d0ed30fb9108c6",
    "6e2636a85223093f469caa6e31902cf4faedba189ee84b29bc029fa0f4889b46",
    "0135e6774a8d14175cb7f25802389b6415aad304058e42929b8776a2c238966c",
    "621dc0438075bee0c05337bc5aa63530cce092573a5939a337d0f6dcff179cfd",
    "07d26e6ab0f3ced67ae8b8b0e9f3172e5faea5ea14afdfc36176103abd8b1469",
    "53607d0bee287e11b6afce58fd08b15d6c1446c7bba70992053e370a4152cf3e",
    "3489febcecfb00f9c469bfb35c11a79878036b1e8ed837de9e9c61d10764c482",
    "4a07ba7750c5f8b8bf561ad10296b4a245f6438d6e2dd2736858980345fc9c36",
    "503ba0a775e5369a6ee5eebdb9efbf7c33af69a6021b1e4268da71eb24cfd9e0",
    "416722295536781e5a7035ff4b9e0e70d6919b45b8bb996c70ab352fe7631bed",
    "733c58a7c9a832c70098ed12fa78387048e16b95fed8c2d7e66fa58fcad238c0",
    "6a62e8d3c8a7096c23dd0c8b25839a38ccca79cc135ed12d97db19eb0d9b22d4",
    "0f8e4f0523d90a1d2c3aa882592da352b4f1ddf0f35daaccb9b83f119e27efb9",
    "1bb35776bed72ad0f69d00570c4bd6fcb6790aaf7449ebaf0317e826f60b51f8",
    "6ad93f2eb83601e0e1b6f0e087e7ab44b8322bf6a0669a039d03a9f429b7afae",
    "697c68f5df3912015c58a87897dba2692a84d76ce7c596a7cfcc1511f8d30cce",
    "6a9b1a23be612790dd171db9e66d9e91b98deb31e039c2b846626273acf99465"
  ]
}

# 检查钱包
bitcoin-cli -regtest getwalletinfo
之前：
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
之后：
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
需要注意的是：balance为0，immature_balance为5000。这是因为区块奖励需要在101次确认之后才变为可用状态。

# 挖矿
bitcoin-cli -regtest -generate 1
{
  "address": "bcrt1q0wrxsvjh4y94v9rjupq5nu0uwff2grj28s942x",
  "blocks": [
    "46e07c0f2a99d8cdfafdd272419e3f44395b23cf4348b3a3e34849ba7a736df3"
  ]
}
# 再次检查钱包
可以看到可用余额balance变为了50。
bitcoin-cli -regtest getwalletinfo
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
# listunspent
使用listunspent指令显示未花交易输出USXOs也能印证：
bitcoin-cli -regtest listunspent 
[
  {
    "txid": "7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7",
    "vout": 0,
    "address": "bcrt1qhk2wdr07u358hkp7cn2k05lah6wrtaga66llum",
    "label": "",
    "scriptPubKey": "0014bd94e68dfee4687bd83ec4d567d3fdbe9c35f51d",
    "amount": 50.00000000,
    "confirmations": 101,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec4e9e9a/84'/1'/0'/0/0]03b1ab5fe25b3b558ec434932a9b6813d49ad5f789aee95159ba9d7e3e99020bfb)#rvxtdmp6",
    "parent_descs": [
      "wpkh(tpubD6NzVbkrYhZ4Wkz2XSMCgp4kgWF8NXpwJgAAN1CZHnywonhzww1j7Eedcqe1ejWBi7noRzQv1TLnQfdHAD47ZtNTcEMq54YYs9Bzi1YeL1h/84'/1'/0'/0/*)#np6hpv0t"
    ],
    "safe": true
  }
]
# gettransaction
这里的金额是从哪里来的？就是那个挖100个区块，其中的第一个区块！后面挖了101次（包括后面刚刚单独generate加了一次），所以就确认了。马上验证一下：

根据txid，使用gettransaction查询
bitcoin-cli -regtest gettransaction 7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7
{
  "amount": 50.00000000,
  "confirmations": 101,
  "generated": true,
  "blockhash": "78bb917f07b38d8735488fe73e24d0c52d15f7dc3f1fd5929790a422d1b83048",
  "blockheight": 1,
  "blockindex": 0,
  "blocktime": 1714463074,
  "txid": "7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7",
  "wtxid": "4d5193ed7d032982f84bf7222ebb945f2ed6c88f24e5197c44a4d229eb0947c4",
  "walletconflicts": [
  ],
  "time": 1714463074,
  "timereceived": 1714463074,
  "bip125-replaceable": "no",
  "details": [
    {
      "address": "bcrt1qhk2wdr07u358hkp7cn2k05lah6wrtaga66llum",
      "parent_descs": [
        "wpkh(tpubD6NzVbkrYhZ4Wkz2XSMCgp4kgWF8NXpwJgAAN1CZHnywonhzww1j7Eedcqe1ejWBi7noRzQv1TLnQfdHAD47ZtNTcEMq54YYs9Bzi1YeL1h/84'/1'/0'/0/*)#np6hpv0t"
      ],
      "category": "generate",
      "amount": 50.00000000,
      "label": "",
      "vout": 0
    }
  ],
  "hex": "020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff025100ffffffff0200f2052a01000000160014bd94e68dfee4687bd83ec4d567d3fdbe9c35f51d0000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf90120000000000000000000000000000000000000000000000000000000000000000000000000"
}
可以看到blockhash为： 78bb917f07b38d8735488fe73e24d0c52d15f7dc3f1fd5929790a422d1b83048

之前挖100个区块的指令，其输出第一个hash不就是这个嘛！

那么，如果继续generate挖矿，区块奖励继续得以确认，钱包balance也会相应的增加。动手试试吧~
# 创建一个新的钱包
下面创建一个新的钱包，试验一下多个钱包间转账
bitcoin-cli -regtest createwallet walletname0430-1
{
  "name": "walletname0430-1"
}
# 查询钱包
    现在我们有两个钱包了， walletname0430 和 walletname0430-1
    bitcoin-cli -regtest -rpcwallet=walletname0430 listunspent
    bitcoin-cli -regtest -rpcwallet=walletname0430-1 listunspent
# 装载钱包
bitcoin-cli -regtest loadwallet walletname0430
bitcoin-cli -regtest loadwallet walletname0430-1

# 创建地址
我们准备从 walletname0430 钱包给 walletname0430-1 钱包转10个比特币。

注意：首先，需要给 walletname0430-1 创建地址，没有地址就没法收款，这个与现实中体验是一致的，很好理解。
bitcoin-cli -rpcwallet=walletname0430-1 getnewaddress 
bcrt1qg87lnrz5ky36xszftlmjsnj6xu5cxfvzdltp4j

# 从B钱包转，

    bitcoin-cli -rpcwallet=walletname0430-1 sendtoaddress bcrt1qh83qc3lrsayw0fepr78xx2qg7cvqll6q59sdat 10
    马上报错说余额不足了。符合预期。
    error code: -6
    error message:
    Insufficient funds
# 从A钱包转
bitcoin-cli -rpcwallet=walletname0430 sendtoaddress bcrt1qh83qc3lrsayw0fepr78xx2qg7cvqll6q59sdat 10 
返回交易txid
300c1b0e7aeaa6aca34728c37d047c6c9f12f815485b78aa3f932918d309399c
# gettransaction
bitcoin-cli -rpcwallet=walletname0430 gettransaction 300c1b0e7aeaa6aca34728c37d047c6c9f12f815485b78aa3f932918d309399c true true
最后一个true参数表示显示decode信息
```json
{
  "amount": -10.00000000,
  "fee": -0.00001410,
  "confirmations": 0,
  "trusted": true,
  "txid": "300c1b0e7aeaa6aca34728c37d047c6c9f12f815485b78aa3f932918d309399c",
  "wtxid": "40769c449078a9107b8e2e314fff93090a986aeeeacc057c84ae700a9195d017",
  "walletconflicts": [
  ],
  "time": 1714468813,
  "timereceived": 1714468813,
  "bip125-replaceable": "yes",
  "details": [
    {
      "address": "bcrt1qh83qc3lrsayw0fepr78xx2qg7cvqll6q59sdat",
      "category": "send",
      "amount": -10.00000000,
      "vout": 0,
      "fee": -0.00001410,
      "abandoned": false
    }
  ],
  "hex": "02000000000101b774eb3d083c9a81ab6a8d89f0bd423b19bf82217640a6405e64a3e284705a7b0000000000fdffffff0200ca9a3b00000000160014b9e20c47e38748e7a7211f8e632808f6180fff407e226bee000000001600148b23cd537fc58a96a61c5712a10eaa11754041e2024730440220554a44b5518dd10fb60a0e39417d3ba1f193f497632438eceb7944c842812a69022046ac66624eb37a35eab7a8ee837e8a5465d1c38ff76fe3496e04c8a7d02a7a39012103b1ab5fe25b3b558ec434932a9b6813d49ad5f789aee95159ba9d7e3e99020bfb65000000",
  "decoded": {
    "txid": "300c1b0e7aeaa6aca34728c37d047c6c9f12f815485b78aa3f932918d309399c",
    "hash": "40769c449078a9107b8e2e314fff93090a986aeeeacc057c84ae700a9195d017",
    "version": 2,
    "size": 222,
    "vsize": 141,
    "weight": 561,
    "locktime": 101,
    "vin": [
      {
        "txid": "7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7",
        "vout": 0,
        "scriptSig": {
          "asm": "",
          "hex": ""
        },
        "txinwitness": [
          "30440220554a44b5518dd10fb60a0e39417d3ba1f193f497632438eceb7944c842812a69022046ac66624eb37a35eab7a8ee837e8a5465d1c38ff76fe3496e04c8a7d02a7a3901",
          "03b1ab5fe25b3b558ec434932a9b6813d49ad5f789aee95159ba9d7e3e99020bfb"
        ],
        "sequence": 4294967293
      }
    ],
    "vout": [
      {
        "value": 10.00000000,
        "n": 0,
        "scriptPubKey": {
          "asm": "0 b9e20c47e38748e7a7211f8e632808f6180fff40",
          "desc": "addr(bcrt1qh83qc3lrsayw0fepr78xx2qg7cvqll6q59sdat)#2ntq5wq0",
          "hex": "0014b9e20c47e38748e7a7211f8e632808f6180fff40",
          "address": "bcrt1qh83qc3lrsayw0fepr78xx2qg7cvqll6q59sdat",
          "type": "witness_v0_keyhash"
        }
      },
      {
        "value": 39.99998590,
        "n": 1,
        "scriptPubKey": {
          "asm": "0 8b23cd537fc58a96a61c5712a10eaa11754041e2",
          "desc": "addr(bcrt1q3v3u65mlck9fdfsu2uf2zr42z965qs0zxtfxal)#ve9022qc",
          "hex": "00148b23cd537fc58a96a61c5712a10eaa11754041e2",
          "address": "bcrt1q3v3u65mlck9fdfsu2uf2zr42z965qs0zxtfxal",
          "type": "witness_v0_keyhash"
        }
      }
    ]
  }
}
```

vin中txid：指的是本次交易的输入交易的id。即本次转账的金额来源： 7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7
查看一下这个交易：

bitcoin-cli -rpcwallet=walletname0430 gettransaction 7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7 true true
```json
{
  "amount": 50.00000000,
  "confirmations": 101,
  "generated": true,
  "blockhash": "78bb917f07b38d8735488fe73e24d0c52d15f7dc3f1fd5929790a422d1b83048",
  "blockheight": 1,
  "blockindex": 0,
  "blocktime": 1714463074,
  "txid": "7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7",
  "wtxid": "4d5193ed7d032982f84bf7222ebb945f2ed6c88f24e5197c44a4d229eb0947c4",
  "walletconflicts": [
  ],
  "time": 1714463074,
  "timereceived": 1714463074,
  "bip125-replaceable": "no",
  "details": [
    {
      "address": "bcrt1qhk2wdr07u358hkp7cn2k05lah6wrtaga66llum",
      "parent_descs": [
        "wpkh(tpubD6NzVbkrYhZ4Wkz2XSMCgp4kgWF8NXpwJgAAN1CZHnywonhzww1j7Eedcqe1ejWBi7noRzQv1TLnQfdHAD47ZtNTcEMq54YYs9Bzi1YeL1h/84'/1'/0'/0/*)#np6hpv0t"
      ],
      "category": "generate",
      "amount": 50.00000000,
      "label": "",
      "vout": 0
    }
  ],
  "hex": "020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff025100ffffffff0200f2052a01000000160014bd94e68dfee4687bd83ec4d567d3fdbe9c35f51d0000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf90120000000000000000000000000000000000000000000000000000000000000000000000000",
  "decoded": {
    "txid": "7b5a7084e2a3645e40a640762182bf193b42bdf0898d6aab819a3c083deb74b7",
    "hash": "4d5193ed7d032982f84bf7222ebb945f2ed6c88f24e5197c44a4d229eb0947c4",
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
          "asm": "0 bd94e68dfee4687bd83ec4d567d3fdbe9c35f51d",
          "desc": "addr(bcrt1qhk2wdr07u358hkp7cn2k05lah6wrtaga66llum)#qnhke557",
          "hex": "0014bd94e68dfee4687bd83ec4d567d3fdbe9c35f51d",
          "address": "bcrt1qhk2wdr07u358hkp7cn2k05lah6wrtaga66llum",
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


这里，我们仔细分解一下比特币交易的过程具体如何进行。
可以看到：x挖矿得到的50个比特币（交易e0235...457f），作为x转账给B（交易8af1...3f2b）的资金来源。

更确切的说：交易e0235...457f的输出，相当于提出了一道【题目】，题目中包含了x的公钥hash:75e090f30d013934836bd5b6668c58c34ae7c11d；而在真正需要使用这笔资金的时候，在交易8af1...3f2b中，需要去给出【答案】，即在其输入中，txinwitness，第一个值为x的签名，第二个值为公钥。

然后，根据题目要求，使用答案去验证：

1）双重hash验证公钥：把本次交易提供的public key做两次hash运算RIPEMD160(SHA256(pubKey)) 与上次交易（题目中）的公钥hash比对。这里用python来计算验证一下。

import hashlib
import codecs

publickey = codecs.decode('038d5b9221e12fe27fade96f3c2ca72c53c587508206a13b6bfdaafc01494a12ad', 'hex')
s = hashlib.new('sha256', publickey).digest()
r = hashlib.new('ripemd160', s).digest()

print(codecs.encode(s, 'hex').decode("utf-8"))
print(codecs.encode(r, 'hex').decode("utf-8"))
输出公钥 75e090f30d013934836bd5b6668c58c34ae7c11d 符合预期。

e748b8d993a8e4d947989e7515ae50b44afec8440328b296ca84d11ed6809949
75e090f30d013934836bd5b6668c58c34ae7c11d
2）验证签名：简单的说，使用一个私钥签名的信息，只有使用对应的公钥才能验证通过。从而保证了安全，其它人无法知道x的私钥，无法伪造其签名，也就不可能偷走x的资金。