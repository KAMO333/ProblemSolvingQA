"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = {}

    for product in  items:
        if product in inventory:
            inventory[product] += 1
        else:
            inventory[product] = 1
    
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for product in  items:
        if product in inventory:
            inventory[product] += 1
        else:
            inventory[product] = 1
    
    return inventory



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for product in  items:
        if product not in inventory:
            continue
        if product in inventory:
            inventory[product] -= 1
            
        if inventory[product] < 0:
            inventory[product] = 0
    
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    new_inventory = inventory.copy()

    for product in new_inventory.keys():
        if product == item:
            inventory.pop(product)

    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    results = []

    for product in inventory:
        if inventory[product] == 0:
            continue
        results.append((product, inventory[product]))

    return results