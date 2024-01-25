import pytest
from gta import *


def test_weapon_init():
    weapon_type = WeaponType.PISTOL
    weapon = Weapon(weapon_type)
    assert weapon.type == weapon_type
    assert weapon.price == 1000
    assert weapon.damage == 5
    assert weapon.ammo_price == 400
    assert weapon.magazine_size == 15
    assert weapon.ammo_in_magazine == 0
    assert weapon.ammo_in_inventory == 0


def test_weapon_reload():
    weapon_type = WeaponType.PISTOL
    weapon = Weapon(weapon_type)
    weapon.ammo_in_inventory = 10
    weapon.reload()

    assert weapon.ammo_in_magazine == 10
    assert weapon.ammo_in_inventory == 0
    weapon.reload()

    assert weapon.ammo_in_magazine == 10
    assert weapon.ammo_in_inventory == 0
    weapon.ammo_in_inventory = 20
    weapon.ammo_in_magazine = 0
    weapon.reload()

    assert weapon.ammo_in_magazine == 15
    assert weapon.ammo_in_inventory == 5


def test_gta_character_buy_weapon():
    character = GTACharacter("Mike", Gender.MALE, 100, 0, [], 5000)

    pistol = character.buy_weapon(WeaponType.PISTOL)
    assert pistol is not None
    assert pistol.type == WeaponType.PISTOL
    assert pistol in character.weapons
    assert character.money == 4000

    pistol2 = character.buy_weapon(WeaponType.PISTOL)
    assert pistol2 is None
    assert len(character.weapons) == 1
    assert character.money == 4000

    character.money = 0
    smg = character.buy_weapon(WeaponType.SMG)
    assert smg is None
    assert len(character.weapons) == 1
    assert character.money == 0


def test_gta_character_buy_ammo():
    pistol = Weapon(WeaponType.PISTOL)
    pistol2 = Weapon(WeaponType.PISTOL)
    character = GTACharacter("Test", Gender.MALE, 100, 0, [pistol], 5000)
    assert character.buy_ammo(pistol) is True
    assert character.buy_ammo(pistol2) is False
    assert pistol.ammo_in_inventory == 15
    assert character.money == 4600
    assert character.buy_ammo(None) is False
    assert character.buy_ammo(Weapon(WeaponType.RPG)) is False
    character.money = 0
    assert character.buy_ammo(pistol) is False
    assert pistol.ammo_in_inventory == 15
    assert character.money == 0


def test_gta_character_health():
    character = GTACharacter("Test", Gender.MALE, 100, 0, [], 0)
    assert character.health == 100
    character.health = -10
    assert character.health == 0
    assert character.dead is True

    with pytest.raises(DeadPlayerException):
        character.health = 50

    assert character.health == 0

    with pytest.raises(DeadPlayerException):
        character.health = 200

    assert character.health == 0

    character.dead = False
    character.health = 200
    assert character.dead is False
    assert character.health == 100


def test_gta_character_armor():
    character = GTACharacter("Test", Gender.MALE, 100, 0, [], 0)
    assert character.armor == 0
    character.armor = 50
    assert character.armor == 50
    character.armor = -10
    assert character.armor == 0


def test_gta_character_get_weapon():
    pistol = Weapon(WeaponType.PISTOL)
    character = GTACharacter("Test", Gender.MALE, 100, 0, [pistol], 1_000_000)
    assert character.buy_weapon(WeaponType.PISTOL) is None
    owned_pistol = character.get_weapon(WeaponType.PISTOL)
    assert pistol == owned_pistol

    smg = character.buy_weapon(WeaponType.SMG)
    owned_smg = character.get_weapon(WeaponType.SMG)
    assert smg == owned_smg


