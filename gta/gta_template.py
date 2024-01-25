from enum import Enum


class WeaponType(Enum):
    PISTOL = {"weapon_price": 1_000, "ammo_damage": 5, "ammo_price": 400, "magazine_size": 15}
    SMG = {"weapon_price": 2_000, "ammo_damage": 5, "ammo_price": 1_000, "magazine_size": 30}
    CARBINE_RIFLE = {"weapon_price": 5_000, "ammo_damage": 10, "ammo_price": 2_500, "magazine_size": 30}
    COMBAT_MG = {"weapon_price": 30_000, "ammo_damage": 15, "ammo_price": 20_000, "magazine_size": 100}
    SNIPER = {"weapon_price": 60_000, "ammo_damage": 35, "ammo_price": 50_000, "magazine_size": 5}
    RPG = {"weapon_price": 100_000, "ammo_damage": 80, "ammo_price": 80_000, "magazine_size": 1}
    MINIGUN = {"weapon_price": 50_000, "ammo_damage": 1, "ammo_price": 200_000, "magazine_size": 3_000}


class JobType(Enum):
    RACE = "race"
    DELIVERY = "delivery"
    BANK_HEIST = "bank heist"


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class DeadPlayerException(Exception):
    pass


class Weapon:
    """The weapon class."""

    def __init__(self, weapon_type: WeaponType):
        """
        Initialise the weapon class.

        :param weapon_type: The type of the new Weapon object.

        :raise TypeError: if the given argument isn't of type WeaponType.
        """
        self.type = weapon_type
        self.price = weapon_type.value["weapon_price"]
        self.damage = weapon_type.value["ammo_damage"]
        self.ammo_price = weapon_type.value["ammo_price"]
        self.magazine_size = weapon_type.value["magazine_size"]
        self.ammo_in_magazine = 0
        self.ammo_in_inventory = 0

    def reload(self):
        """
        Reload the weapon if the character has ammo in their inventory.

        If the magazine is not full, as much ammo as possible will be transferred from inventory to magazine.
        """
        pass

    def __repr__(self):
        """
        Return the name of the weapon in lowercase.

        :return the name of the weapon in lowercase.
        """
        return str(self.type.name).lower()


class GTACharacter:
    """A class to represent a character in a Grand Theft Auto-style game."""

    def __init__(self, name: str, gender: Gender, initial_health: int, armor: int, weapons: list[Weapon], money: int):
        """
        Initializes a new GTACharacter instance with the given attributes.

        :param name: The name of the character.
        :param gender: The gender of the character.
        :param initial_health: The health of the character, between 0 and 100.
        :param armor: The armor of the character, between 0 and 100.
        :param weapons: A list of the character's weapons.
        :param money: The amount of money the character has.
        """
        self.dead = False
        self.name = name
        self.gender = gender
        self.health = initial_health
        self.__armor = armor
        self.__money = money
        self.weapons = weapons

    @property
    def health(self):
        """Gets the current health of the character."""
        pass

    @health.setter
    def health(self, new_value: int):
        """
        Sets the current health of the character.

        :param new_value: The new health value for the character.

        :raise DeadPlayerException: If the player is dead.
        """
        pass

    @property
    def armor(self):
        """
        Gets the current armor of the character.

        :return: current armor of the character.
        """
        pass

    @armor.setter
    def armor(self, new_value: int):
        """
        Sets the current armor of the character.

        :param new_value: The new armor value for the character.

        :raise DeadPlayerException: If the player is dead.
        """
        pass

    @property
    def money(self):
        """
        Gets the amount of money the character has. The amount of money should be guaranteed to be between
        0 and 2,147,483,647.

        :return: The amount of money the character has.
        """
        pass

    @money.setter
    def money(self, new_value: int):
        """
        Sets the amount of money the character has. Like in the game Grand Theft Auto V, if the player's money is set
        to be out of bounds, it should return to its previous state. The bounds being 0 and 2,147,483,647
        (maximum value for a 32-bit signed integer).

        :param new_value: The new amount of money for the character.
        """
        pass

    def get_weapon(self, weapon_type: WeaponType) -> Weapon | None:
        """
        Return the weapon object of the given weapon type if it's in the character's weapons list.
        Otherwise, returns None.

        :param weapon_type: The type of weapon to search for.

        :return: The found weapon or None.
        """
        pass

    def buy_weapon(self, weapon_type: WeaponType) -> Weapon | None:
        """
        Buy a new weapon of the given type and adds it to the character's weapons list.
        The character must have enough money to buy the weapon.

        :param weapon_type: The type of weapon to buy.

        :return: The bought weapon.
        """
        pass

    def buy_ammo(self, weapon: Weapon) -> bool:
        """
        Buy one clip of ammo for the specified weapon type and add it to the weapon's inventory.
        The character must have enough money to buy the ammo, and they must own the weapon.

        :param weapon: A weapon to buy ammo for.

        :return: Whether the transaction was successful or not.
        """
        pass

    def buy_armor(self):
        """Refill the character's armor if the character has enough money ($1,000)."""
        pass

    def buy_health(self):
        """Refill the character's health if the character has enough money ($2,000)."""
        pass

    def earn_money(self, job_type: JobType) -> int:
        """
        Earns money by completing a job.

        For racing, the character needs to have at least $10,000 of money. At each participated race,
        the character bids all of their money and wins every 2nd race. Meaning 1st, 3rd, 5th etc. races will be lost.
        For delivery, the character needs to have at least $20,000, one weapon and (at least 80 health
        or at least 50 health and 50 armor). Each delivery costs $20,000, but after every 3rd delivery, the character
        is paid $100,000.
        For bank heist, the character needs to have at least two weapons and at least 80 health and 80 armor.
        With most bank heists, the character will earn 25% of their current money and lose 35 health and 60 armor.
        If the earned amount is float, then round it to the closest integer. With every 4th bank heist
        on the other hand, the character will earn 75% of their money, but lose 95 health and 95 armor.

        :param job_type: A type of job to be completed.
        :return: Amount of money earned. If the character lost money, then the returned amount is negative.
        """
        pass

    def __repr__(self):
        """Character's name."""
        return self.name


