GetBlock for Developers
https://getblock.io/docs/

Bitcoin Transactions
https://aandds.com/blog/bitcoin-tx.html#7cd69889


== Blockchain ==
## getbestblockhash
返回最优链上最近区块的哈希
## getblock "blockhash" ( verbosity )
返回具有指定哈希的区块
## getblockchaininfo
返回区块链当前状态信息
## getblockcount
返回本地最优链上的区块数量
https://getblock.io/docs/btc/json-rpc/btc_getblockcount/
## getblockfilter "blockhash" ( "filtertype" )
## getblockfrompeer "blockhash" peer_id
## getblockhash height
返回本地最有区块链上指定高度区块的哈希
## getblockheader "blockhash" ( verbose )
返回指定区块头
## getblockstats hash_or_height ( stats )
## getchaintips
返回每个本地区块链的最高位区块（tip）信息
## getchaintxstats ( nblocks "blockhash" )
## getdeploymentinfo ( "blockhash" )
## getdifficulty
返回POW难度
## getmempoolancestors "txid" ( verbose )
返回交易池内指定交易的所有祖先
## getmempooldescendants "txid" ( verbose )
返回交易池内指定交易的所有后代
## getmempoolentry "txid"
返回交易池内指定交易的池数据
## getmempoolinfo
返回交易池信息
## getrawmempool ( verbose mempool_sequence )
返回交易池内的所有交易
## gettxout "txid" n ( include_mempool )
返回指定交易输出的详细信息
## gettxoutproof ["txid",...] ( "blockhash" )
返回一个或多个交易的证明数据
## gettxoutsetinfo ( "hash_type" hash_or_height use_index )
返回UTXO集合的统计信息
## gettxspendingprevout [{"txid":"hex","vout":n},...]
## preciousblock "blockhash"
## pruneblockchain height
对区块链执行剪枝操作
## savemempool
## scanblocks "action" ( [scanobjects,...] start_height stop_height "filtertype" "options" )
## scantxoutset "action" ( [scanobjects,...] )
## verifychain ( checklevel nblocks )
验证本地区块链的每个记录
## verifytxoutproof "proof"
验证交易输出证明

== Control ==
## getmemoryinfo ( "mode" )
## getrpcinfo
返回Rpc服务器详情
## help ( "command" )
返回所有可用的RPC命令，或返回指定命令的帮助信息
## logging ( ["include_category",...] ["exclude_category",...] )
## stop
安全关闭bitcoin core的节点服务
## uptime

== Mining ==
## getblocktemplate ( "template_request" )
返回节点模板
## getmininginfo
返回挖矿相关信息
## getnetworkhashps ( nblocks height )
返回估算的全网哈希速率
## prioritisetransaction "txid" ( dummy ) fee_delta
交易优先权
## submitblock "hexdata" ( "dummy" )
提交区块
## submitheader "hexdata"

== Network ==
## addnode "node" "command"
## clearbanned
## disconnectnode ( "address" nodeid )
## getaddednodeinfo ( "node" )
## getconnectioncount
## getnettotals
## getnetworkinfo
## getnodeaddresses ( count "network" )
## getpeerinfo
## listbanned
## ping
## setban "subnet" "command" ( bantime absolute )
## setnetworkactive state

== Rawtransactions ==
## analyzepsbt "psbt"
## combinepsbt ["psbt",...]
## combinerawtransaction ["hexstring",...]
## converttopsbt "hexstring" ( permitsigdata iswitness )
## createpsbt [{"txid":"hex","vout":n,"sequence":n},...] [{"address":amount,...},{"data":"hex"},...] ( locktime replaceable )
## createrawtransaction [{"txid":"hex","vout":n,"sequence":n},...] [{"address":amount,...},{"data":"hex"},...] ( locktime replaceable )
## decodepsbt "psbt"
## decoderawtransaction "hexstring" ( iswitness )
## decodescript "hexstring"
## finalizepsbt "psbt" ( extract )
## fundrawtransaction "hexstring" ( options iswitness )
## getrawtransaction "txid" ( verbosity "blockhash" )
No such mempool transaction. Blockchain transactions are still in the process of being indexed. Use gettransaction for wallet transactions.
## joinpsbts ["psbt",...]
## sendrawtransaction "hexstring" ( maxfeerate maxburnamount )
## signrawtransactionwithkey "hexstring" ["privatekey",...] ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )
## testmempoolaccept ["rawtx",...] ( maxfeerate )
## utxoupdatepsbt "psbt" ( ["",{"desc":"str","range":n or [n,n]},...] )

