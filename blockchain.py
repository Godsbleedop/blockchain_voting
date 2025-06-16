import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, votes, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.votes = votes
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'votes': self.votes,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_votes = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time(), [], "0")
        self.chain.append(genesis_block)

    def add_vote(self, voter_id, candidate):
        vote = {'voter_id': voter_id, 'candidate': candidate}
        self.pending_votes.append(vote)
        if len(self.pending_votes) >= 5:
            self.create_block()

    def create_block(self):
        previous_block = self.chain[-1]
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            votes=self.pending_votes.copy(),
            previous_hash=previous_block.hash
        )
        self.pending_votes = []
        self.chain.append(block)
        print(f"\n✅ New Block Created! Index: {block.index}, Hash: {block.hash[:10]}...")

    def print_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index} - Hash: {block.hash[:10]}...")
            print(f"Timestamp: {block.timestamp}")
            print(f"Previous Hash: {block.previous_hash[:10]}...")
            print(f"Votes: {block.votes}")
