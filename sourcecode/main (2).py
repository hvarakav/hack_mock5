from cryptography.fernet import Fernet

class ElectronicVotingSystem:
    def __init__(self):
        # Generate encryption key
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.votes = []

    def cast_vote(self, vote):
        # Encrypt the vote and store it
        encrypted_vote = self.cipher.encrypt(vote.encode())
        self.votes.append(encrypted_vote)

    def tally_votes(self):
        # Decrypt and count the votes
        vote_count = {}
        for encrypted_vote in self.votes:
            decrypted_vote = self.cipher.decrypt(encrypted_vote).decode()
            if decrypted_vote in vote_count:
                vote_count[decrypted_vote] += 1
            else:
                vote_count[decrypted_vote] = 1
        return vote_count

def main():
    voting_system = ElectronicVotingSystem()

    while True:
        print("1. Cast a vote")
        print("2. Tally votes")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vote = input("Enter your vote: ")
            voting_system.cast_vote(vote)
            print("Your vote has been recorded.")
        elif choice == '2':
            result = voting_system.tally_votes()
            print("Vote tally:", result)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