def test_weapon():
    weapon_pistol = Weapon(WeaponType.PISTOL)
    assert isinstance(weapon_pistol, Weapon)
    assert weapon_pistol.type == WeaponType.PISTOL
    assert weapon_pistol.price == 1000
    assert weapon_pistol.damage == 5
    assert weapon_pistol.ammo_price == 400
    assert weapon_pistol.magazine_size == 15
    assert weapon_pistol.ammo_in_magazine == 0
    assert weapon_pistol.ammo_in_inventory == 0

    weapon_rpg = Weapon(WeaponType.RPG)
    assert isinstance(weapon_rpg, Weapon)
    assert weapon_rpg.type == WeaponType.RPG
    assert weapon_rpg.price == 100000
    assert weapon_rpg.damage == 80
    assert weapon_rpg.ammo_price == 80000
    assert weapon_rpg.magazine_size == 1
    assert weapon_rpg.ammo_in_magazine == 0
    assert weapon_rpg.ammo_in_inventory == 0

    with pytest.raises(TypeError):
        weapon = Weapon(1)

    weapon_pistol.reload()
    assert weapon_pistol.ammo_in_magazine == 0

    weapon_pistol.ammo_in_inventory = 20
    weapon_pistol.reload()
    assert weapon_pistol.ammo_in_magazine == 15
    assert weapon_pistol.ammo_in_inventory == 5

    weapon_pistol.ammo_in_magazine = 0
    weapon_pistol.ammo_in_inventory = 10
    weapon_pistol.reload()
    assert weapon_pistol.ammo_in_magazine == 10
    assert weapon_pistol.ammo_in_inventory == 0


def test_gta_character():
    weapon_pistol = Weapon(WeaponType.PISTOL)
    weapon_smg = Weapon(WeaponType.SMG)

    character = GTACharacter("Bob", Gender.MALE, 80, 50, [weapon_pistol], 5000)
    assert character.name == "Bob"
    assert character.gender == Gender.MALE
    assert character.health == 80
    assert character.armor == 50
    assert character.get_weapon(WeaponType.PISTOL) == weapon_pistol
    assert character.get_weapon(WeaponType.RPG) is None
    assert character.buy_weapon(WeaponType.PISTOL) is None
    assert character.buy_weapon(WeaponType.RPG) is None
    assert character.buy_weapon(WeaponType.MINIGUN) is None
    character.money = 50_000
    assert character.buy_weapon(WeaponType.MINIGUN).type == WeaponType.MINIGUN
    assert len(character.weapons) == 2

    character.money = 5_000
    assert character.buy_ammo(weapon_smg) is False
    assert character.buy_ammo(weapon_pistol) is True
    assert weapon_pistol.ammo_in_inventory == 15
    assert character.money == 4600

    character.health = 120
    assert character.health == 100

    character.health = -10
    assert character.health == 0
    assert character.dead

    with pytest.raises(DeadPlayerException):
        character.health = 20

    assert character.health == 0
    assert character.dead

    with pytest.raises(DeadPlayerException):
        character.health = 120

    assert character.health == 0
    assert character.dead

    character.dead = False
    character.armor = -10
    assert character.armor == 0

    character.armor = 80
    assert character.armor == 80

    assert str(character) == "Bob"


