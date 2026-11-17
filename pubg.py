
class PUBG:
    def __init__(self, player_name, player_id, level=1):
        # Player information
        self.player_name = player_name
        self.player_id = player_id
        self.level = level

        # Player statistics
        self.health = 100
        self.armor = 100
        self.kills = 0
        self.deaths = 0
        self.damage = 0
        self.rank = "Bronze"

        # Game information
        self.weapon = None
        self.ammo = 0
        self.inventory = []
        self.is_alive = True

    # Create player
    def create_player(self):
        print(f"Player {self.player_name} created successfully!")

    # Display player information
    def player_info(self):
        print("\n----- PLAYER INFORMATION -----")
        print(f"Name       : {self.player_name}")
        print(f"Player ID  : {self.player_id}")
        print(f"Level      : {self.level}")
        print(f"Health     : {self.health}")
        print(f"Armor      : {self.armor}")
        print(f"Kills      : {self.kills}")
        print(f"Deaths     : {self.deaths}")
        print(f"Damage     : {self.damage}")
        print(f"Rank       : {self.rank}")
        print(f"Weapon     : {self.weapon}")
        print(f"Ammo       : {self.ammo}")
        print(f"Alive      : {self.is_alive}")

    # Increase player level
    def level_up(self):
        self.level += 1
        print(f"Congratulations! Level increased to {self.level}")

    # Equip weapon
    def equip_weapon(self, weapon_name, ammo):
        self.weapon = weapon_name
        self.ammo = ammo
        print(f"{weapon_name} equipped with {ammo} ammo.")

    # Reload weapon
    def reload(self, ammo):
        self.ammo += ammo
        print(f"Reloaded! Total ammo: {self.ammo}")

    # Fire weapon
    def shoot(self):
        if not self.is_alive:
            print("Player is dead!")
        elif self.weapon is None:
            print("No weapon equipped!")
        elif self.ammo > 0:
            self.ammo -= 1
            print(f"{self.player_name} fired {self.weapon}!")
        else:
            print("Out of ammo! Reload your weapon.")

    # Add item to inventory
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

    # Remove item from inventory
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")

    # Display inventory
    def show_inventory(self):
        print("\n----- INVENTORY -----")
        for item in self.inventory:
            print(f"- {item}")

        if not self.inventory:
            print("Inventory is empty.")

    # Take damage
    def take_damage(self, amount):
        if not self.is_alive:
            return

        remaining = amount

        absorbed = min(self.armor, remaining)
        self.armor -= absorbed
        remaining -= absorbed

        self.health = max(0, self.health - remaining)
        self.damage += amount

        print(f"Player took {amount} damage.")
        print(f"Remaining Health: {self.health}")

        if self.health == 0:
            self.is_alive = False
            self.deaths += 1
            print("Player eliminated!")

    # Heal player
    def heal(self, amount):
        if self.is_alive:
            self.health = min(100, self.health + amount)
            print(f"Health restored to {self.health}.")

    # Record kill
    def add_kill(self):
        if self.is_alive:
            self.kills += 1
            print(f"Total kills: {self.kills}")

    # Calculate K/D ratio
    def kd_ratio(self):
        if self.deaths == 0:
            return float(self.kills)
        return round(self.kills / self.deaths, 2)

    # Update rank
    def update_rank(self):
        if self.kills >= 50:
            self.rank = "Conqueror"
        elif self.kills >= 30:
            self.rank = "Ace"
        elif self.kills >= 20:
            self.rank = "Diamond"
        elif self.kills >= 10:
            self.rank = "Platinum"
        else:
            self.rank = "Bronze"

        print(f"Current Rank: {self.rank}")

    # Display statistics
    def player_stats(self):
        print("\n----- PLAYER STATS -----")
        print(f"Kills      : {self.kills}")
        print(f"Deaths     : {self.deaths}")
        print(f"K/D Ratio  : {self.kd_ratio()}")
        print(f"Damage     : {self.damage}")
        print(f"Rank       : {self.rank}")

print(__name__=='__main__')
print(__name__)
# Main program
if __name__ == '__main__':

    # Create player object
    player1 = PUBG("Shadow", 101, 10)

    # Create player
    player1.create_player()

    # Equip weapon
    player1.equip_weapon("M416", 30)

    # Add inventory items
    player1.add_item("Medkit")
    player1.add_item("Helmet")
    player1.add_item("Energy Drink")

    # Perform player actions
    player1.shoot()
    player1.shoot()
    player1.take_damage(20)
    player1.heal(10)
    player1.add_kill()
    player1.add_kill()

    # Display information
    player1.show_inventory()
    player1.player_info()

    # Update and display rank
    player1.update_rank()
    player1.player_stats()

    # Level up
    player1.level_up()
