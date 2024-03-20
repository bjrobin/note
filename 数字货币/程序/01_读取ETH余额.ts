const { ethers, JsonRpcProvider } = require('ethers')
require('dotenv').config()
  
const INFURA_URL_TESTNET = process.env.INFURA_URL_TESTNET
console.log(INFURA_URL_TESTNET)
const WALLET_ADDRESS = process.env.WALLET_ADDRESS
console.log(WALLET_ADDRESS)
const WALLET_SECRET = process.env.WALLET_SECRET
console.log(WALLET_SECRET)

const provider = new JsonRpcProvider(INFURA_URL_TESTNET) // Ropsten
// const provider = new ethers.providers.JsonRpcProvider(INFURA_URL_TESTNET) // Ropsten

const wallet = new ethers.Wallet(WALLET_SECRET)
const connectedWallet = wallet.connect(provider)
console.log("connectedWallet",connectedWallet)
for (var _name in wallet) {
    console.log(_name,wallet[_name])
}
// const bal = provider.getBalance("0xdAC17F958D2ee523a2206206994597C13D831ec7") //1n
// const bal = provider.getBalance("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2") // WETH 3022915577361730462409682n

// 37999032136990566 WETH怎么取到这个值？
// 44617681908164723 ETH
// 499670071465371659n 这个不知道代表啥，换另外的provider，这个值不一样
const bal = provider.getBalance(WALLET_ADDRESS) // 44617681908164723 ETH 这个可以取到
console.log("Number.MAX_SAFE_INTEGER:",Number.MAX_SAFE_INTEGER);
// 1ETH = 1000000000000000000
bal.then((balance: any) => {
    console.log(balance);
    console.log(balance.toString()); // 0
    console.log("ethers.formatEther(balance.toString()):",ethers.formatEther(balance.toString()));
});
