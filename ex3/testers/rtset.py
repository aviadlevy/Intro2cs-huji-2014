constant = [('constant_pension', [0, 0, 3.5, 20], {}, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            ('constant_pension', [0, 12.5, -17, 5], {}, [0.0, 0.0, 0.0, 0.0, 0.0]),
            ('constant_pension', [1.5, 0, -18, 20], {}, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            ('constant_pension', [1.5, 12.5, -100, 0], {}, []),
            ('constant_pension', [100, 100, 0, 1], {}, [100.0]),
            ('constant_pension', [1.5, 25, -19, 20], {}, [0.375, 0.67875, 0.9247875, 1.124077875, 1.2855030787500001, 1.4162574937875, 1.522168569967875, 1.607956541673979, 1.6774447987559231, 1.733730286992298, 1.7793215324637615, 1.8162504412956468, 1.846162857449474, 1.870391914534074, 1.8900174507726, 1.905914135125806, 1.918790449451903, 1.9292202640560416, 1.937668413885394, 1.9445114152471692]),
            ('constant_pension', [100, 100, 7.5, 20], {}, [100.0, 207.5, 323.0625, 447.2921875, 580.8391015625, 724.4020341796875, 878.732186743164, 1044.6371007489013, 1222.984883305069, 1414.708749552949, 1620.81190576942, 1842.3727987021264, 2080.550758604786, 2336.592065500145, 2611.8364704126557, 2907.7242056936047, 3225.803521120625, 3567.738785204672, 3935.319194095022, 4330.468133652148]),
            ('constant_pension', [1.5, 25, 118, 5], {}, [0.375, 1.1925, 2.9746499999999996, 6.859736999999998, 15.329226659999994]),
            ('constant_pension', [100, 25, 119, 5], {}, [25.0, 79.75, 199.6525, 462.238975, 1037.30335525]),
            ('constant_pension', [], {'growth_rate': 4.5, 'salary': 80, 'save': 100, 'years': 20}, [80.0, 163.6, 250.962, 342.25528999999995, 437.6567780499999, 537.3513330622499, 641.5321430500511, 750.4010894873034, 864.1691385142319, 983.0567497473722, 1107.2943034860039, 1237.122547142874, 1372.7930617643033, 1514.5687495436969, 1662.7243432731632, 1817.5469387204555, 1979.336550962876, 2148.406695756205, 2325.084997065234, 2509.713821933169])]

variable = [('variable_pension', [100, 20.0, []], {}, []),
            ('variable_pension', [100, 20.0, [10]], {}, [20.0]),
            ('variable_pension', [100, 20.0, [10, 15]], {}, [20.0, 43.0]),
            ('variable_pension', [100, 20.0, [0, 0, 0, 0, 0, 0, 0, 0]], {}, [20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0]),
            ('variable_pension', [100, 20.0, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]], {}, [20.0, 42.0, 66.2, 92.82000000000001, 122.10200000000002, 154.31220000000002, 189.74342000000004, 228.71776200000005, 271.5895382000001, 318.7484920200001, 370.6233412220002, 427.68567534420026, 490.45424287862033]),
            ('variable_pension', [100, 20.0, [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20]], {}, [20.0, 42.5, 71.0, 87.45, 118.38125000000001, 162.0575, 173.954625, 215.698953125, 278.83874375, 284.8968065625, 340.5089073828125, 428.610688859375]),
            ('variable_pension', [100, 0.0, [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20]], {}, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            ('variable_pension', [0, 20.0, [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20]], {}, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            ('variable_pension', [250, 12.5, [5, 12.5, -20, -5, 12.5, 20, 5, 12.5, -20, -5, 12.5, 20]], {}, [31.25, 66.40625, 84.375, 111.40625, 156.58203125, 219.1484375, 261.355859375, 325.275341796875, 291.4702734375, 308.146759765625, 377.91510473632815, 484.74812568359374]),
            ('variable_pension', [], {'growth_rates': [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20], 'salary': 100, 'save': 20.0}, [20.0, 42.5, 71.0, 87.45, 118.38125000000001, 162.0575, 173.954625, 215.698953125, 278.83874375, 284.8968065625, 340.5089073828125, 428.610688859375])]

choose = [('choose_best_fund', [100, 25, 'file_0'], {}, ('f0', 305.9737111539997)),
          ('choose_best_fund', [100, 25, 'file_1'], {}, ('f0', 25.0)),
          ('choose_best_fund', [100, 25, 'file_2'], {}, ('f4', 307.20523429605385)),
          ('choose_best_fund', [100, 25, 'file_3'], {}, ('f3', 308.01539286341097)),
          ('choose_best_fund', [], {'funds_file': 'file_4', 'salary': 100, 'save': 25}, ('f3', 307.20523429605385))]

growth = [('growth_in_year', [[10], -2], {}, None),
          ('growth_in_year', [[10], -1], {}, None),
          ('growth_in_year', [[10], 0], {}, 10),
          ('growth_in_year', [[10], 1], {}, None),
          ('growth_in_year', [[10, 11, 12, 13, 14], -7], {}, None),
          ('growth_in_year', [[11, 13, 15, 17, 19], -2], {}, None),
          ('growth_in_year', [[12, 15, 18, 21, 24], 0], {}, 12),
          ('growth_in_year', [[13, 17, 21, 25, 29], 2], {}, 21),
          ('growth_in_year', [[14, 19, 24, 29, 34], 5], {}, None),
          ('growth_in_year', [], {'growth_rates': [10, 11, 12, 13, 14], 'year': 4}, 14)]

inflation = [('inflation_growth_rates', [[3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6], [2, 3.5, 5, 2, 3.5, 5, 2, 3.5, 5, 2, 3.5, 5]], {}, [0.9803921568627416, 0.48309178743961567, 0.0, 3.9215686274509887, -0.48309178743961567, -0.952380952380949, 2.941176470588225, 2.4154589371980784, -1.904761904761909, 1.9607843137254832, 1.449275362318847, 0.952380952380949]),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3, 4], [2, 3.5, 5, 2, 3.5, 5, 2, 3.5, 5, 2, 3.5, 5]], {}, [0.9803921568627416, 0.48309178743961567, 0.0, 3.9215686274509887, -0.48309178743961567, -0.952380952380949]),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6], [2, 3.5, 5, 2, 3.5, 5]], {}, [0.9803921568627416, 0.48309178743961567, 0.0, 3.9215686274509887, -0.48309178743961567, -0.952380952380949, 5, 6, 3, 4, 5, 6]),
             ('inflation_growth_rates', [[], [2, 3.5, 5, 2, 3.5, 5, 2, 3.5, 5, 2, 3.5, 5]], {}, []),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6], []], {}, [3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6]),
             ('inflation_growth_rates', [[3, 4, 5, 6], [0, 0, 0, 0]], {}, [3.0000000000000027, 4.0000000000000036, 5.000000000000004, 6.000000000000005]),
             ('inflation_growth_rates', [[0, 0, 0], [2, 3.5, 5]], {}, [-1.9607843137254943, -3.3816425120772986, -4.761904761904767]),
             ('inflation_growth_rates', [[0, 0, 0], [0, 0, 0]], {}, [0.0, 0.0, 0.0]),
             ('inflation_growth_rates', [[0], [0]], {}, [0.0]),
             ('inflation_growth_rates', [], {'growth_rates': [3, 4, 5], 'inflation_factors': [2, 4.5, 5]}, [0.9803921568627416, -0.4784688995215336, 0.0])]

