// https://blog.csdn.net/weixin_41303815/article/details/124799850
const {Web3} = require("web3")
var moment = require('moment');
var web3: any = null
// web3 = new Web3.providers.HttpProvider(INFURA_URL_TESTNET);
// npm install --save dotenv 
// 在Finder里面直接按 ⌘⇧. （Cmd+Shift+.）即可切换隐藏文件显示与隐藏。
require('dotenv').config({path: '/data/.env'})
  
const INFURA_URL_TESTNET = process.env.INFURA_URL_TESTNET
console.log(INFURA_URL_TESTNET)
// const WALLET_ADDRESS = process.env.WALLET_ADDRESS
// console.log(WALLET_ADDRESS)
// const WALLET_SECRET = process.env.WALLET_SECRET
// console.log(WALLET_SECRET)
const startBlock = 19496171;
const endBlock = 19496171;
var _contract_num = 0;
var _contract_0x = 0;
async function connectWeb3() {
    // const web3 = new Web3.providers.HttpProvider(INFURA_URL_TESTNET)
    web3 = new Web3(INFURA_URL_TESTNET);
    console.log('web3.' + web3);
    web3.eth.getBlockNumber().then(console.log);
    // global.web3 = web3;
    console.log('web3 has connected successfully.');
}
// Part Functions
async function checkIfIsContract(j: number,newAddress: string) {
    // console.log('newAddress.' + newAddress);
    if(newAddress == null){
        console.log('=========='+j+'=================================================================');
        console.log('不是合约 null');
       
        return false;
    }
    var code = await web3.eth.getCode(newAddress);
    // console.log(" ** CODE ** " + code);
    if(code == '0x') {
        // console.log('=========='+j+'=================================================================');
        console.log('不是合约 NOT CONTRACT');
        _contract_0x++;
        return false;
    } else {
        console.log('是合约 CONTRACT');
        _contract_num++;
        return true
    };
}
async function uniqueAddAddress(j: number ,newAddress:string,transactionInput: string) {
    
    // console.log('newAddress.' + newAddress+' transactionInput.' + transactionInput);
    let result = await checkIfIsContract(j,newAddress);
    // console.log('result.' + result);

}
async function scanTheChain() {
    for(let i = startBlock; i <= endBlock; i++) {
        console.log('scanning the chain.');
        console.log("[ " + moment().format('MMMM Do YYYY, h:mm:ss a') + " ] " + "Scanning Block " + i);
        var blockInfo = await web3.eth.getBlock(i);
        console.log('blockinfo.' + blockInfo);
		if(!Boolean(blockInfo)){continue}
        var blockTxes = blockInfo.transactions;
        // console.log('blockTxes.' + blockTxes);
        var blockTxCnt = await web3.eth.getBlockTransactionCount(i);
        console.log("CNT => " + blockTxCnt)
        console.log('===========================================================================');
        for(let j = 0; j < blockTxCnt; j++) {
            // console.log('===========================================================================');
            var thisTx = await web3.eth.getTransaction(blockTxes[j]);
            const txFrom = thisTx.from;
            await uniqueAddAddress(j,txFrom,thisTx.input);
            const txTo = thisTx.to;
            await uniqueAddAddress(j,txTo,thisTx.input);
        }
        console.log("Contract Number: " + _contract_num);
        console.log("Not Contract Number: " + _contract_0x);
    }
}
(async function main(){
    console.log(moment().format('LLL'));
    
    moment.locale('zh-cn');
    console.log(moment().format('LLL'));

    console.log("Hello World");
    // await connectDB();
    await connectWeb3();
    await scanTheChain();
})();