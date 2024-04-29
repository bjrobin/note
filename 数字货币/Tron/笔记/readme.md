# 官方文档
https://developers.tron.network/docs/getting-start


https://blog.csdn.net/yqq1997/article/details/116781966
curl --request GET --url https://api.trongrid.io/v1/accounts/TPcUx2iwjomVzmX3CHDDYmnEPJFTVeyqqS/transactions
# 申请
    https://www.trongrid.io/
    100,000 Requests / Day
    3 API Keys
# 启动Java-tron节点

# TRX和TRC10交易三种合约
    https://blog.csdn.net/linzhiji/article/details/124961242
    在TRON中检测TRX或TRC10事务涉及3种类型的合约：

    TransferContract （系统合同类型）
    TransferAssetContract （系统合同类型）
    TriggerSmartContract （智能合约类型）

# 类型
## TransferContract （系统合同类型） 普通TRX交易
```json
    {
      "ret": [{ "contractRet": "SUCCESS" }],
      "signature": [
        "76bdf73cbd0b5291f01e4b16689742a52a0d0d285b7a11797a265f6bde233822d4a66b98c9b66891a57a9e320208b86285cd2986db34226371cb9c7fb055577000"
      ],
      "txID": "828d6f0eb9a386fadff2099979f935cb29487ef0cb9f7e3c8c36a4745d2fa94d",
      "raw_data": {
        "contract": [
          {
            "parameter": {
              "value": {
                "amount": 3500000, //转账金额
                "owner_address": "TLuNzZoViQ5dKnAYTUxSc3EiaUyREwfrRx",//发送地址
                "to_address": "TBgCKA38iNv8a8LQ6F8fxkKh77Zivxxxxx"//接收地址
              },
              "type_url": "type.googleapis.com/protocol.TransferContract"
            },
            "type": "TransferContract"
          }
        ],
        "ref_block_bytes": "49ae",
        "ref_block_hash": "1e1206224e6eb8f2",
        "expiration": 1713150564000,
        "timestamp": 1713150504407
      },
      "raw_data_hex": "0a0249ae22081e1206224e6eb8f240a0adecfded315a68080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a154177f00f6d72aff8f2ae48a90bbe6cb80ae4f51ace12154112b89b1e08a6d20f63e366e80f1f131a5449648618e0cfd50170d7dbe8fded31"
    }
```
## TransferAssetContract （系统合同类型）
```json
{
      "ret": [{ "contractRet": "SUCCESS" }],
      "signature": [
        "85d810d6a3db3fe2e99c011f5c9d1aba0680cb72e38f7decf82eb317a76bf42a1a09618d71de408204f61794cdbdb81e7cd3b2535a9e9ee87a30ee610b2b5e8a00"
      ],
      "txID": "dd860f6352121983bc2c4e8c533a9b5450b45280f09ed257a7402007a6c2e39d",
      "raw_data": {
        "contract": [
          {
            "parameter": {
              "value": {
                "amount": 888888888,
                "asset_name": "1004937",
                "owner_address": "TBaKHGyPrncojNoyeVqirb8Hs69kZQAqFT",
                "to_address": "TDRkHLDxnBu2XtkxwKZMm5qwSuguKHmWDB"
              },
              "type_url": "type.googleapis.com/protocol.TransferAssetContract"
            },
            "type": "TransferAssetContract"
          }
        ],
        "ref_block_bytes": "49ae",
        "ref_block_hash": "1e1206224e6eb8f2",
        "expiration": 1713150564000,
        "timestamp": 1713150504815
      },
      "raw_data_hex": "0a0249ae22081e1206224e6eb8f240a0adecfded315a77080212730a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e736665724173736574436f6e7472616374123d0a0731303034393337121541119bed28701f5e0c456a2066e1e7d5eed4bec70b1a154125ed4dd73d479a070af49b23e54d9d003c2039a420b8bceda70370efdee8fded31"
    }
```
## TriggerSmartContract （智能合约类型） TRC20交易
```json
    {
      "ret": [{ "contractRet": "SUCCESS" }],
      "signature": [
        "3cf4d8f1f92f03489dad996982d6820839301ec3fb0e30a9fae9c6dffac113d84a3631e47153e4d860f02a3e3410b52b2ae7bed9026580c884775fd3335196f501"
      ],
      "txID": "79a6ff01cf794933b955f492503b49092ba124777e9017cc2b925373d6824bfb",
      "raw_data": {
        "contract": [
          {
            "parameter": {
              "value": {
                //其中的 data的组成和 ERC20转账完全一样
                //其中TRC20的接受者地址是不带41的十六进制字符串格式, 即和ETH地址完全一样, 所以, 在转换为 Base58格式的地址形式时需要加上41的前缀.
                "data": "a9059cbb000000000000000000000000c686c48436aec3a1dfce4ac5a4526c39366985ba000000000000000000000000000000000000000000000000000000001b898f80"//函数签名(4字节) + 接受者地址(32字节)  + 金额(32字节)
                "owner_address": "TThvaA82HGM62bveyhmbxqiKKDWWHkVWaX",
                "contract_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
              },
              "type_url": "type.googleapis.com/protocol.TriggerSmartContract"
            },
            "type": "TriggerSmartContract"
          }
        ],
        "ref_block_bytes": "49a8",
        "ref_block_hash": "caec48a9c126cf6e",
        "expiration": 1713157632000,
        "fee_limit": 75600000,
        "timestamp": 1713150498062
      },
      "raw_data_hex": "0a0249a82208caec48a9c126cf6e4080e09b81ee315aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541c28e4f675164a461cfac877bbf77180595e33f93121541a614f803b6fd780986a42c78ec9c7f77e6ded13c2244a9059cbb000000000000000000000000c686c48436aec3a1dfce4ac5a4526c39366985ba000000000000000000000000000000000000000000000000000000001b898f80708eaae8fded31900180a18624"
    }
```
# 参考
## 波场归集充值回调（trx/trc10/trc20版本整合）
    https://blog.csdn.net/sail331x/article/details/114765892

    TRX转账功能
    TRC20转账功能
    TRC10转账功能

## 波场协议
    https://github.com/tronprotocol/documentation/tree/master/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3/%E6%B3%A2%E5%9C%BA%E5%8D%8F%E8%AE%AE