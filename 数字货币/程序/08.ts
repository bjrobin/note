const { ethers } = require('ethers')
// import { ethers } from 'ethers'
// const { abi: IUniswapV3PoolABI } = require('@uniswap/v3-core/artifacts/contracts/interfaces/IUniswapV3Pool.sol/IUniswapV3Pool.json')
import { abi as IUniswapV3PoolABI } from '@uniswap/v3-core/artifacts/contracts/interfaces/IUniswapV3Pool.sol/IUniswapV3Pool.json'
const { abi: SwapRouterABI } = require('@uniswap/v3-periphery/artifacts/contracts/interfaces/ISwapRouter.sol/ISwapRouter.json')
const { getPoolImmutables, getPoolState } = require('./helpers')
const ERC20ABI = require('./abi.json')
require('dotenv').config()

const INFURA_URL_TESTNET = process.env.INFURA_URL_TESTNET
console.log(INFURA_URL_TESTNET)
const WALLET_ADDRESS = process.env.WALLET_ADDRESS
const WALLET_SECRET = process.env.WALLET_SECRET

//https://ropsten.infura.io/
//Ropsten Network decommissioned, please use Goerli or Sepolia instead
//https://blog.infura.io/post/deprecation-timeline-for-rinkeby-ropsten-and-kovan-testnets
const provider = new ethers.providers.JsonRpcProvider(INFURA_URL_TESTNET) // Ropsten

// const poolAddress = "0x4D7C363DED4B3b4e1F954494d2Bc3955e49699cC" // UNI/WETH 这个找不到了
// const poolAddress = "0x1d42064Fc4Beb5F8aAF85F4617AE8b3b5B8Bd801" // UNI/WETH 换成这个
const poolAddress = '0x4e68Ccd3E89f51C3074ca5072bbAC773960dFa36' // ETH/USDT
// const poolAddress = '0x11b815efB8f581194ae79006d24E0d814B7697F6' // ETH/USDT
// https://docs.uniswap.org/contracts/v3/reference/deployments
const swapRouterAddress = '0xE592427A0AEce92De3Edee1F18E0157C05861564' // SwapRouter

const name0 = 'Wrapped Ether'
const symbol0 = 'WETH'
const decimals0 = 18
// const address0 = '0xc778417e063141139fce010982780140aa0cd5ab'
const address0 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'//WETH

// const name1 = 'Uniswap Token'
// const symbol1 = 'UNI'
// const decimals1 = 18
// const address1 = '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984'

//const TokenB = new Token(3, immutables.token0, 6, 'USDT', 'Tether USD')//0xdAC17F958D2ee523a2206206994597C13D831ec7
const name1 = 'Tether USD'
const symbol1 = 'USDT'
const decimals1 = 6
const address1 = '0xdAC17F958D2ee523a2206206994597C13D831ec7' // USDT

function log(s,obj){
  console.log("--------------------------")
  console.log("# "+s)
  console.log("```js")
  console.log(obj)
  console.log("```")

}

async function main() {
  //const poolAddress1 = '0x4e68Ccd3E89f51C3074ca5072bbAC773960dFa36' // ETH/USDT
  const gasPrice = await provider.getGasPrice()
  log("gasPrice",gasPrice)//BigNumber { _hex: '0x02c3483284', _isBigNumber: true }
  log("gasPrice",gasPrice.toNumber())//11866223236
  log("gasPrice",Number(gasPrice))//11866223236
  
  //value + gasPrice * gasLimit
  //0.01 

  // gasLimit = 200,000, gasPrice * gasLimit = 200000 * 50 * 10^-9 = 0.01.
  // 11 * 1000000  * 10^-9 = 0.011000000
  //                         0.01031115790476832
  // return
  const poolContract = new ethers.Contract(
    poolAddress,
    IUniswapV3PoolABI,
    provider
  )

  //console.log("poolContract",poolContract)

  const immutables = await getPoolImmutables(poolContract)
  log("immutables",immutables)
  
  const state = await getPoolState(poolContract)
  log("state",state)

  

  const wallet = new ethers.Wallet(WALLET_SECRET)
  const connectedWallet = wallet.connect(provider)
  log("connectedWallet",connectedWallet)

  const swapRouterContract = new ethers.Contract(
    swapRouterAddress,
    SwapRouterABI,
    provider
  )

  log("swapRouterContract",swapRouterContract)
  const inputAmount = 0.001
  // .001 => 1 000 000 000 000 000
  //         1 000 000 000 000 000 000 00
  const amountIn = ethers.utils.parseUnits(
    inputAmount.toString(),
    decimals0
  )

  log("amountIn",amountIn)
  const approvalAmount = (amountIn * 100000).toString()
  log("approvalAmount",approvalAmount)
  const tokenContract0 = new ethers.Contract(
    address0,
    ERC20ABI,
    provider
  )

  log("tokenContract0",tokenContract0)
  const approvalResponse = await tokenContract0.connect(connectedWallet).approve(
    swapRouterAddress,
    approvalAmount
  )
  log("approvalResponse",approvalResponse)
  //'exactInputSingle((address,address,uint24,address,uint256,uint256,uint256,uint160))': 
  const params = {
    tokenIn: immutables.token0,
    tokenOut: immutables.token1,
    fee: immutables.fee,
    recipient: WALLET_ADDRESS,
    deadline: Math.floor(Date.now() / 1000) + (60 * 10),
    amountIn: amountIn,
    amountOutMinimum: 0,
    sqrtPriceLimitX96: 0,
  }

  log("params",params)

  const transaction = swapRouterContract.connect(connectedWallet).exactInputSingle(
    params,
    {
      gasLimit: ethers.utils.hexlify(2000000)
    }
  ).then(transaction => {
    log("transaction",transaction)
  })
  
  
}

main()