post = [('post_retirement', [1000.0, [], 700], {}, []),
        ('post_retirement', [1000.0, [10], 700], {}, [400.0]),
        ('post_retirement', [1000.0, [10, 15], 700], {}, [400.0, -240.00000000000006]),
        ('post_retirement', [1000.0, [0, 0, 0, 0, 0, 0, 0, 0, 0], 111], {}, [889.0, 778.0, 667.0, 556.0, 445.0, 334.0, 223.0, 112.0, 1.0]),
        ('post_retirement', [1000.0, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 70], {}, [1030.0, 1063.0, 1099.3000000000002, 1139.2300000000002, 1183.1530000000005, 1231.4683000000007, 1284.6151300000008, 1343.076643000001, 1407.3843073000012, 1478.1227380300015, 1555.935011833002, 1641.5285130163022, 1735.6813643179325]),
        ('post_retirement', [1000.0, [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20], 50], {}, [900.0, 962.5, 1105.0, 999.75, 1074.71875, 1239.6625, 1127.679375, 1218.639296875, 1412.3671562499999, 1291.7487984374998, 1403.2173982421873, 1633.8608778906248]),
        ('post_retirement', [1000.0, [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20], 90], {}, [860.0, 877.5, 963.0, 824.8499999999999, 837.95625, 915.5474999999999, 779.7701249999999, 787.2413906249999, 854.6896687499998, 721.9551853124998, 722.1995834765622, 776.6395001718746]),
        ('post_retirement', [1000.0, [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20], 200], {}, [750.0, 643.75, 572.5, 343.875, 186.859375, 24.23124999999999, -176.98031250000003, -399.10285156250006, -678.923421875, -844.97725078125, -1150.5994071289063, -1580.7192885546874]),
        ('post_retirement', [1000.0, [5, 12.5, -20, -5, 12.5, 20, 5, 12.5, -20, -5, 12.5, 20], 120], {}, [930.0, 926.25, 621.0, 469.94999999999993, 408.6937499999999, 370.4324999999999, 268.9541249999999, 182.5733906249999, 26.058712499999928, -95.24422312500008, -227.1497510156251, -392.57970121875013]),
        ('post_retirement', [], {'expenses': 100.0, 'growth_rates': [-5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20, -5, 12.5, 20], 'savings': 1000}, [850.0, 856.25, 927.5, 781.125, 778.765625, 834.51875, 692.7928125, 679.3919140625, 715.2702968749999, 579.5067820312498, 551.945129785156, 562.3341557421872])]

