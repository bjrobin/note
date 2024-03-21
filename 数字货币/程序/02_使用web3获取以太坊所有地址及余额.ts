// https://www.jianshu.com/p/e2ca19f276fb
const {Web3} = require("web3")
const rpcURL = "http://localhost:8545"
const web3 = new Web3(rpcURL);
// web3.eth.getAccounts().then(console.log); // [ '0xcA8C3fb5D8B94b36E1dA447C932BcD6B1B6480d8' ]
// web3.eth.getBalance("0xc11442C38740D5dDFdD3d6148c2c4232BAa6d8b0").then(console.log);
// web3.eth.getBalance("0xcA8C3fb5D8B94b36E1dA447C932BcD6B1B6480d8").then(console.log);
// 获取特定地址关联的代码。
// web3.eth.getCode("0x959E169A89dB63F97f9FB45143c18cD46cd8A101").then(console.log);
// 0x608060405234801561001057600080fd5b506004361061002b5760003560e01c806345773e4e14610030575b600080fd5b61003861004e565b6040516100459190610124565b60405180910390f35b60606040518060400160405280600b81526020017f48656c6c6f20576f726c64000000000000000000000000000000000000000000815250905090565b600081519050919050565b600082825260208201905092915050565b60005b838110156100c55780820151818401526020810190506100aa565b838111156100d4576000848401525b50505050565b6000601f19601f8301169050919050565b60006100f68261008b565b6101008185610096565b93506101108185602086016100a7565b610119816100da565b840191505092915050565b6000602082019050818103600083015261013e81846100eb565b90509291505056fea26469706673582212206896ccc2a417b3114f92d234d5d88d13626b3b38e22493ca9ee9c190043a49fa64736f6c634300080d0033

// 获取区块链的信息
web3.eth.getBlockNumber().then(console.log);
// web3.eth.getBlockNumber(function (error, result) {
//     console.log(result)
// })
// You can also use await/async function calls to avoid nesting callbacks in your code:
async function getBlockNumber2() {
    const latestBlockNumber = await web3.eth.getBlockNumber()
    console.log(latestBlockNumber)
    return latestBlockNumber
}
// web3.eth.getBlock(0).then(console.log);
// console.log("-----------------------------------")
// web3.eth.getBlock("latest").then(console.log);
// web3.eth.getBlock(41980).then(console.log);

//获取当前区块高度
function getBlockNumber () {
    web3.eth.getBlockNumber().then(
    function(result:number){
        // console.log("blockNumber:"+result);
        throughBlock(result);
    })
}
//从创世区块0开始遍历
function throughBlock (blockNumber:number) {
    if (!blockNumber) {console.log('blockNumber is 0');return false;};
    for (var i = 0; i < blockNumber; i++) {
        // console.log("i:"+i);
        getBlock(i);
    };
}
//获取当前区块的信息
function getBlock (blockNumber:number) {
    web3.eth.getBlock(blockNumber).then(
        function(result:any){
            const transactions = result.transactions;
            if (transactions){
                for (var i = 0; i < transactions.length; i++) {
                    console.log("---",blockNumber+" transactions i:"+i);
                    getTransactions(transactions[i]);
                }
            }
        });
}
//获取交易信息
function getTransactions (txh: any) {
    web3.eth.getTransaction(txh).then(
        function(result: any){
            var from = result.from;
            var to = result.to;
            console.log("from:"+from,"to:"+to);
            getCode(from);
            getCode(to);
    });
}
// 验证地址是否是合约地址
function getCode (address: any) {
    if (!address) {return false;};
    web3.eth.getCode(address).then(
        function(result: string){
            console.log("address:"+address,"code:"+result);
            if (result == '0x') {
                getBalance(address);                
            };          
    });
}
// 获取地址余额
function getBalance (address: any) {
    web3.eth.getBalance(address).then(
        function(result: string){
            if (!addressList.includes(address)) {
                addressList.push(address);
                console.log(address+"\t"+result); //地址 余额
            };          
        });
}
var addressList=[] as any[];
getBlockNumber();
web3.eth.getBlock("latest").then(console.log);