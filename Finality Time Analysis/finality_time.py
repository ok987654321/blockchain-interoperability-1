import time
from web3 import Web3

# Initialize a Web3 instance connected to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Replace with your transaction hash and desired number of confirmations
transaction_hash = '0xYourTransactionHash'
desired_confirmations = 12

def get_confirmation_time(transaction_hash, desired_confirmations):
    start_time = time.time()

    while True:
        try:
            receipt = w3.eth.getTransactionReceipt(transaction_hash)
            if receipt and receipt['blockNumber'] is not None:
                current_block = w3.eth.blockNumber
                confirmations = current_block - receipt['blockNumber']
                if confirmations >= desired_confirmations:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    return elapsed_time
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(10)  # Wait for 10 seconds before checking again

if __name__ == "__main__":
    finality_time = get_confirmation_time(transaction_hash, desired_confirmations)
    print(f"Finality Time for {desired_confirmations} Confirmations: {finality_time} seconds")
