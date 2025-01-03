
### recipe.lua
全部的 enabled = false 替换为 enabled = true




### item.lua
type = "item", name = "coal", fuel_value = "4MJ" -> "400GJ",
type = "gun", name = "submachine-gun", cooldown = 6 -> 0.1, movement_slow_down_factor = 0.7 -> 0, range = 18 -> 100,
type = "ammo", name = "firearm-magazine", damage = {amount = 5 -> 5000, type = "physical"}



### entity/resource.lua
local function resource(resource_parameters, autoplace_parameters), autoplace = resource_autoplace.resource_autoplace_settings, base_density = autoplace_parameters.base_density 添加*27, 添加additional_richness = 1000000,


### Factorio/data/space-age/prototypes/recipe.lua
type = "recipe", name = "scrap-recycling", type = "item", name = "ice", probability = 0.05 -> 0.25, 
                                           type = "item", name = "holmium-ore", probability = 0.01 -> 0.21,



  {
    type = "recipe",
    name = "agricultural-science-pack",
    category = "organic",
    subgroup = "science-pack",
    surface_conditions =
    {
      {
        property = "pressure",
        min = 2000,
        max = 2000
      }
    },
    enabled = false,
    ingredients =
    {
      {type = "item", name = "bioflux", amount = 1},
      {type = "item", name = "pentapod-egg", amount = 1}

    },
    energy_required = 4,
    results = {{type="item", name="agricultural-science-pack", amount=1}},
    allow_productivity = true,
    crafting_machine_tint =
    {
      primary = {0.1, 0.2, 0.0, 1},
      secondary = {0.639, 0.764, 1, 1}
    }
  },

 复用metallurgic-science-pack 的条件，并调整配方 修改为

  {
    type = "recipe",
    name = "agricultural-science-pack",
    category = "metallurgy",
    surface_conditions =
    {
      {
        property = "pressure",
        min = 4000,
        max = 4000
      }
    },
    enabled = false,
    ingredients =
    {
      {type = "item", name = "holmium-plate", amount = 2},
      {type = "item", name = "superconductor", amount = 2},
      {type = "item", name = "supercapacitor", amount = 1},
    },
    energy_required = 10,
    results = {{type="item", name="agricultural-science-pack", amount=1}},
    allow_productivity = true
  },


  添加
  {
    type = "recipe",
    name = "tungsten-ore",
    enabled = true,
    surface_conditions =
    {
      {
        property = "pressure",
        min = 4000,
        max = 4000
      }
    },
    ingredients = {{type = "item", name = "tungsten-ore", amount = 1}},
    results = {{type="item", name="tungsten-ore", amount=100}},
    allow_productivity = true
  },
  {
    type = "recipe",
    name = "calcite",
    enabled = true,
    surface_conditions =
    {
      {
        property = "pressure",
        min = 4000,
        max = 4000
      }
    },
    ingredients = {{type = "item", name = "calcite", amount = 1}},
    results = {{type="item", name="calcite", amount=100}},
    allow_productivity = true
  },
  {
    type = "recipe",
    name = "coal",
    enabled = true,
    surface_conditions =
    {
      {
        property = "pressure",
        min = 4000,
        max = 4000
      }
    },
    ingredients = {{type = "item", name = "coal", amount = 1}},
    results = {{type="item", name="coal", amount=100}},
    allow_productivity = true
  },



### Factorio/data/space-age/prototypes/technology.lua

  {
    type = "technology",
    name = "agricultural-science-pack",
    icon = "__space-age__/graphics/technology/agricultural-science-pack.png",
    icon_size = 256,
    essential = true,
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "agricultural-science-pack"
      },
    },
    prerequisites = {"bioflux-processing", "bacteria-cultivation", "artificial-soil"},
    research_trigger =
    {
      type = "craft-item",
      item = "bioflux",
      count = 100
    }
  },

 复用electromagnetic-science-pack  修改为

  {
    type = "technology",
    name = "agricultural-science-pack",
    icon = "__space-age__/graphics/technology/agricultural-science-pack.png",
    icon_size = 256,
    essential = true,
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "agricultural-science-pack"
      },
    },
    prerequisites = {"electromagnetic-plant"},
    research_trigger =
    {
      type = "craft-item",
      item = "supercapacitor"
    }
  },

  
    type = "technology",
    name = "agriculture",

    
    type = "technology",
    name = "heating-tower",  prerequisites = {"planet-discovery-gleba"} -> {"planet-discovery-fulgora"},




