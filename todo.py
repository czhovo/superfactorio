TODOS=[
    # base/prototypes/entity/entities.lua, 
    {'special': False, 
     'file':'base/prototypes/entity/entities.lua', 'TODO':[
        {'item':'add_full_resistances_function'},
        {'item': '"character"', 'adjustments': [
            ('add_full_resistances', '', ''),
            ('collision_box', '{{-0.2, -0.2}, {0.2, 0.2}}', '{{-0., -0.}, {0., 0.}}'),
            ('inventory_size', '80', '2000'),
            ('build_distance', '10', '100'),
            ('drop_item_distance', '10', '100'),
            ('reach_distance', '10', '100'),
            ('item_pickup_distance', '1', '10'),
            ('enter_vehicle_distance', '3', '10'),
            ('reach_resource_distance', '2.7', '100'),
            ('grounded_landing_search_radius', '5', '100'),
            ('running_speed', '0.15', '0.9'),
            ('mining_speed', '0.5', '50'),
        ]},
        {'item': '"fast-inserter"', 'adjustments': [
            ('add_full_resistances', '', ''),
            ('energy_per_movement', '"7kJ"', '"7J"'),
            ('energy_per_rotation', '"7kJ"', '"7J"'),
            ('extension_speed', '0.1', '1.25'),
            ('rotation_speed', '0.04', '0.5')
        ]},
        {'item': '"long-handed-inserter"', 'adjustments': [
            ('energy_per_movement', '"5kJ"', '"5J"'),
            ('energy_per_rotation', '"5kJ"', '"5J"'),
            ('extension_speed', '0.05', '0.625'),
            ('rotation_speed', '0.02', '0.25')
        ]},
        # container
        {'item': '"iron-chest"', 'adjustments':[
            ('inventory_size', '32', '8000'),
        ]},
        # manufacturing machines
        {'item': '"stone-furnace"', 'adjustments':[
            ('crafting_speed', '1', '30'),
        ]},
        {'item': '"assembling-machine-1"', 'adjustments':[
            ('crafting_speed', '0.5', '15'),
        ]},
        {'item': '"assembling-machine-2"', 'adjustments':[
            ('crafting_speed', '0.75', '22.5'),
        ]},
        {'item': '"assembling-machine-3"', 'adjustments':[
            ('crafting_speed', '1.25', '37.5'),
        ]},
        {'item': '"electric-furnace"', 'adjustments':[
            ('crafting_speed', '2', '60'),
        ]},
        {'item': '"steel-furnace"', 'adjustments':[
            ('crafting_speed', '2', '60'),
        ]},
        {'item': '"oil-refinery"', 'adjustments':[
            ('crafting_speed', '1', '30'),
        ]},
        {'item': '"chemical-plant"', 'adjustments':[
            ('crafting_speed', '1', '30'),
        ]},
        {'item': '"centrifuge"', 'adjustments':[
            ('crafting_speed', '1', '30'),
        ]},
        # electricity
        {'item': '"solar-panel"', 'adjustments':[
            ('production', '"60kW"', '"600MW"'),
        ]},
        {'item': '"accumulator"', 'adjustments':[
            ('buffer_capacity', '"5MJ"', '"5GJ"'),
            ('input_flow_limit', '"300kW"', '"300MW"'),
            ('output_flow_limit', '"300kW"', '"300MW"'),
        ]},
        {'item': '"small-electric-pole"', 'adjustments':[
            ('add_light', '', ''),
        ]},
        # radar
        {'item': ' "radar"', 'adjustments':[
            ('max_distance_of_sector_revealed', '14', '100'),
            ('max_distance_of_nearby_sector_revealed', '3', '50'),
        ]},
        # tank
        {'item': '"tank"', 'adjustments':[
            ('add_full_resistances', '', ''),
            ('resistances', '', ''),
            ('braking_power', '"800kW"', '"80MW"'),
            ('consumption', '"600kW"', '"60MW"'),
        ]},
        # wall
        {'item': '"stone-wall"', 'adjustments':[
            ('add_full_resistances', '', ''),
            ('resistances', '', ''),
        ]},
    ]},

    # base/prototypes/entity/transport-belts.lua
    {'special': False, 
     'file':'base/prototypes/entity/transport-belts.lua', 'TODO':[
        {'item': '"transport-belt"', 'adjustments':[
            ('speed', '0.03125', '0.625'),
        ]},
        {'item': '"underground-belt"', 'adjustments':[
            ('speed', '0.03125', '0.625'),
        ]},
        {'item': '"splitter"', 'adjustments':[
            ('speed', '0.03125', '0.625'),
        ]},
    ]},

    # base/prototypes/entity/mining-drill.lua
    {'special': False, 
     'file':'base/prototypes/entity/mining-drill.lua', 'TODO':[
        {'item': '"electric-mining-drill"', 'adjustments':[
            ('mining_speed', '0.5', '50'),
        ]},
        {'item': '"pumpjack"', 'adjustments':[
            ('mining_speed', '1', '60'),
        ]},
    ]},

    # base/prototypes/entity/trains.lua
    {'special': False, 
     'file':'base/prototypes/entity/trains.lua', 'TODO':[
        {'item': '"locomotive"', 'adjustments':[
            ('max_speed', '1.2', '12'),
            ('max_power', '"600kW"', '"6000kW"'),
            ('braking_force', '10', '100'),
        ]},
        {'item': '"cargo-wagon"', 'adjustments':[
            ('max_speed', '1.5', '6'),
        ]},
        {'item': '"fluid-wagon"', 'adjustments':[
            ('max_speed', '1.5', '6'),
        ]},
    ]},

    # base/prototypes/entity/flying-robots.lua
    {'special': False, 
     'file':'base/prototypes/entity/flying-robots.lua', 'TODO':[
        {'item': '"logistic-robot"', 'adjustments':[
            ('max_payload_size', '1', '10'),
            ('speed', '0.05', '0.5'),
        ]},
        {'item': '"construction-robot"', 'adjustments':[
            ('max_payload_size', '1', '10'),
            ('speed', '0.06', '0.6'),
        ]},
    ]},

    # base/prototypes/entity/turrets.lua
    {'special': False, 
     'file':'base/prototypes/entity/turrets.lua', 'TODO':[
        {'item':'add_full_resistances_function'},
        {'item': '"gun-turret"', 'adjustments':[
            ('add_full_resistances', '', ''),
        ]},
    ]},

    # base/prototypes/entity/resource.lua
    {'special': True, 
     'file':'base/prototypes/entity/resource.lua', 'TODO':[
         {'item':'adjust_function_resource'},
    ]},

    # base/prototypes/recipe.lua
    {'special': False, 
     'file':'base/prototypes/recipe.lua', 'TODO':[
        {'item': '""', 'adjustments':[
            ('enabled', 'false', 'true'),
        ]},
        {'item': '""', 'adjustments':[
            ('enabled', 'false', 'true'),
        ]},
        {'item': '""', 'adjustments':[
            ('enabled', 'false', 'true'),
        ]},
        {'item': '""', 'adjustments':[
            ('enabled', 'false', 'true'),
        ]},
        {'item': '""', 'adjustments':[
            ('enabled', 'false', 'true'),
        ]},
        {'item': '""', 'adjustments':[
            ('enabled', 'false', 'true'),
        ]},
    ]},

    # base/prototypes/item.lua
    {'special': False, 
     'file':'base/prototypes/item.lua', 'TODO':[
        {'item': '"coal"', 'adjustments':[
            ('fuel_value', '"4MJ"', '"400GJ"'),
        ]},
        {'item': '"submachine-gun"', 'adjustments':[
            ('cooldown', '6', '0.1'),
            ('movement_slow_down_factor', '0.7', '0'),
            ('range', '18', '100'),
        ]},
        {'item': '"firearm-magazine"', 'adjustments':[
            ('damage', '{amount = 5, type = "physical"}', '{amount = 5000, type = "physical"}'),
        ]},
    ]},

    # space-age/prototypes/entity/entities.lua
    {'special': False, 
     'file':'space-age/prototypes/entity/entities.lua', 'TODO':[
        {'item':'add_full_resistances_function'},
        {'item': '"asteroid-collector"', 'adjustments':[
            ('add_full_resistances', '', ''),
            ('inventory_size', '39', '399'),
        ]},
        {'item': '"cargo-bay"', 'adjustments':[
            ('inventory_size_bonus', '20', '2000'),
        ]},
        {'item': '"electromagnetic-plant"', 'adjustments':[
            ('crafting_speed', '2', '20'),
        ]},
        {'item': '"foundry"', 'adjustments':[
            ('crafting_speed', '4', '40'),
        ]},
        {'item': '"thruster"', 'adjustments':[
            ('max_performance', '{fluid_volume = 0.8, fluid_usage = 2, effectivity = 0.51}', '{fluid_volume = 0.8, fluid_usage = 2, effectivity = 5.1}'),
        ]},
    ]},

    # space-age/prototypes/entity/big-mining-drill.lua
    {'special': False, 
     'file':'space-age/prototypes/entity/big-mining-drill.lua', 'TODO':[
        {'item': '"big-mining-drill"', 'adjustments':[
            ('mining_speed', '2.5', '25'),
        ]},
    ]},

    # space-age/prototypes/technology.lua
    {'special': True, 
     'file':'space-age/prototypes/technology.lua', 'TODO':[
        {'item': 'adjust_agricultural_science_pack_technology'},
        # 还要修改其他必要草星科技的解锁条件
    ]},

    # space-age/prototypes/recipe.lua
    {'special': False, 
     'file':'space-age/prototypes/recipe.lua', 'TODO':[
        {'item': '"scrap-recycling"', 'adjustments':[
            ('{type = "item", name = "ice",                    amount = 1, probability', '0.05', '0.25'), 
            ('{type = "item", name = "holmium-ore",            amount = 1, probability', '0.01', '0.21'), 
        ]},
    ]},

    {'special': True, 
     'file':'space-age/prototypes/recipe.lua', 'TODO':[
         {'item': 'adjust_agricultural_science_pack_recipe'},
         {'item': 'vulcanus_mineral_production_increase'},
    ]},
]