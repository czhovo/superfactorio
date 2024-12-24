TODO_base_entity_entities=[
    # base/prototypes/entity/entities.lua, 
     
    # character
    {'item': '"character"', 'entry': [
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
    # inserters
    {'item': '"fast-inserter"', 'entry': [
        ('add_full_resistances', '', ''),
        ('energy_per_movement', '"7kJ"', '"7J"'),
        ('energy_per_rotation', '"7kJ"', '"7J"'),
        ('extension_speed', '0.1', '1.25'),
        ('rotation_speed', '0.04', '0.5')
    ]},
    {'item': '"long-handed-inserter"', 'entry': [
        ('energy_per_movement', '"5kJ"', '"5J"'),
        ('energy_per_rotation', '"5kJ"', '"5J"'),
        ('extension_speed', '0.05', '0.625'),
        ('rotation_speed', '0.02', '0.25')
    ]},
    # container
    {'item': '"iron-chest"', 'entry':[
        ('inventory_size', '32', '8000'),
    ]},
    # manufacturing machines
    {'item': '"stone-furnace"', 'entry':[
        ('crafting_speed', '1', '30'),
    ]},
    {'item': '"assembling-machine-1"', 'entry':[
        ('crafting_speed', '0.5', '15'),
    ]},
    {'item': '"assembling-machine-2"', 'entry':[
        ('crafting_speed', '0.75', '22.5'),
    ]},
    {'item': '"assembling-machine-3"', 'entry':[
        ('crafting_speed', '1.25', '37.5'),
    ]},
    {'item': '"electric-furnace"', 'entry':[
        ('crafting_speed', '2', '60'),
    ]},
    {'item': '"steel-furnace"', 'entry':[
        ('crafting_speed', '2', '60'),
    ]},
    {'item': '"oil-refinery"', 'entry':[
        ('crafting_speed', '1', '30'),
    ]},
    {'item': '"chemical-plant"', 'entry':[
        ('crafting_speed', '1', '30'),
    ]},
    {'item': '"centrifuge"', 'entry':[
        ('crafting_speed', '1', '30'),
    ]},
    # electricity
    {'item': '"solar-panel"', 'entry':[
        ('production', '"60kW"', '"600MW"'),
    ]},
    {'item': '"accumulator"', 'entry':[
        ('buffer_capacity', '"5MJ"', '"5GJ"'),
        ('input_flow_limit', '"300kW"', '"300MW"'),
        ('output_flow_limit', '"300kW"', '"300MW"'),
    ]},
    {'item': '"small-electric-pole"', 'entry':[
        ('add_light', '', ''),
    ]},
    # radar
    {'item': ' "radar"', 'entry':[
        ('max_distance_of_sector_revealed', '14', '100'),
        ('max_distance_of_nearby_sector_revealed', '3', '50'),
    ]},
    # tank
    {'item': '"tank"', 'entry':[
        ('add_full_resistances', '', ''),
        ('resistances', '', ''),
        ('braking_power', '"800kW"', '"80MW"'),
        ('consumption', '"600kW"', '"60MW"'),
    ]},
    # wall
    {'item': '"stone-wall"', 'entry':[
        ('add_full_resistances', '', ''),
        ('resistances', '', ''),
    ]},
    
]


"""

    {'item': '"asteroid-collector"', 'entry': [
        ('add_full_resistances', '', ''),
        ('inventory_size', '39', '3999'),
        ('resistances', '', ''),
    ]},
    
"""

"""

    {'item': '', 'entry':[
        ('', '', ''),
    ]},
    
"""