def test_shoot():
    weapon_types: list[WeaponType] = [
        WeaponType.PISTOL, WeaponType.SMG, WeaponType.CARBINE_RIFLE,
        WeaponType.COMBAT_MG, WeaponType.SNIPER, WeaponType.RPG, WeaponType.MINIGUN
    ]
    cj = GTACharacter("Carl Johnson", Gender.MALE, 100, 100, [], 0)
    tommy = GTACharacter("Tommy", Gender.MALE, 100, 100, [], 0)

    for sort in weapon_types:
        weapon = cj.buy_weapon(sort)
        assert weapon is None
        assert cj.buy_ammo(Weapon(sort)) is False
        assert cj.buy_ammo(weapon) is False
        assert tommy.buy_weapon(sort) is None
        assert tommy.buy_ammo(weapon) is False

    cj.money = 1_000_000
    smg = cj.buy_weapon(WeaponType.SMG)
    smg.ammo_in_inventory = 10

    assert shoot(cj, tommy, smg, 2) is False
    smg.reload()
    assert shoot(cj, tommy, smg, 11) is False
    assert shoot(cj, tommy, smg, 2) is True
    assert tommy.armor == 90
    assert tommy.health == 100

    assert shoot(cj, tommy, smg) is True
    assert tommy.armor == 50
    assert tommy.health == 100

    rpg = cj.buy_weapon(WeaponType.RPG)
    rpg.ammo_in_inventory = 10
    rpg.reload()
    assert shoot(cj, tommy, rpg, 2) is False
    assert shoot(cj, tommy, rpg) is True
    assert tommy.armor == 50
    assert tommy.health == 20
    assert shoot(cj, tommy, rpg, 1) is False

    rpg.reload()
    assert shoot(cj, tommy, rpg, 1) is True
    assert tommy.armor == 50
    assert tommy.health == 0
    assert tommy.dead is True

    rpg.reload()
    with pytest.raises(DeadPlayerException):
        shoot(cj, tommy, rpg, 1)

    tommy.dead = False
    tommy.health = 100
    cj.health = 0

    rpg.reload()
    with pytest.raises(DeadPlayerException):
        shoot(cj, tommy, rpg, 1)


def test_add_money():
    cj = GTACharacter("Carl Johnson", Gender.MALE, 100, 100, [], 1_000_000_000)
    cj.money += 2_000_000_000
    assert cj.money == 1_000_000_000
    cj.money += 1_000_000_000
    assert cj.money == 2_000_000_000
    cj.money += 147_483_647
    assert cj.money == 2_147_483_647
    cj.money += 1
    assert cj.money == 2_147_483_647


def test_remove_money():
    cj = GTACharacter("Carl Johnson", Gender.MALE, 100, 100, [], 1_000_000_000)
    cj.money -= 1_100_000_000
    cj.money -= 1_000_000_001
    assert cj.money == 1_000_000_000

    cj.money -= 200_000_000
    assert cj.money == 800_000_000

    cj.money -= 800_000_000
    assert cj.money == 0


def test_buy_armor():
    cj = GTACharacter("Carl Johnson", Gender.MALE, 70, 70, [], 10_000_000)
    cj.buy_armor()
    assert cj.money == 9_999_000
    assert cj.armor == 100
    assert cj.health == 70

    cj.dead = True
    with pytest.raises(DeadPlayerException):
        cj.buy_armor()


def test_buy_health():
    cj = GTACharacter("Carl Johnson", Gender.MALE, 70, 70, [], 10_000_000)
    cj.buy_health()
    assert cj.money == 9_998_000
    assert cj.health == 100
    assert cj.armor == 70

    cj.dead = True
    with pytest.raises(DeadPlayerException):
        cj.buy_health()


def test_earn_money_with_not_enough_money():
    player = GTACharacter("John", Gender.MALE, 100, 0, [], 9_999)
    assert player.earn_money(JobType.RACE) == 0
    player.money += 10_000
    assert player.earn_money(JobType.DELIVERY) == 0


