import hashlib
import json
from time import time

class SupplyChainBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_events = []
        # Create the Genesis block
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'events': self.pending_events,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash(block)
        self.pending_events = []  # clear pending events
        self.chain.append(block)
        return block

    def add_event(self, product_id, actor, location, status, details):
        event = {
            'product_id': product_id,
            'actor': actor,
            'location': location,
            'status': status,
            'details': details,
            'timestamp': time()
        }
        self.pending_events.append(event)
        return event

    def hash(self, block):
        block_copy = block.copy()
        block_copy['hash'] = ''
        encoded = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def get_chain(self):
        return self.chain


# ---------------- USER INTERACTION ----------------
blockchain = SupplyChainBlockchain()

while True:
    print("\n===== BLOCKCHAIN SUPPLY CHAIN SYSTEM =====")
    print("1. Add Supply Chain Event")
    print("2. Create (Mine) New Block")
    print("3. View Entire Blockchain")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        product_id = input("Enter Product ID: ")
        actor = input("Enter Actor Name (Manufacturer/Distributor/etc.): ")
        location = input("Enter Location: ")
        status = input("Enter Status (Manufactured/Shipped/Received/etc.): ")
        details = input("Enter Additional Details: ")
        blockchain.add_event(product_id, actor, location, status, details)
        print("✅ Event added successfully!")

    elif choice == '2':
        prev_hash = blockchain.chain[-1]['hash']
        blockchain.create_block(prev_hash)
        print("⛏️  New block created successfully!")

    elif choice == '3':
        print("\n📦 Current Blockchain Data:")
        for block in blockchain.get_chain():
            print(json.dumps(block, indent=4))
        print("\nTotal Blocks:", len(blockchain.chain))

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice, please try again.")