== Signer ==
## enumeratesigners

== Util ==
## createmultisig nrequired ["key",...] ( "address_type" )
## deriveaddresses "descriptor" ( range )
## estimatesmartfee conf_target ( "estimate_mode" )
## getdescriptorinfo "descriptor"
## getindexinfo ( "index_name" )
## signmessagewithprivkey "privkey" "message"
## validateaddress "address"
## verifymessage "address" "signature" "message"

== Wallet ==
## abandontransaction "txid"
## abortrescan
## addmultisigaddress nrequired ["key",...] ( "label" "address_type" )
## backupwallet "destination"
## bumpfee "txid" ( options )
## createwallet "wallet_name" ( disable_private_keys blank "passphrase" avoid_reuse descriptors load_on_startup external_signer )
## dumpprivkey "address"
## dumpwallet "filename"
## encryptwallet "passphrase"
## getaddressesbylabel "label"
## getaddressinfo "address"
## getbalance ( "dummy" minconf include_watchonly avoid_reuse )
## getbalances
## getnewaddress ( "label" "address_type" )
## getrawchangeaddress ( "address_type" )
## getreceivedbyaddress "address" ( minconf include_immature_coinbase )
## getreceivedbylabel "label" ( minconf include_immature_coinbase )
## gettransaction "txid" ( include_watchonly verbose )
gettransaction方法仅支持获得与本地钱包相关的交易，如果不是与本地钱包相关的交易，则需要先 getrawtransaction ，再decoderawtransaction，才可以得到对rawtransaction解码后的json格式交易数据。
## getunconfirmedbalance
## getwalletinfo
## importaddress "address" ( "label" rescan p2sh )
## importdescriptors "requests"
## importmulti "requests" ( "options" )
## importprivkey "privkey" ( "label" rescan )
## importprunedfunds "rawtransaction" "txoutproof"
## importpubkey "pubkey" ( "label" rescan )
## importwallet "filename"
## keypoolrefill ( newsize )
## listaddressgroupings
## listdescriptors ( private )
## listlabels ( "purpose" )
## listlockunspent
## listreceivedbyaddress ( minconf include_empty include_watchonly "address_filter" include_immature_coinbase )
## listreceivedbylabel ( minconf include_empty include_watchonly include_immature_coinbase )
## listsinceblock ( "blockhash" target_confirmations include_watchonly include_removed include_change "label" )
## listtransactions ( "label" count skip include_watchonly )
## listunspent ( minconf maxconf ["address",...] include_unsafe query_options )
## listwalletdir
## listwallets
## loadwallet "filename" ( load_on_startup )
## lockunspent unlock ( [{"txid":"hex","vout":n},...] persistent )
## migratewallet ( "wallet_name" "passphrase" )
## newkeypool
## psbtbumpfee "txid" ( options )
## removeprunedfunds "txid"
## rescanblockchain ( start_height stop_height )
## restorewallet "wallet_name" "backup_file" ( load_on_startup )
## send [{"address":amount,...},{"data":"hex"},...] ( conf_target "estimate_mode" fee_rate options )
## sendall ["address",{"address":amount,...},...] ( conf_target "estimate_mode" fee_rate options )
## sendmany ( "" ) {"address":amount,...} ( minconf "comment" ["address",...] replaceable conf_target "estimate_mode" fee_rate verbose )
## sendtoaddress "address" amount ( "comment" "comment_to" subtractfeefromamount replaceable conf_target "estimate_mode" avoid_reuse fee_rate verbose )
## sethdseed ( newkeypool "seed" )
## setlabel "address" "label"
## settxfee amount
## setwalletflag "flag" ( value )
## signmessage "address" "message"
## signrawtransactionwithwallet "hexstring" ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )
## simulaterawtransaction ( ["rawtx",...] {"include_watchonly":bool,...} )
## unloadwallet ( "wallet_name" load_on_startup )
## upgradewallet ( version )
## walletcreatefundedpsbt ( [{"txid":"hex","vout":n,"sequence":n,"weight":n},...] ) [{"address":amount,...},{"data":"hex"},...] ( locktime options bip32derivs )
## walletdisplayaddress "address"
## walletlock
## walletpassphrase "passphrase" timeout
## walletpassphrasechange "oldpassphrase" "newpassphrase"
## walletprocesspsbt "psbt" ( sign "sighashtype" bip32derivs finalize )

== Zmq ==
## getzmqnotifications