def test_earn_money_with_enough_money():
    weapon1 = Weapon(WeaponType.PISTOL)
    weapon2 = Weapon(WeaponType.SMG)
    player = GTACharacter("John", Gender.MALE, 100, 100, [weapon1, weapon2], 0)

    assert player.earn_money(JobType.BANK_HEIST) == 0
    player.money = 10_000
    assert player.health == 65
    assert player.armor == 40
    player.health = 100
    player.armor = 100

    assert player.earn_money(JobType.RACE) == -10_000
    assert player.money == 0
    player.money = 14_213
    assert player.earn_money(JobType.RACE) == 14_213
    assert player.money == 28_426
    assert player.earn_money(JobType.RACE) == -28_426
    assert player.money == 0

    player.money = 81_252
    assert player.earn_money(JobType.DELIVERY) == -20_000
    assert player.money == 61_252
    assert player.earn_money(JobType.DELIVERY) == -20_000
    assert player.money == 41_252
    assert player.earn_money(JobType.DELIVERY) == 80_000
    assert player.money == 121_252
    assert player.earn_money(JobType.DELIVERY) == -20_000
    assert player.money == 101_252

    player.money = 10_000
    assert player.earn_money(JobType.BANK_HEIST) == 2_500
    assert player.money == 12_500
    player.health = 100
    player.armor = 100

    assert player.earn_money(JobType.BANK_HEIST) == 3_125
    assert player.money == 15_625
    player.health = 100
    player.armor = 100

    assert player.earn_money(JobType.BANK_HEIST) == 11_719
    assert player.money == 27_344
    assert player.health == 5
    assert player.armor == 5


def test_earn_money_with_not_enough_health_or_armor():
    player = GTACharacter("John", Gender.MALE, 80, 79, [], 1_000_000)
    assert player.earn_money(JobType.BANK_HEIST) == 0
    player.health = 79
    player.armor = 80
    assert player.earn_money(JobType.BANK_HEIST) == 0
    player.armor = 0
    assert player.earn_money(JobType.DELIVERY) == 0
    player.health = 50
    player.armor = 49
    assert player.earn_money(JobType.DELIVERY) == 0
    player.health = 49
    player.armor = 50
    assert player.earn_money(JobType.DELIVERY) == 0


def test_earn_money_bank_with_enough_health_and_armor():
    player = GTACharacter("John", Gender.MALE, 80, 79, [], 20000)
    assert player.earn_money(JobType.BANK_HEIST) == 0
    player.health = 79
    player.armor = 80
    assert player.earn_money(JobType.BANK_HEIST) == 0
    player.armor = 0
    assert player.earn_money(JobType.DELIVERY) == 0
    player.health = 50
    player.armor = 49
    assert player.earn_money(JobType.DELIVERY) == 0
    player.health = 49
    player.armor = 50
    assert player.earn_money(JobType.DELIVERY) == 0


def test_earn_money_with_not_enough_weapons():
    player = GTACharacter("John", Gender.MALE, 100, 100, [], 1_000_000)
    assert player.earn_money(JobType.DELIVERY) == 0
    assert player.earn_money(JobType.BANK_HEIST) == 0
    player.buy_weapon(WeaponType.PISTOL)
    assert player.earn_money(JobType.BANK_HEIST) == 0


def test_earn_money_character_dies():
    weapon1 = Weapon(WeaponType.PISTOL)
    weapon2 = Weapon(WeaponType.SMG)
    player = GTACharacter("John", Gender.MALE, 100, 100, [weapon1, weapon2], 1_000_000)

    for i in range(3):
        assert player.earn_money(JobType.BANK_HEIST) != 0
        player.health = 80
        player.armor = 80

    assert player.earn_money(JobType.BANK_HEIST) == 0
    assert player.dead


def test_earn_money_with_invalid_job_type():
    weapon1 = Weapon(WeaponType.PISTOL)
    weapon2 = Weapon(WeaponType.SMG)
    player = GTACharacter("John", Gender.MALE, 100, 100, [weapon1, weapon2], 1_000_000)
    assert player.earn_money("unga-bunga") == 0
    assert player.money == 1_000_000


def test_earn_money_when_player_is_dead():
    player = GTACharacter("John", Gender.MALE, 0, 0, [Weapon(WeaponType.SMG), Weapon(WeaponType.SMG)], 1_000_000_000)

    with pytest.raises(DeadPlayerException):
        player.earn_money(JobType.RACE)
    with pytest.raises(DeadPlayerException):
        player.earn_money(JobType.DELIVERY)
    with pytest.raises(DeadPlayerException):
        player.earn_money(JobType.BANK_HEIST)
