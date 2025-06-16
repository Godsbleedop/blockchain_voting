from blockchain import Blockchain

def main():
    chain = Blockchain()

    print("=== Blockchain Voting System ===")
    print("Each block stores 5 votes.\n")

    while True:
        voter_id = input("Enter Voter ID (or 'exit' to quit): ").strip()
        if voter_id.lower() == 'exit':
            break

        candidate = input("Enter Candidate Name: ").strip()

        if not voter_id or not candidate:
            print(" Voter ID and Candidate name required.\n")
            continue

        chain.add_vote(voter_id, candidate)

    print("\n🧾 Final Blockchain:")
    chain.print_chain()

if __name__ == "__main__":
    main()
