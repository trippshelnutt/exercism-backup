""" Meltdown Mitigation exercise """

MAXIMUM_TEMPERATURE = 800
MINIMUM_NEUTRONS_EMITTED = 500
MAXIMUM_PRODUCT_OF_TEMPERATURE_AND_NEUTRONS_EMITTED = 500000

EFFICIENCY_GREEN = 80
EFFICIENCY_ORANGE = 60
EFFICIENCY_RED = 30

NORMAL_STATUS_MINIMUM = 90
NORMAL_STATUS_MAXIMUM = 110


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: temperature value in kelvin (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature >= MAXIMUM_TEMPERATURE:
        return False

    if neutrons_emitted <= MINIMUM_NEUTRONS_EMITTED:
        return False

    product_of_temperature_and_neurons_emitted = temperature * neutrons_emitted

    if product_of_temperature_and_neurons_emitted >= \
            MAXIMUM_PRODUCT_OF_TEMPERATURE_AND_NEUTRONS_EMITTED:
        return False

    return True


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    efficiency = generated_power / theoretical_max_power * 100

    if efficiency >= EFFICIENCY_GREEN:
        return "green"

    if efficiency >= EFFICIENCY_ORANGE:
        return "orange"

    if efficiency >= EFFICIENCY_RED:
        return "red"

    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature in kelvin (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """

    product_of_temperature_and_neurons_per_second = temperature * \
        neutrons_produced_per_second

    status = product_of_temperature_and_neurons_per_second / threshold * 100

    if status < NORMAL_STATUS_MINIMUM:
        return "LOW"

    if status >= NORMAL_STATUS_MINIMUM and status <= NORMAL_STATUS_MAXIMUM:
        return "NORMAL"

    return "DANGER"