def shoot(shooter: GTACharacter, target: GTACharacter, weapon: Weapon, times: int = None) -> bool:
    """
    Make the character shoot a target.

    :param shooter: The shooter.
    :param target: The target.
    :param weapon: The type of weapon used to shoot the target.
    :param times: Times to shoot the target. Default value None meaning the shooter will empty
        the weapon's magazine at the target.

    :return: Whether the shooting happened or not.

    """
    pass


if __name__ == '__main__':
    franklin = GTACharacter("Franklin", Gender.MALE, 100, 100, [Weapon(WeaponType.PISTOL), Weapon(WeaponType.SMG)],
                            1242142)
    michael = GTACharacter("Michael", Gender.MALE, 100, 100,
                           [Weapon(WeaponType.CARBINE_RIFLE), Weapon(WeaponType.PISTOL)], 91242142)
    trevor = GTACharacter("Trevor", Gender.MALE, 100, 100,
                          [Weapon(WeaponType.COMBAT_MG), Weapon(WeaponType.RPG), Weapon(WeaponType.MINIGUN),
                           Weapon(WeaponType.SNIPER)], 1210042)
    noob = GTACharacter("noob", Gender.MALE, 100, 100, [], 0)

    f_smg = franklin.get_weapon(WeaponType.SMG)
    print(shoot(franklin, michael, f_smg))
    print(shoot(franklin, michael, f_smg))
    print(shoot(franklin, michael, f_smg))
    print()

    print(franklin, franklin.health, franklin.armor)
    print(michael, michael.health, michael.armor)
    print(trevor, trevor.health, trevor.armor)
    print()

    t_rpg = trevor.get_weapon(WeaponType.RPG)
    print(trevor.buy_ammo(t_rpg))
    trevor.buy_ammo(t_rpg)
    print(t_rpg.reload())
    print(shoot(trevor, franklin, t_rpg))
    print(t_rpg.reload())
    try:
        print(shoot(trevor, franklin, t_rpg))
        print("Should raise DeadPlayerException")
    except DeadPlayerException:
        pass
    print()

    print(franklin, franklin.health, franklin.armor)
    print(michael, michael.health, michael.armor)
    print(trevor, trevor.health, trevor.armor)
    print()

    try:
        franklin.health = 100
        print("Should raise DeadPlayerException")
    except DeadPlayerException:
        pass

    try:
        print(shoot(franklin, trevor, t_rpg))
        print("Should raise DeadPlayerException")
    except DeadPlayerException:
        pass

    print(noob.buy_weapon(WeaponType.PISTOL))
