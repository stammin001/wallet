# Wallet for Bitcoin and Ethereum

### Descirption
This wallet helps with transfer of bitcoin or ethereum from one address to another. This is built with HD Wallet tool which would result to deterministic accounts based on the mnemonic provided. 

### How to use

1. Call derive_wallets() function with appropriate parameters as below to generate the public/private keys based on mnemonic:
   
   ![Wallet_Keys]()
   
2. In order to send bitcoin, will have to call send_tx function with appropriate parameter values. Below is the snapshot of an example:

  ![BTC Transaction Input]()

   Below is the snapshot of the resulting transaction out of this

  ![BTC Transaction Output](screenshots/BTCTest_Transaction_2.PNG)

3. In order to send ethereum, will have to call send_tx function with appropriate parameter values. Below is the snapshot of an example:

  ![ETH Transaction Input]()

   Below is the snapshot of the resulting transaction out of this

  ![ETH Transaction Output](screenshots/ETH_Transaction_2.PNG)

