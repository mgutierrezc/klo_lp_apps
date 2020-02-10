doc = """"
Control parameters for MoneyPolitics
"""

task_endowments = [125, 80, 40, 25, 25, 15, 15, 15, 9]
possible_message_receivers = [['125', 'Income 125'], ['80', 'Income 80'], ['40', 'Income 40'],
                              ['251', 'Income 25 (Player 2)'], ['250', 'Income 25 (Player 1)'],
                              ['152', 'Income 15 (Player 3)'], ['151', 'Income 15 (Player 2)'],
                              ['150', 'Income 15 (Player 1)'], ['9', 'Income 9'], ]
message_cost = 1
number_of_messages = 1
possible_tax_systems = [[0, 'Progressivity System'], [1, "Tax Rate System"]]