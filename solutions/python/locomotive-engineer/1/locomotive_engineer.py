"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    return each_wagons_id[2:3] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    new_list_1 = [wagons_rows[0][0]] + [wagons_rows[1][0]] + [wagons_rows[2][0]]
    new_list_2 = [wagons_rows[0][1]] + [wagons_rows[1][1]] + [wagons_rows[2][1]]
    new_list_3 = [wagons_rows[0][2]] + [wagons_rows[1][2]] + [wagons_rows[2][2]]
    
    return [new_list_1, new_list_2, new_list_3]
