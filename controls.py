doc = """"
Control parameters for MoneyPolitics
"""

task_endowments = [125, 80, 40, 25, 25, 15, 15, 15, 9]
possible_message_receivers = [[['125', '1'], 'Income 125'], [['80', '1'], 'Income 80'],
                       [['40', '1'], 'Income 40'], [['25', '2'], 'Income 25 (Player 2)'],
                       [['25', '1'], 'Income 25 (Player 1)'], [['15', '3'], 'Income 15 (Player 3)'],
                       [['15', '2'], 'Income 15 (Player 2)'], [['15', '1'], 'Income 15 (Player 1)'],
                       [['9','1'], 'Income 9'], [['0', '0'], 'None']]
message_cost = 1
number_of_messages = 1
possible_tax_systems = [[0, 'Progressivity System'], [1, "Tax Rate System"]]
