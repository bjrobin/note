const TronWeb = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.trongrid.io',
  solidityNode: 'https://api.trongrid.io',
  eventServer: 'https://api.trongrid.io',
});

const txHash = '661f1df88ce02b746efe7449c3c7a04d6d21a7fc019723c92679228d8275ad57';

tronWeb.trx.getTransaction(txHash).then((transaction) => {
  console.log('transaction:', transaction);
}).catch((error) => {
  console.error('Error:', error);
});

// error TS7006: Parameter 'error' implicitly has an 'any' type.
// tsc --init   
// "noImplicitAny": false,                            /* Enable error reporting for expressions and declarations with an implied 'any' type. */
// Error: Cannot find module '@noble/secp256k1'
// npm install @noble/secp256k1@1.7.1