badinputs = [('constant_pension', [-200,15,10,8],{},None),
             ('constant_pension', [-0.5,15,10,8],{},None),
             ('constant_pension', [1000,-5,10,8],{},None),
             ('constant_pension', [1000,-0.1,10,8],{},None),
             ('constant_pension', [1000,115,10,8],{},None),
             ('constant_pension', [1000,100.4,10,8],{},None),
             ('constant_pension', [1000,15,-130,8],{},None),
             ('constant_pension', [1000,15,-100.1,8],{},None),
             ('constant_pension', [1000,15,10,-1],{},None),
             ('constant_pension', [1000,15,10,-10],{},None),
             ('variable_pension', [-150,15,[10,12,14,-5,10,12,14]],{},None),
             ('variable_pension', [-0.3,15,[10,12,14,-5,10,12,14]],{},None),
             ('variable_pension', [1000,-15,[10,12,14,-5,10,12,14]],{},None),
             ('variable_pension', [1000,-0.2,[10,12,14,-5,10,12,14]],{},None),
             ('variable_pension', [1000,215,[10,12,14,-5,10,12,14]],{},None),
             ('variable_pension', [1000,105,[10,12,14,-5,10,12,14]],{},None),
             ('variable_pension', [1000,15,[-210,12,14,-5,10,12.0,14.0]],{},None),
             ('variable_pension', [1000,15,[10,-112,14,-5,10,12.0,14.0]],{},None),
             ('variable_pension', [1000,15,[-114]],{},None),
             ('variable_pension', [1000,15,[10,12,14,-5,10,12.0,-414.0]],{},None),
             ('choose_best_fund', [-1000,15,"file_1"],{},None),
             ('choose_best_fund', [-0.2,15,"file_1"],{},None),
             ('choose_best_fund', [1000,-15,"file_1"],{},None),
             ('choose_best_fund', [1000,-0.15,"file_1"],{},None),
             ('choose_best_fund', [1000,111,"file_1"],{},None),
             ('growth_in_year', [[10,12,14,-5,10,12,14],-10],{},None),
             ('growth_in_year', [[10,12,14,-5,10,12,14],-1],{},None),
             ('growth_in_year', [[10,12,14,-5,10,12,14],7],{},None),
             ('growth_in_year', [[10,12,14,-5,10,12,14],17],{},None),
             ('growth_in_year', [[],1],{},None),
             ('inflation_growth_rates', [[-103, 4, 5, 6, 3], [2, 3.5, 5, 2, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6, -123], [2, 3.5, 5, 2, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3], [-102, 3.5, 5, 2, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3], [2, 3.5, 5, -102, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6], [2, 3.5, 5, 2, -123.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6, -333], [2, 3.5, 5, 2]],{},None),
             ('inflation_growth_rates', [[-223, 4, 5, 6, 3], [-222, 3.5, 5, 2, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3], [-100, 3.5, 5, 2, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6, 3], [2, 3.5, -100, 2, 3.5]],{},None),
             ('inflation_growth_rates', [[3, 4, 5, 6], [2, 3.5, 5, 2, -100]],{},None),

             ('post_retirement', [-100,[3,4,5,6,3,4,5,6,3,4,5,6],150],{},None),
             ('post_retirement', [-0.4,[3,4,5,6,3,4,5,6,3,4,5,6],150],{},None),
             ('post_retirement', [1000,[3,4,5,6,3,4,5,6,3,4,5,6],-150],{},None),
             ('post_retirement', [1000,[3,4,5,6,3,4,5,6,3,4,5,6],-0.7],{},None),

             ('post_retirement', [1000,[3,-144,5,6,3,4,5,6,3,4,5,6],150],{},None),
             ('post_retirement', [1000,[3,4,5,6,3,4,5,-666,3,4,5,6],150],{},None),
             ('post_retirement', [1000,[3,4,5,6,3,4,5,6,3,4,5,-116],150],{},None),
             ('post_retirement', [1000,[-103,-104,-105,-106,-103,-104,-105,-106,-103,-104,-105,-106],150],{},None),
             ('post_retirement', [1000,[-103,4,-105,6,-103,4,-105,6,-103,4,-105,6],150],{},None),
             ('post_retirement', [1000,[3,-104,5,-106,3,-104,5,-106,3,-104,5,-106],150],{},None)
             ]

rtset={
    "constant"  : constant,
    "variable"  : variable,
    "choose"    : choose,
    "growth"    : growth,
    "inflation" : inflation,
    "post"      : post,
    "badinputs" : badinputs,
    }
