// CALLING A SMART CONTRACT FROM JAVASCRIPT
// https://ethereum.org/en/developers/tutorials/calling-a-smart-contract-from-javascript/
const ERC20TransferABI = [
    {
      constant: false,
      inputs: [
        {
          name: "_to",
          type: "address",
        },
        {
          name: "_value",
          type: "uint256",
        },
      ],
      name: "transfer",
      outputs: [
        {
          name: "",
          type: "bool",
        },
      ],
      payable: false,
      stateMutability: "nonpayable",
      type: "function",
    },
    {
      constant: true,
      inputs: [
        {
          name: "_owner",
          type: "address",
        },
      ],
      name: "balanceOf",
      outputs: [
        {
          name: "balance",
          type: "uint256",
        },
      ],
      payable: false,
      stateMutability: "view",
      type: "function",
    },
  ]
const DAI_ADDRESS = "0x6b175474e89094c44da98b954eedeac495271d0f"
const web3 = new Web3("http://localhost:8545")
const daiToken = new web3.eth.Contract(ERC20TransferABI, DAI_ADDRESS)