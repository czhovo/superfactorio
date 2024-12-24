def trigger(line):

	nlspace=len(line)-len(line.lstrip())

	line=line.strip()

	todolist=[]

	if line=='name = "character",':
		todolist.append(('add_full_resistances', '', ''))
		todolist.append(('collision_box', '{{-0.2, -0.2}, {0.2, 0.2}}', '{{-0., -0.}, {0., 0.}}'))
		todolist.append(('inventory_size', '80', '2000'))
		todolist.append(('build_distance', '10', '100'))
		todolist.append(('drop_item_distance', '10', '100'))
		todolist.append(('reach_distance', '10', '100'))
		todolist.append(('item_pickup_distance', '1', '10'))
		todolist.append(('enter_vehicle_distance', '3', '10'))
		todolist.append(('reach_resource_distance', '2.7', '100'))
		todolist.append(('grounded_landing_search_radius', '5', '100'))
		todolist.append(('running_speed', '0.15', '0.9'))
		todolist.append(('mining_speed', '0.5', '50'))

	elif line=='name = "fast-inserter",':
		todolist.append(('add_full_resistances', '', ''))
		todolist.append(('energy_per_movement', '"7kJ"', '"7J"'))
		todolist.append(('energy_per_rotation', '"7kJ"', '"7J"'))
		todolist.append(('extension_speed', '0.1', '1.25'))
		todolist.append(('rotation_speed', '0.04', '0.5'))

	elif line=='name = "long-handed-inserter",':
		todolist.append(('energy_per_movement', '"5kJ"', '"5J"'))
		todolist.append(('energy_per_rotation', '"5kJ"', '"5J"'))
		todolist.append(('extension_speed', '0.05', '0.625'))
		todolist.append(('rotation_speed', '0.02', '0.25'))

	elif line=='name = "iron-chest",':
		todolist.append(('inventory_size', '32', '8000'))

	elif line=='name = "stone-furnace",':
		todolist.append(('crafting_speed', '1', '30'))

	elif line=='name = "assembling-machine-1",':
		todolist.append(('crafting_speed', '0.5', '15'))

	elif line=='name = "assembling-machine-2",':
		todolist.append(('crafting_speed', '0.75', '22.5'))

	elif line=='name = "assembling-machine-3",':
		todolist.append(('crafting_speed', '1.25', '37.5'))

	elif line=='name = "electric-furnace",':
		todolist.append(('crafting_speed', '2', '60'))

	elif line=='name = "steel-furnace",':
		todolist.append(('crafting_speed', '2', '60'))

	elif line=='name = "oil-refinery",':
		todolist.append(('crafting_speed', '1', '30'))

	elif line=='name = "chemical-plant",':
		todolist.append(('crafting_speed', '1', '30'))

	elif line=='name = "centrifuge",':
		todolist.append(('crafting_speed', '1', '30'))

	elif line=='name = "solar-panel",':
		todolist.append(('production', '"60kW"', '"600MW"'))

	elif line=='name = "accumulator",':
		todolist.append(('buffer_capacity', '"5MJ"', '"5GJ"'))
		todolist.append(('input_flow_limit', '"300kW"', '"300MW"'))
		todolist.append(('output_flow_limit', '"300kW"', '"300MW"'))

	elif line=='name = "small-electric-pole",':
		todolist.append(('add_light', '', ''))

	elif line=='name =  "radar",':
		todolist.append(('max_distance_of_sector_revealed', '14', '100'))
		todolist.append(('max_distance_of_nearby_sector_revealed', '3', '50'))

	elif line=='name = "tank",':
		todolist.append(('add_full_resistances', '', ''))
		todolist.append(('resistances', '', ''))
		todolist.append(('braking_power', '"800kW"', '"80MW"'))
		todolist.append(('consumption', '"600kW"', '"60MW"'))

	elif line=='name = "stone-wall",':
		todolist.append(('add_full_resistances', '', ''))
		todolist.append(('resistances', '', ''))

	return todolist, nlspace
