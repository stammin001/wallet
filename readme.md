# Wallet for Bitcoin and Ethereum

### Description
This wallet helps with transfer of bitcoin or ethereum from one address to another. This is built with HD Wallet tool which would result to deterministic accounts based on the mnemonic provided. 

### How to use

1. Please refer to requirements.txt file for installing some of the dependencies

2. Please refer to wallet.ipynb file for executable code used for this

3. Call derive_wallets() function with appropriate parameters as below to generate the public/private keys based on mnemonic:
   
   ![Derive_Wallet](screenshots/Derive_Wallets.PNG)
   
   Below is the snapshot of keys generated for different coins like BTC-Test, ETH and LTC
   
   ![BTC_Keys](screenshots/BTC_Keys.PNG)
   ![ETH_Keys](screenshots/ETH_Keys.PNG)
   ![LTC_Keys](screenshots/LTC_Keys.PNG)
   
4. In order to send test bitcoin, will have to call send_tx function with appropriate parameter values. Below is the snapshot of an example:

  ![BTC Transaction Input](screenshots/BTCTest_Transaction_Request.PNG)

   Below is the snapshot of the resulting transaction out of this

  ![BTC Transaction Output](screenshots/BTCTest_Transaction_2.PNG)

5. In order to send ethereum, will have to call send_tx function with appropriate parameter values. Below is the snapshot of an example:

  ![ETH Transaction Input](screenshots/ETHTest_Transaction_Request.PNG)

   Below is the snapshot of the resulting transaction out of this

  ![ETH Transaction Output](screenshots/ETH_Transaction_2.PNG)

